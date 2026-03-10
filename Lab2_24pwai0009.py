
# TASK-01: Personal Info Collector

# Step 1: Ask the user for their full name and store it as a string
full_name = input("Enter your full name   : ")

# Step 2: Ask for their favorite color (also a string)
fav_color = input("Enter your favorite color: ")

# Step 3: Ask for birth year – we use int() to convert the text into a number
birth_year = int(input("Enter your birth year  : "))

# Step 4: Calculate age by subtracting birth year from the current year (2026)
current_year = 2026
age = current_year - birth_year

# Step 5: Print 3 formatted lines using f-strings
# f-strings start with f" and let us insert variables directly using { }
print(f"\nWelcome, {full_name}!")
print(f"Your favorite color is {fav_color} – perfect for calm AI thinking.")
print(f"You were born in {birth_year} → you are currently {age} years old ({current_year}).")
 
 
# TASK-02: Mini Calculator

# Step 1: Get two numbers – float() allows decimals like 5.5
num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number: "))

# Step 2: Show available operations and get the user's choice
print("Available operations: + - * / ** %")
op = input("Choose an operation : ").strip()  # .strip() removes accidental spaces

# Step 3: Validate – if operator is not in the allowed list, stop here
if op not in ["+", "-", "*", "/", "**", "%"]:
    print("Invalid operator!")

# Step 4: If dividing by zero, print error and stop
elif op == "/" and num2 == 0:
    print("Cannot divide by zero!")

# Step 5: All good – perform the calculation
else:
    if op == "+":
        result = num1 + num2
        print(f"\n  {num1} + {num2} = {result}")

    elif op == "-":
        result = num1 - num2
        print(f"\n  {num1} - {num2} = {result}")

    elif op == "*":
        result = num1 * num2
        print(f"\n  {num1} * {num2} = {result}")

    elif op == "/":
        result = num1 / num2
        print(f"\n  {num1} / {num2} = {result:.2f}")   # :.2f → 2 decimal places

    elif op == "**":
        result = num1 ** num2
        print(f"\n  {num1} ** {num2} = {result:.2f}")  # :.2f → 2 decimal places

    elif op == "%":
        result = num1 % num2
        print(f"\n  {num1} % {num2} = {result}")
        
        
# TASK-03: Even or Odd Checker
# CHALLENGE A – Even / Odd & Multiple Checker


print("=" * 45)
print("  CHALLENGE A – Even/Odd & Multiple Checker")
print("=" * 45)

# Step 1: Get the range from the user
start = int(input("Enter starting number: "))
end   = int(input("Enter ending number  : "))

# Step 2: Set current to the starting number
current = start

# Step 3: Loop until current goes past the ending number
while current <= end:

    # Step 4: Skip any number divisible by 7 – 'continue' jumps
    # straight back to the top of the loop without printing
    if current % 7 == 0:
        current += 1   
        continue

    # Step 5: Check all three conditions using if / elif / else
    if current % 2 == 0 and current % 5 == 0:
        # Divisible by BOTH 2 and 5
        print(f"  {current} → Even & Multiple of 5!!")

    elif current % 5 == 0:
        # Divisible by 5 only
        print(f"  {current} → Multiple of 5!")

    elif current % 2 == 0:
        # Divisible by 2 only
        print(f"  {current} → Even")

    else:
        # Not divisible by 2 or 5
        print(f"  {current} → Odd")

    current += 1   # Step 6: move to the next number

print()



# CHALLENGE B – Password Strength Checker


print("=" * 45)
print("  CHALLENGE B – Password Strength Checker")
print("=" * 45)

# Step 1: Get a password from the user
password = input("Enter a password: ")

# Step 2: Check length first – must be at least 6 characters
if len(password) < 6:
    print("Too short!")

else:
    # Step 3: Nested check – must contain at least one digit
    # any() goes through each character and checks if it is a digit
    has_digit = any(char.isdigit() for char in password)

    if not has_digit:
        print("Add at least one number.")

    else:
        # Step 4: Nested check – must contain at least one uppercase letter
        has_upper = any(char.isupper() for char in password)

        if not has_upper:
            print("Add at least one capital letter.")

        else:
            # Step 5: All checks passed!
            print("Strong password – good choice!")

print("=" * 45)