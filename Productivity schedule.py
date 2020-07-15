# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 10:31:02 2020

@author: DELL
"""   
import random
answer1 = input("Have you ever listened to a joke before")
if answer1 == "Yes":
    print("I will tell you a joke")
else:
     print("Let me tell you a joke")
     while True:
         jokes = {"1":"What do you call a aligator in a vest a investigator!" ,
         "2":"Why did the banana go to the doctor because he did not peel himself" ,
         "3":"What do you call a sleeping bull? a bulldozer!" ,
         "4":"What has four wheels and a fly a garbage truck" ,
         "5":"What do you call a bear with no teeth a gummy bear" ,
         "6":"Why do golfers have 2 pairs of pants, in case they get a hole in one" ,
         "7":"What do you call a fly with no wings, a walk" ,
         "8":"What gets more wet the more it dries"}
kewyord = input("Enter the number of joke")
number = random.randint(1,8)
print(jokes[kewyord])
    

