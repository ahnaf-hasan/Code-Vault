def check_odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"




number = int(input("Enter a number: "))

print(f"{number} is {check_odd_even(number)}.")
