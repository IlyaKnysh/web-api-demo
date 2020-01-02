from config.driver_config import BROWSER

DATA_SOURCE = 'db_path'
DB_NAME = 'DB_NAME'
USER = 'user'
PASSWORD = 'password'
DRIVER = '{ODBC Driver 17 for SQL Server}' if BROWSER == 'remote' else '{SQL Server}'
