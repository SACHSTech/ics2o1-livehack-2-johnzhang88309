"""
--------------------------------------------------------
Name: triangle calculator.py
Purpose:To take the 3 sides of a shape and calculate if it is a triangle
 
Author: Zhang.J
 
Created: 23/02/2021
--------------------------------------------------------
"""
print("***** Triangle Calculator *****")
print ("")

#input statements for side lengths
side_1 = int(input("Enter the length of side 1: "))
side_2 = int(input("Enter the length of side 2: "))
side_3 = int(input("Enter the length of side 3: "))
print("")

#if statements, calculations, and print statements
if side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2 + side_3 > side_1:  
  print("It is a triangle. ")
else:
  print("It is not a triangle. ")