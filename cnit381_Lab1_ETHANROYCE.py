# Name: Ethan Royce
# CNIT-381 - section 001
# Lab 01
# You may do your work by editing this file, or by typing code at
# https://www.programiz.com/python-programming/online-compiler/ to
# check for result and copying it into the appropriate part of this file when
# you are done. When you are done, running this file should compute and
# print the answers to all the problems.
# Save this file with name in this format: cnit381_1_hw1_YOURNAME
# Submit this file to Stout's Canvas
import math # makes the math function available
from math import pi # makes the pi available
###
### Problem 1
### Write a Python program to convert radian to degree.
### Note: The radian is the standard unit of angular measure, used in many
### areas of mathematics. An angle's measurement in radians is numerically
### equal to the length of a corresponding arc of a unit circle; one radian is
### just under 57.3 degrees (when the arc length is equal to the radius).
### Hint: https://www.varsitytutors.com/hotmath/hotmath_help/topics/radian-to-degree-measure
### Sample output:
### Input radians: 10
### 572.7272727272727
print ("Problem 1 solution follows:")
radius = float(input("Input radians: ")) # Takes a float as an input of radius

def r_to_d(radius):
    degrees = radius * (180 / math.pi)
    return degrees

degrees = r_to_d(radius)
print(f"{radius} radians is equal to {degrees} degrees.")
###
### Problem 2
### Write a Python program which accepts the radius of a circle from the user and compute the area then print the it out.
### Sample Output :
### r = 1.1
### Area = 3.8013271108436504
print ("Problem 2 solution follows:")
radius = float(input ("Input the radius of the circle : ")) # Takes a float as an input of radius

def calculate_area(radius):
    area = math.pi * radius**2
    return area

area = calculate_area(radius)

print(f"The area of the circle with radius {radius} is: {area}")
###
### Problem 3
### Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black","Blue","Yellow"]
print ("Problem 3 solution follows:")

first_color = color_list[0]
last_color = color_list[5]

print("First color:", first_color)
print("Last color:", last_color)
###
### Problem 4
### Use list indexing to determine how many days are in a particular month
### based on the integer variable month, and store that value in the integer variable num_days.
### For example, if month is 8, num_days should be set to 31,
### since the eighth month, August, has 31 days.
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
month = 5
print ("Problem 4 solution follows:")

num_days = days_in_month[5]

print(num_days)
###
### Problem 5
### Select the three most recent dates from this list using list slicing notation.
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
'March 9, 2016']
print ("Problem 5 solution follows:")

eclipse_dates = eclipse_dates[7:11]

print(eclipse_dates)
###
### Problem 6
### print the maximum and minimum lenght of these lists by using len(), max(), min()
a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]
print ("Problem 6 solution follows:")

print(len(a), max(a), min(a))

print(len(b), max(b), min(b))

print(len(c), max(c), min(c))

# sample output: Max = 4, Min = 2
###
### Problem 7
### Given a list: names = ["Carol", "Albert", "Ben", "Donna"]
### use join() and sorted() to get this output:
### Albert & Ben & Carol & Donna
names = ["Carol", "Albert", "Ben", "Donna"]
print ("Problem 7 solution follows:")

namelist = " & ".join(names)

print(namelist)

###
### Problem 8
### Given a list: names = ["Carol", "Albert", "Ben", "Donna"]
### use append() to get this output:
### ["Carol", "Albert", "Ben", "Donna", "Eugenia"]
names1 = ["Carol", "Albert", "Ben", "Donna"]
print ("Problem 8 solution follows:")

names1.append('Eugenia')

print(names1)

###
### Problem 9
### Define a Dictionary, population,that provides information on
### the world's largest cities and print it out. The key is the name of a city
### a string), and the associated value is its population in millions of people.
### Key | Value
### Shanghai | 17.8
### Istanbul | 13.3
### Karachi | 13.0
### Mumbai | 12.5
print ("Problem 9 solution follows:")

largestcities = {"Shanghai": 17.8, "Istanbul": 13.3, "Karachi": 13.0, "Mumbai": 12.5}

print(largestcities)

###
### Problem 10
### Run the code below and explain the outcome

print("Problem 10:")

a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a == b)
print(a is b)
print(a == c)
print(a is c)

### First the print statement compares if a is equal to b, secondly, the 'is' statement is comparing if they have the same
### identity which since b = a, they do. Third, it is comparing if a is equal to c. Last, it is checking if a has the same
### identity as c, which it doesn't.