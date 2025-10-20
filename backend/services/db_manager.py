from backend.utils.hash import hash_password, hash_verification
from decimal import Decimal

class DBManager:

    def __init__(self, pool):
        self.pool = pool


    """ Public Methods """
    async def create_account(self, username:str, email:str, plain_password:str):
        # Check if username/email already exists
        try:
            username_exists = await self._username_exists(username)
        except Exception as e:
            print(f"Fatal Error in create_account() --> username_exists: {e}")
            return
        
        if username_exists:
            print("Error: username_already_exists")
            return {"type": "signup_error", "code": "username_exists"}
        
        try:
            email_exists = await self._email_exists(email)
        except Exception as e:
            print(f"Fatal Error in create_account() --> _email_exists")
            return
        
        if email_exists:
            print("Error: email_already_exists")
            return {"type": "signup_error", "code": "email_exists"}
        
        # Create account
        hashed_password = hash_password(plain_password)
        query = "INSERT INTO user (username, email, password) VALUES(%s, %s, %s)"
        
        try:
            await self._execute_query(query, (username, email, hashed_password))
        except Exception as e:
            print(f"Fatal Error in create_account() --> insert_into_user: {e}")
            return
        
        # Select id(user) per creare il portfolio
        query = "SELECT id FROM user WHERE username = %s"
        
        try:
            user_id_tuple = await self._execute_query(query, (username,))
            user_id = user_id_tuple[0][0]
        except Exception as e:
            print(f"Fatal Error in create_account() --> select_id_user: {e}")
            return
        
        # Create portfolio
        query = "INSERT INTO portfolio (user_id) VALUES (%s)"
        
        try:
            await self._execute_query(query, (user_id,))
        except Exception as e:
            print(f"Fatal Error in create_portfolio() --> inser_into_portfolio: {e}")
            return
        
        print("Type: SUCCESS, Account Created")
        return {"type": "signup_successful"}

    async def login(self, email:str, password:str):
        try:
            email_exists = await self._email_exists(email)
        except Exception as e:
            print(f"Fatal Error in login() --> _email_exists: {e}")
            return
        
        if not email_exists:
            print("Error: Unregistered email")
            return {"type": "login_error", "code": "email_exists"}
        
        # Return user data
        query = "SELECT password FROM user WHERE email = %s"
        
        try:
            response = await self._execute_query(query, (email,))
        except Exception as e:
            print(f"Fatal Error in login() --> select_password: {e}")
            return
        
        # Check if password match
        if not hash_verification(password, response[0][0]):
            print("Wrong Password")
            return {"type": "login_error", "code": "wrong_password"}
        
        # Return user data
        user_query = "SELECT id, username, email FROM user WHERE email = %s"
        portfolio_query = "SELECT id, balance FROM portfolio WHERE user_id = %s"
        position_query = "SELECT * FROM position WHERE portfolio_id = %s AND status = 'open'"
        
        try:
            user_response = await self._execute_query(user_query, (email,))
        except Exception as e:
            print(f"Fatal Error in login() --> user_response: {e}")
            return
        
        try:
            portfolio_response = await self._execute_query(portfolio_query, user_response[0][0])
        except Exception as e:
            print(f"Fatal Error in login() --> portfolio_response: {e}")
            return
        
        try:
            position_response = await self._execute_query(position_query, portfolio_response[0][0])
        except Exception as e:
            print(f"Fatal Error in login() --> position_response: {e}")
            return
        
        # Mapping user data
        user_data = {
            "info": {
                "id": int(user_response[0][0]),
                "username": str(user_response[0][1]),
                "email": str(user_response[0][2])
            },

            "portfolio": {
                "id": int(portfolio_response[0][0]),
                "balance": str(portfolio_response[0][1])
            },

            "position": [ 
                {
                    "id": int(position[0]),
                    "portfolio_id": int(position[1]),
                    "ticker": str(position[2]),
                    "execution_price": str(position[3]),
                    "size": str(position[4]),
                    "status": str(position[5]),
                    "created_at": str(position[6])
                } for position in position_response
            ]
        }
        
        print("Login Success")
        return {"type": "login_successful", "payload": {user_data}}


    async def deposit(self, portfolio_id:int, amount:Decimal):
        query = "UPDATE portfolio SET balance = balance + %s WHERE id = %s"
        
        try:
            response = await self._execute_query(query, (amount, portfolio_id))
        except Exception as e:
            print(f"Fatal Error in deposit() --> update_portfolio_balance: {e}")
            return
        
        if not response:
            print(f"Error deposit : id_mismatch")
            return {"type": "deposit_error_id_mismatch"}
        
        # Return new balance
        query = "SELECT balance FROM portfolio WHERE id = %s"

        try:
            balanceUpdated = await self._execute_query(query, (portfolio_id,))
        except Exception as e:
            print(f"Fatal Error in deposit() --> select_balance: {e}")
            return

        return {"type": "deposit_successful", "payload": {balanceUpdated}}
    
    async def withdraw(self, portfolio_id:int, amount:Decimal):
        query = "UPDATE portfolio SET balance = balance - %s WHERE id = %s"
        
        try:
            response = await self._execute_query(query, (amount, portfolio_id))
        except Exception as e:
            print(f"Fatal Error in withdraw() --> update_portfolio_balance: {e}")
            return
        
        if not response:
            print(f"Error withdraw : id_mismatch")
            return {"type": "withdraw_error_id_mismatch"}
        
        # Return new balance
        query = "SELECT balance FROM portfolio WHERE id = %s"
        
        try:
            balanceUpdated = await self._execute_query(query, (portfolio_id,))
        except Exception as e:
            print(f"Fatal Error in withdraw() --> select_balance: {e}")
            return
        
        return {"type": "withdraw_successful", "payload": {balanceUpdated}}
 
    async def execute_order(self,
                           portfolio_id:int,
                           ticker:str,
                           execution_price:str,
                           size:str):
        query = "INSERT INTO position (portfolio_id, ticker, execution_price, size) VALUES(%s,%s,%s,%s)"
        
        try:
            await self._execute_query(query, (portfolio_id, ticker, Decimal(str(execution_price)), Decimal(str(size))))
        except Exception as e:
            print(f"Fatal Error in execute_order(): {e}")
            return
        
        return {"type": "order_executed"}


    async def close_position(self, position_id:int):
        query = "UPDATE position SET status = 'closed' WHERE id = %s"
        
        try:
            response = await self._execute_query(query, (position_id,))
        except Exception as e:
            print(f"Fatal Error in close_position(): {e}")
            return
        
        if not response:
            print(f"Error close_position: id_mismatch")
            return {"type": "close_position_error_id_mismatch"}
        
        return {"type": "positon_closed"}
    

    """ Private Methods """
    async def _execute_query(self, query:str, params:str):
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(query, params)
                if query.strip().upper().startswith("SELECT"):
                    return await cursor.fetchall()
                else:
                    return cursor.rowcount
                

    async def _username_exists(self, username:str):
        query = "SELECT username FROM user WHERE username = %s"
        
        try:
            response = await self._execute_query(query, (username,))
        except Exception as e:
            print(f"Fatal Error in _username_exists(): {e}")
            return
        
        return bool(response)


    async def _email_exists(self, email:str):
        query = "SELECT email FROM user WHERE email = %s"
        
        try:
            response = await self._execute_query(query, (email,))
        except Exception as e:
            print(f"Fatal Error in _email_exists(): {e}")
            return
        
        return bool(response)