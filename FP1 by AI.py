# Import the 'random' module to generate random numbers
import random

# Greet the user and ask for their name
print("Hello! What is your name?")

# Store the user's input in the varUserName variable
varUserName = input()

# Greet the user personally using their name
print(f"Hello, {varUserName}! Here are your lucky numbers:")

# Generate numbers for the powerball
num1 = random.randint(1, 69)
num2 = random.randint(1, 69)
num3 = random.randint(1, 69)
num4 = random.randint(1, 69)
num5 = random.randint(1, 69)
num6 = random.randint(1, 26)

# Print the numbers with the specified spacing
# Using an f-string automatically converts the numbers to strings
print(f"{num1}  {num2}  {num3}  {num4}  {num5}    {num6}")

# Display a farewell message
print(f"\nGood luck, {varUserName}!")