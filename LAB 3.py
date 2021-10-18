#Miguel jusino
# oct 12

#Problem 1 – Write a program that prints “Hello World” to the screen
print ("hello world")

#Problem 2 – Write a program that asks the user for their name and greets them with their name.
NAME = input(" name:")
print("hello", NAME)

#Problem 3 – Modify the previous program such that only the users you and your instructor are greeted with their names. (**USED NAME FROM PROBLEM 2 ASWELL**)
NAME2 = input(" name2:")
print("hello", NAME, "and", NAME2)

#Problem 4 - Write a program that will compute the area of a circle. Prompt the user to enter the radius and print a nice message back to the user with the answer.
pi = 3.147
print("area of circle")
print (pi)

#Problem 5 - Write a program that will compute MPG for a car. Prompt the user to enter the number of miles driven and the number of gallons used. Print a nice message with the answer.
Miles = int(input(" Current Miles: "))
Gallons = int(input("Gallons Used: "))
print("thank you you MPG is: ", Miles/Gallons)

#Problem 6 - Write a program that will convert degrees Fahrenheit to degrees Celsius.
celsius = float(input("Celsius: "))
fahrenheit = (celsius * 9/5)+32
fahrenheit = round(fahrenheit,2)
print (celsius,'celsius is: ',fahrenheit, 'fahrenheit ')

#Problem 7 - It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday. If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights you would return home on a Saturday (day 6) Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the number of day of the week you will return on.
      startday = int(input(" what day is 0-6"))
daystowait = int(input("how many days of vacation? "))
end_day = (startday + daystowait)
print (end_day)
          

