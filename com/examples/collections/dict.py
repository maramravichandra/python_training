data = {
    "name" : "Ravi",
    "location" : "NJ",
    "current_address" : "913",
    "previous_address": [
        {
            "2024" : "address of 2023 dsfafd"
        },
        {
            "2023" : "address of 2023"
        }
    ]
}

print("Name is ", data['name'])
print("Name is ", data['previous_address'])

previous_address = [ add['2023'] for add in data['previous_address'] if '2023' in add ]
print(previous_address)

data["zipcode"] = "08817"
print(data)

data["zipcode"] = "08816"
print(data)

del data["zipcode"]
print(data)

print( data.get("zipcode", "default"))
print( data.keys() )
print( data.values() )

for key,value in data.items():
    print(key,value)

previous_address = [ add['2023'] for add in data['previous_address'] if '2023' in add ]
print(previous_address)

dict1 = {'a':1, "b":2}
dict2 = {'a':3, "c":2}

print("Merging dict : ", {**dict1, **dict2} )
print("Merging dict : ", {**dict2, **dict1} )

employee_data = {
    {
        "id" : 100,
        "sal" : 100000
    },
    {
        "id": 1001,
        "sal": 120000
    },
    {
        "id": 1002,
        "sal": 1340000
    },
    {
        "id": 1003,
        "sal": 1444000
    }, {
        "id" : 1004,
        "sal" : 177000
    }, {
        "id" : 1005,
        "sal" : 1990000
    }
}

# find out max salary of employee





