from random import *
import os

u_pwd = input("Enter A Password: ")
pwd = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','y','z','1','2','3','4','5','6','7','8','9','10']

pw = ""
while(pw!=u_pwd):
    pw = ""

    for letter in range(len(u_pwd)):
        guess_pwd = pwd[randint(0,17)]
        pw = str(guess_pwd) + str(pw)
        print(pw)
        print("Cracking Password...Please Wait!")
        os.system("cls")

    if pw == u_pwd:
        break

print("Your Password Is: ",pw)
