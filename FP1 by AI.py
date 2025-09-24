# Import the necessary modules
import random
import time

# ANSI escape codes for colors
RED = '\033[91m'
RESET = '\033[0m' # Resets the color back to default

# Have a greeting that asks the user for their name
print("Hello! Welcome to the Lucky Number Generator.")
varUserName = input("What is your name? ")

# Greet the user by calling them by their name
print(f"It's a pleasure to meet you, {varUserName}!")
print("Let's generate your six lucky numbers...")
time.sleep(1) # A small pause for dramatic effect

# Generate the numbers beforehand
num1 = random.randint(1, 69)
num2 = random.randint(1, 69)
num3 = random.randint(1, 69)
num4 = random.randint(1, 69)
num5 = random.randint(1, 69)
powerball = random.randint(1, 26)

# Print the numbers one by one with a delay
print("\nHere are your numbers:")

# We use 'end' to print spaces instead of a newline,
# and 'flush=True' to ensure the number appears immediately.
print(num1, end='  ', flush=True)
time.sleep(0.25)

print(num2, end='  ', flush=True)
time.sleep(0.25)

print(num3, end='  ', flush=True)
time.sleep(0.25)

print(num4, end='  ', flush=True)
time.sleep(0.25)

# Print the 5th number with four spaces after it
print(num5, end='    ', flush=True)
time.sleep(0.25)

# Print the final number in red and then reset the color
print(f"{RED}{powerball}{RESET}")


# After complete, have a farewell message for the user
print(f"\nGood luck, {varUserName}! Have a wonderful day.")