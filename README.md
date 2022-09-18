# README For FizzBuzz Script

This is a simple script written in Python 3.7.10 for the FizzBuzz game.

## How It Works

The script executes by:

1. Printing "fizz" if the current number is divisible by 3 with no remainder.
2. Printing "buzz" if the current number is divisible by 5 with no remainder.
3. Printing "fizzbuzz" if the current number is divisible by both 3 and 5 with no remainder.
4. Not printing anything if the current number is not divisible by 3 or 5 with no remainder and then moving to the next number.

The first set of numbers are generated using the range function to create a range of 1 to 100 to loop through for the first implementation, where simple print statements print the output during the for loop.

The second set of numbers are generated using the range function to create a range of 101 to 200 to loop through for the second implementation. 

This time however, the evaluation for fizz, buzz, fizzbuzz, or pass is processed differently. The second implementation uses the first for loop to add the number and print value as a key : value pair to a dictionary.

The dictionary is then iterated through after it has been filled by a second for loop to print the values of the dictionary.

## How to Run the Script

This script does not take much to run. The steps are below.

1. Make sure Python 3.7.10 is installed on your device
2. Clone the repository to your local machine.
3. Navigate to the folder where the script is located.
4. Run from the command line or command prompt using
```
python fizzbuzz.py
```