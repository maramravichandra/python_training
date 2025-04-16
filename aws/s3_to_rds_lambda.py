import json

def lambda_handler(event, context):
    print("Received event: " , event)
    data = json.loads(event)
    records = data['Records']
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
            object['objectSize'] = record['s3']['object']['size']
            print("Object: ", object)
            objects.append(object)
        return {"statusCode": 200, "objects": objects}
    except Exception as e:
        print(e)
        raise e

