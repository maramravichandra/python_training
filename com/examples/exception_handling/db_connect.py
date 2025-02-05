#pip install psycopg2
import psycopg2

def connect_db(retry=0):
    connection = psycopg2.connect(
        dbname = "practice",
        user = "postgres",
        password = "vals@1230",
        host = "localhost"
    )
    cur = connection.cursor()
    try:
        # queries
        cur.execute("insert into employee(id,name,address,sal) values(100,'Ravi', 'Edison,NJ', 1000000)")
        connection.commit()
        cur.execute("Select * from employee")
        print("Row count : ", cur.rowcount)
    except TimeoutError:
        print("Timed out.")
        if retry == 3:
            raise Exception("Database is taking loger time to execute your query Or db is not responding")
        else:
            print("Retrying..")
            connect_db( retry + 1)
    except Exception as exp:
        print("Error : ", exp)
    finally:
        cur.close()
        print("Closing the connection.")

connect_db()