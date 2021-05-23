from utilities.configuration import *


def buildPayloadfromDB(query):
    AddBody = {}
    tp = getQuery(query)
    AddBody["name"] = tp[0]
    AddBody["isbn"] = tp[1]
    AddBody["aisle"] = tp[2]
    AddBody["author"] = tp[3]
    # print(AddBody)
    return AddBody

