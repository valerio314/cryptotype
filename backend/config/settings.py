# Database Configuration
POOL_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root", 
    "password": "rootroot",
    "db": "cryptotype",
    "autocommit": True,
    "minsize": 5,
    "maxsize": 10
}

# Server Configuration  
HTTP_SERVER_CONFIG = {
    "host": "localhost",
    "port": 8080
}

WS_SERVER_CONFIG = {
    "host": "localhost",
    "port": 8000
}

APP_NAME = "Cryptotype"