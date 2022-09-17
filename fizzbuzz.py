
# Basic Fizz Buzz Application using print statements

count = range(1,100)

for num in count:
    if num % 3 == 0 and num % 5 == 0:
        print(f'{num} - fizzbuzz')
    elif num % 3 == 0 and num % 5 != 0:
        print(f'{num} - fizz')
    elif num % 3 != 0 and num % 5 == 0:
        print(f'{num} - buzz')
    else:
        pass

# Same Fizz Buzz Application, but using a Data Dictionary

count = range(101,200)

fizzbuzz_dictionary = {}

for num in count:
    if num % 3 == 0 and num % 5 == 0:
        fizzbuzz_dictionary.update({num:'fizzbuzz'})
    elif num % 3 == 0 and num % 5 != 0:
        fizzbuzz_dictionary.update({num:'fizz'})
    elif num % 3 != 0 and num % 5 == 0:
        fizzbuzz_dictionary.update({num:'buzz'})
    else:
        pass

for key, value in fizzbuzz_dictionary.items():
    print(f'{key} = {value}')