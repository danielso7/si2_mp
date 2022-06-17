# 
# File: db.py
# Author: Daniel Oliveira
# Mec. Number: 89208
# Course: Sistemas Inteligentes II
# Date: 17th June of 2022
#

### MySQL Database Initial Definition and Handling ###

## Import dependencies ##

from mysql.connector import *

## Create MySQL Database, if there is none with the same name ##

def createDB():
    try:
        with connect(host="localhost", user="root", password="pass") as connection:
            create_db = "CREATE DATABASE IF NOT EXISTS `crexusers` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;"
            with connection.cursor() as cursor:
                cursor.execute(create_db)
    except Error as e:
        print(e)

## Create table inside the database, if there is none with the same name ##

def createTable():
    try:
        with connect(host="localhost", user="root", password="pass", database="crexusers") as connection:
            create_table ="""CREATE TABLE IF NOT EXISTS `accounts` (
	                      `id` int(11) NOT NULL AUTO_INCREMENT,
  	                      `username` varchar(50) NOT NULL,
                          `name` varchar(100) NOT NULL,
  	                      `password` varchar(255) NOT NULL,
  	                      `email` varchar(100) NOT NULL,
                          `balance` int(255) NOT NULL,
                          PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;"""
            with connection.cursor() as cursor:
                cursor.execute(create_table)
                connection.commit()
    except Error as e:
        print(e)

## Print current database state ##      

def printDB():
    connection = connect(host="localhost", user="root", password="pass", database="crexusers")
    show ="SELECT * FROM accounts"
    with connection.cursor() as cursor:
        cursor.execute(show)
        result = cursor.fetchall()
    for row in result:
        print(row)

## Create initial accounts with user data and insert them into the database ##

def insertInitialAccounts():
    connection = connect(host="localhost", user="root", password="pass", database="crexusers")
    ins = """INSERT INTO `accounts` (`id`, `username`, `name`, `password`, `email`, `balance`) 
          VALUES 
          (1, 'daniel', 'Daniel Oliveira', 'pass1', 'danielsoliveira@ua.pt', 0),
          (2, 'diogo', 'Diogo Silva', 'pass2', 'diogosilva@ua.pt', 0),
          (3, 'pedro', 'Pedro Ferreira', 'pass3', 'pedroferreira@ua.pt', 0),
          (4, 'maria', 'Maria Sousa', 'pass4', 'mariasousa@ua.pt', 0),
          (5, 'joana', 'Joana Castro', 'pass5', 'joanacastro@ua.pt', 0)
          """
    with connection.cursor() as cursor:
        cursor.execute(ins)
        connection.commit()

## Remove one chosen user ##

def removeUser(user):
    connection = connect(host="localhost", user="root", password="pass", database="crexusers")
    deluser = "DELETE FROM accounts WHERE username=" + user
    with connection.cursor() as cursor:
        cursor.execute(deluser)
        connection.commit()

## Delete existing database ##

def deleteDB():
    connection = connect(host="localhost", user="root", password="pass", database="crexusers")
    deldb = "DROP DATABASE crexusers"
    with connection.cursor() as cursor:
        cursor.execute(deldb)
        connection.commit()

## Update user BTC balance, buying more or selling what he currently have ##

def updateBalance(id,new,flag):
    connection = connect(host="localhost", user="root", password="pass", database="crexusers")
    if flag:
        update = "UPDATE accounts SET balance = balance + " + str(new) + " WHERE id = " + str(id)
    else:
        update = "UPDATE accounts SET balance = GREATEST(0, balance - " + str(new) + ") WHERE id = " + str(id)
    with connection.cursor() as cursor:
        cursor.execute(update)
        connection.commit()

## Update user password on the database ##

def updatePassword(id,new):
    connection = connect(host="localhost", user="root", password="pass", database="crexusers")

    update = "UPDATE accounts SET password = '" + str(new) + "' WHERE id = " + str(id)

    with connection.cursor() as cursor:
        cursor.execute(update)
        connection.commit()

## Update user email on the database ##

def updateEmail(id,new):
    connection = connect(host="localhost", user="root", password="pass", database="crexusers")

    update = "UPDATE accounts SET email = '" + str(new) + "' WHERE id = " + str(id)

    with connection.cursor() as cursor:
        cursor.execute(update)
        connection.commit()

## Initial function to create database, table and insert accounts ##

def initializeDB():
    createDB()
    createTable()
    insertInitialAccounts()

## Main function just to print current state of database ##

def main():
    printDB()

## Run directly to check database ##

if __name__ == "__main__":
    main()

