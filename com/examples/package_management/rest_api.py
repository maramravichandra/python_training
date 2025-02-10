import requests

respose = requests.get("https://www.ebi.ac.uk/biosamples/samples/SAME123271.json")
print(respose.text)

respose = requests.get("https://google.com")
print(respose.text)