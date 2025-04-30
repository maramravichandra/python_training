import json
import os
import pymysql
import sys

user_name = 'admin' #os.environ['USER_NAME']
password = os.environ['PASSWORD']
rds_proxy_host = os.environ['RDS_PROXY_HOST']
db_name = os.environ['DB_NAME']

def get_connection():
    try:
        print("User name:", user_name)
        print("Password:", password)
        print("RDS Proxy host:", rds_proxy_host)
        print("DB name:", db_name)
        conn = pymysql.connect(host=rds_proxy_host, port=3306, user=user_name,
                               passwd=password, db=db_name, connect_timeout=600)
        print("SUCCESS: Connection to RDS MySQL instance succeeded")
        return conn
    except Exception as e:
        print(e)
        sys.exit(1)

def insert_records(data):
    print("Inserting records")
    conn = get_connection()
    print("SUCCESS: Connection to RDS MySQL instance succeeded")
    insert_sql = f"""insert into image_details(bucketName, awsRegion, eventName, 
    eventTime, sourceIPAddress, objectKey) values(%s,%s,%s,%s,%s,%s)"""
    print("Inserting Query: ", insert_sql)
    with conn.cursor() as cur:
        cur.execute("""create table if not exists image_details (bucketName varchar(100) not null, 
        awsRegion varchar(200) , eventName varchar(100) , eventTime varchar(100) , sourceIPAddress varchar(100) , objectKey varchar(200) )""")
        for record in data:
            cur.execute(insert_sql, (record['bucketName'],record['awsRegion'],record['eventName']
                                     ,record['eventTime'],record['sourceIPAddress'],record['objectKey']))
        conn.commit()


def lambda_handler(event, context):
    print("Received event: " , event)
    records = event['Records']
    print("Records: ", records)
    bucket = records[0]['s3']['bucket']['name']
    print("Bucket Name: ", bucket)
    try:
        objects = []
        for record in records:
            object = dict()
            object['bucketName'] = bucket
            object['awsRegion'] = record['awsRegion']
            object['eventName'] = str(record['eventName']).split(":")[0]
            object['eventTime'] = record['eventTime']
            object['sourceIPAddress'] = record['requestParameters']['sourceIPAddress']
            object['objectKey'] = record['s3']['object']['key']
            print("Object: ", object)
            objects.append(object)
        insert_records(objects)
        response = {"statusCode": 200, "objects": objects}
        print("Response: ", response)
        return response
    except Exception as e:
        print(e)
        raise e