#!/usr/bin/env python3
# Created by: Shem
# Created on: 11/14/2025
# This program calculates the factorial of a positive number using a loop.
# this is my code

def main():
    # Start the loop counter at 0
    loop_counter = 0
    # Initialize factorial to 1
    factorial = 1
    try:
        # Ask the user for a positive integer
        user_number = int(input("Enter a positive number: "))
        print("")

        # Check if the number is negative
        if user_number < 0:
            print("Enter a number above 0")
        else:
            # Loop until the loop_counter reaches the user_number
            while True:
                # Increase loop counter by 1 each time
                loop_counter = loop_counter + 1
                # Multiply factorial by the current counter
                factorial = factorial * loop_counter
                # Show how many times the loop has run
                print("Tracking {} times through loop.".format(loop_counter))
                # Stop looping once we reach the user's number
                if loop_counter >= user_number:
                    break
            print("")
            # Display the final factorial result
            print("{}! = {}".format(user_number, factorial))

    except ValueError:
        # Handle cases where input is not a valid integer
        print("Invalid input! Please enter a valid positive integer.")


# Makes sure main() runs only when the file is executed directly
if __name__ == "__main__":
    main()
