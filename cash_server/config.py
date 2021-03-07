DB_USER = "postgres"
DB_PASSWORD = "DQnqGP6y"
DB_HOST = "db"
DB_PORT = "5432"
DB_NAME = "cash"

APP_HOST = '0.0.0.0'
APP_PORT = 5000

db_str = "postgresql+psycopg2://%s:%s@%s:%s/%s" % (DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
