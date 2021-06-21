# DB_USER = "root"
DB_USER = "postgres"  # docker-compose
# DB_PASSWORD = "postgres"  # docker-compose
# DB_PASSWORD = "DQnqGP6y"
DB_PASSWORD = "DQnqGP6y"  # docker-compose
DB_HOST = "localhost"
# DB_HOST = "db"    # docker-compose
DB_PORT = "5432"
# DB_PORT = "5432"  # docker-compose
DB_NAME = "cash"

APP_HOST = '0.0.0.0'
APP_PORT = 5037

db_str = "postgresql+psycopg2://%s:%s@%s:%s/%s" % (DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
