import configparser
import mysql.connector
from mysql.connector import Error


def getconfig():
    config = configparser.ConfigParser()
    config.read(".\\utilities\\properties.ini")
    return config


config = getconfig()
con_config = {

        "host": config["SQL"]["host"],
        "database": config["SQL"]["database"],
        "user": config["SQL"]["user"],
        "password": config["SQL"]["password"]
    }


def connectToDatbase():
    try:
        # conn = mysql.connector.connect(host="localhost", database="APIDevelop", user="root", password="root")
        conn = mysql.connector.connect(**con_config)
        if conn.is_connected():
            print("Connection Success")
            return conn
    except Error as e:
        print(e)


def getQuery(query):
    conn = connectToDatbase()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    # print(row)
    return row
