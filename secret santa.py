#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      15Richardsonc
#
# Created:     27/11/2018
# Copyright:   (c) 15Richardsonc 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from random import shuffle

number=int(input("How many people do you want to include? "))

people=[]

for i in range (number):
    people.append(input("Please enter one person: "))

shuffle(people)
offset = [people[-1]] + people[:-1]
for santa, receiver in zip(people, offset):
     print(santa, "buys for", receiver)