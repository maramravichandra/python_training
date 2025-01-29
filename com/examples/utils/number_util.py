def sum( numbers ):
    result = 0
    for number in numbers:
        result = result + int(number)
        print("Current result ", result)
    return result