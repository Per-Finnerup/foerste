# ** Temperatur konverter **
#         10.12.2019.
#     Per Finnerup Larsen
# **       Python 3       **
import os, sys

#Denne funktion konverterer fharenheit til celsius og viser resultatet
def celsius_func(temp_fahrenheit):
    #temp_fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
    temp_celsius = float((temp_fahrenheit - 32) / 1.8)
    print(temp_celsius)
 
def fahrenheit_func(temp_celsius):
    #temp_celsius = float(input("Enter a temperature in Celsius: "))
    temp_fahrenheit = float((temp_celsius * 1.8) + 32)
    print(temp_fahrenheit)
 
#temp_celsius = float(input("Enter a temperature in Celsius: "))
#print(type (Celsius))

#print (sys.argv)
#print ("This python program filename is", sys.argv[0])
#print ("This python program filename is " + sys.argv[0])
#print ("This python program filename is {}".format(sys.argv[0]))

#print ("Temp input =", sys.argv[1])

if len(sys.argv) == 3:
    print ("Temp input =", sys.argv[1])
    fahrenheit_func(float(sys.argv[1]))
    print ("Temp input =", sys.argv[2])
    celsius_func(float(sys.argv[2]))
