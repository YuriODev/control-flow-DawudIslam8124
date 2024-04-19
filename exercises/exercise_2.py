# Your solution to Exercise 2
age = int(input("Enter age: "))

if age <= 1:
  print("Infant")
elif age >= 1 and age < 13:
  print("Child")
elif age > 13 and age < 20:
  print("Teenager")
elif age > 20:
  print("Adult")
