import sys

from dask.array.ufunc import da_frompyfunc


def find_division():
    try:
        numerator = int(input("Enter the numerator : "))
        denominator = int(input("Enter the denominator : "))
        print(f"Result of {numerator}/{denominator} is {numerator/denominator}")
    except ZeroDivisionError:
        print("Got 0 as denominator. Please enter the number other then 0.")
        sys.exit()


def read_file():
    file_path = input("Enter absolute path of a file to print the content :")

    try:
        with open(file_path) as file:
            print("Content: ", str(file.readlines()))
    except FileNotFoundError:
        print(f"File {file_path} not found. Please enter valid file path.")
        sys.exit(-1)
    finally:
         print("Getting finally block")


read_file()

def connect_db(retry=0):
    driver_url = ""
    connection = None
    try:
        # queries
        print("")
    except TimeoutError:
        # print the error
        if retry == 3:
            raise Exception("Database is taking loger time to execute your query Or db is not responding")
        else:
            connect_db( retry + 1)
    finally:
        # Close the connection
        print("")






