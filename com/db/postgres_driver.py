import psycopg2

class PostgresDriver:
    host = ""
    username = ""
    password = ""
    dbname = ""
    connection = None

    def __init__(self, host, username, password, dbname ):
        self.host = host
        self.username = username
        self.password = password
        self.dbname = dbname
        self.__establish_connection__()

    def __establish_connection__(self):
        print("Establishing connection..")
        self.connection = psycopg2.connect(
            dbname = self.dbname,
            user = self.username,
            password = self.password,
            host = self.host
        )

    def insert_data(self, data):
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"insert into employee(id,name,address,sal) values({data})")
            self.connection.commit()
        except Exception as exp:
            print("Error : ", exp)
        finally:
            cursor.close()

    def read_data(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            records = cursor.fetchall()
            return records
        except Exception as exp:
            print("Error : ", exp)
        finally:
            cursor.close()

    def close_connection(self):
        self.connection.close()