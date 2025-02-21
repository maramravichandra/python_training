import boto3

iam = boto3.resource("iam")
def list_users():
    users = list(iam.users.all())
    print("All Users", str(users))


list_users()

