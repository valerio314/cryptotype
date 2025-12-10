"""
class User:
    def __init__(self, id=None, username=None, email=None, password=None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
    
    def __repr__(self):
        return f"User (id={self.id}, username={self.username}, email={self.email})"

class Portfolio:
    def __init__(self, id=None, user_id=None, balance=0.00):
        self.id = id
        self.user_id = user_id
        self.balance = balance
    
    def __repr__(self):
        return f"Portfolio (id={self.id}, user_id={self.user_id}, balance={self.balance})"

class Position:
    def __init__(self, id=None, portfolio_id=None, ticker=None, 
                 execution_price=None, size=None, status='open', 
                 created_at=None, closed_at=None):
        self.id = id
        self.portfolio_id = portfolio_id
        self.ticker = ticker
        self.execution_price = execution_price
        self.size = size
        self.status = status
        self.created_at = created_at
        self.closed_at = closed_at
    
    def __repr__(self):
        return f"Position (id={self.id}, ticker={self.ticker}, status={self.status})"
"""