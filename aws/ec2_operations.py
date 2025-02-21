import boto3


ec2 = boto3.client("ec2")
def list_ec2_instances():
    instances = ec2.describe_instances()
    print("Ec2 instances : ", str(list(instances)))
    resvations = instances['Reservations']
    print("Ec2 resvations instances : ", str(list(resvations)))
    responseMetadata = instances['ResponseMetadata']
    print("Ec2 responseMetadata instances : ", str(list(responseMetadata)))

list_ec2_instances()