#This program is a simple Four Function Calculator using else if statements to add,subtract,multiply,or divide.

num1 = int(input("enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

print("Choose calculation: \n"
    "Add \n"
    "Subtract \n"
    "Multiply \n"
    "Divide")

calc = input()
if calc == "Add":
    ans = num1 + num2
elif calc == "Subtract":
    ans = num1 - num2
elif calc == "Multiply":
    ans = num1 * num2
elif calc == "Divide":
    ans = num1 / num2

print(ans)