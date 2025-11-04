#Task : Calculator 

num1=float(input("Enter 1st number: "))
num2=float(input("Enter 2nd number: "))


#Operation Menu
print("Select Operation")
print("1. Choose '+'")
print("2. Choose '-'")
print("3. Choose '*'")
print("4. Choose '/'")

choice = input("Enter your operation(+ , - , * , /)")

if choice == "+" :
    result = num1 + num2
elif choice == "-":
    result = num1 - num2
elif choice == "*":
    result = num1 * num2
elif choice == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error ! cannot devide by 0"
else :
    result = "Invalid Operation"


print(f"\n result: {result}")


