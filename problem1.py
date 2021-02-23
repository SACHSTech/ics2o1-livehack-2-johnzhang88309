"""
--------------------------------------------------------
Name: Speed and speeding calculator.py
Purpose:To calculate if someone is speeding given the speed limit and the recorded speed of the car 
 
Author: Zhang.J
 
Created: 23/02/2021
--------------------------------------------------------
"""
print("***** Speed and Speeding Calculator *****")
print("")

#input statements for speed limit and recorded speed
speed_limit = int(input("Enter the speed limit: "))
recorded_speed = int(input("Enter the speed of your car: "))
print("")

#calculations, if statements and printing
speed_difference = recorded_speed - speed_limit
if speed_difference <= 0: 
  print ("Congragulations, you are within the speed! ")
elif speed_difference >= 1 and speed_difference <= 20:
  print ("You are speeding and your fine is $100") 
elif speed_difference >= 21 and speed_difference <= 30: 
  print ("You are speeding and your fine is $270")
else: 
  print("You are speeding and your fine is $570")






