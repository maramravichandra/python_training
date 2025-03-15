import sys

import boto3
import json
import mysql.connector

# Initialize AWS Secrets Manager client
secrets_manager = boto3.client('secretsmanager', region_name = 'us-east-1')
db_host = "mydb.c4bsuga2er7o.us-east-1.rds.amazonaws.com"


# Getting username, password from secret manager
def get_secretvalue():
    secret_name = secrets_manager.get_secret_value(SecretId='rds!db-6d38e2e8-8b91-4130-8422-9aa117ec0519')
    secret_dict = json.loads(secret_name['SecretString'])
    db_username = secret_dict['username']
    db_password = secret_dict['password']
    return db_username, db_password


def execute_query(db_name, table_name, files, s3_base_dir, created_user):
    db_username, db_password = get_secretvalue()
    print("db_name : ", db_name)
    print("table_name :", table_name)
    print("Secrets: {} : {}", db_username, db_password)

    connection = mysql.connector.connect(
        host=db_host,
        user=db_username,
        password=db_password,
        database=''
    )
    cursor = connection.cursor()
    cursor.execute("create database if not exists {}".format(db_name))
    cursor.execute("create table if not exists {}.{}( name varchar(100), createdby varchar(50), created_date date, location varchar(200))".format(db_name, table_name))
    connection.commit()
    cursor.close()
    connection.close()

    try:
        connection = mysql.connector.connect(
            host=db_host,
            user=db_username,
            password=db_password,
            database=db_name
        )
        insert_query = """insert into {}.{}(name, createdby, created_date, location)
                          values( '{}', '{}', current_date(), '{}' )"""
        cursor = connection.cursor()
        for file in files:
            formatted_query = insert_query.format(db_name, table_name, file, created_user, s3_base_dir)
            print("Formatted Query : ", formatted_query)
            cursor.execute(formatted_query)

        connection.commit()
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        connection.close()


# Input & function call
if __name__=="__main__":
    db_name = sys.argv[1]
    print("Db Name", db_name)
    table_name = sys.argv[2]
    print("Table Name", table_name)
    files = sys.argv[3].split(" ")
    print("Files", files)
    s3_base_dir = sys.argv[4]
    print("S3 base directory", s3_base_dir)
    created_user = sys.argv[5]
    print("Created User", created_user)
    execute_query(db_name, table_name, files, s3_base_dir, created_user)