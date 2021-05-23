import requests
from utilities.payload import *
from utilities.configuration import *
from utilities.resource import *


print("------------Adding book in Library")
url = config["API"]["endpoint"] + GetApiResource.AddBook
headers = {"Content-Type": "application/json"}
query = "select * from Books2;"

addBook_response = requests.post(url, json=buildPayloadfromDB(query), headers=headers,)
print(addBook_response.status_code)
print("History is ", addBook_response.history)
print(addBook_response.text)

addBook_json = addBook_response.json()
id = addBook_json["ID"]
print("Book id is :" + id)

print("---------------Getting book from Library------------")
url1 = config["API"]["endpoint"] + GetApiResource.GetBook
params = {"ID": id}
getbook_response = requests.get(url1, params=params,)
print(getbook_response.status_code)
print(getbook_response.text)

print("---------------Deleting book from library--------")
url2 = config["API"]["endpoint"] + GetApiResource.DeleteBook
jsonBody = {"ID": id}
delBook_resopnse = requests.post(url2, json=jsonBody, headers=headers)
print(delBook_resopnse.status_code)
print(delBook_resopnse.text)


