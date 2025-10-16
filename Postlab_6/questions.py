import math

# Laboratoy 6: Loops Part II

# Problem 1: Count the Vowels
def num_vowels(s):
    # Your code here
    return -1 # Dummy Return
# Test cases:
print("Problem 1 tests:")
print(f"Input: '' | Expected: 0 | Found: {num_vowels('')}")
print(f"Input: 'spam spam spam' | Expected: 3 | Found: {num_vowels('spam spam spam')}")
print(f"Input: 'SpAm EgG sAuSaGe AnD sPaM' | Expected: 8 | Found: {num_vowels('SpAm EgG sAuSaGe AnD sPaM')}")


# Problem 2: Is Prime
def is_prime(n):
    # Your code here  
    return True # Dummy Return
# Test cases:
print("Problem 2 tests:")
print(f"Input: 5 | Expected: True | Found: {is_prime(5)}")
print(f"Input: 10 | Expected: False | Found: {is_prime(10)}")
print(f"Input: 13 | Expected: True | Found: {is_prime(13)}")


# Problem 3: FizzBuzz
def fizz_buzz(n):
    # Your code here
    return -1 # Dummy Return
# Test cases:
print("Problem 3 tests:")
print(f"Input: 5 | Expected: '1 2 Fizz 4 Buzz' | Found: '{fizz_buzz(5)}'")
print(f"Input: 30 | Expected: '1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 fizz_buzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 fizz_buzz' | Found: '{fizz_buzz(30)}'")
print(f"Input: 1 | Expected: '1' | Found: '{fizz_buzz(1)}'")

# Problem 4: Binary to Decimal
def toDecimal(binary):
    # TODO: Your code HERE
    return 0

# Test Cases:
print(f"Input: '00010011' | Expected: 19 | Found: {toDecimal('00010011')}")
print(f"Input: '01110011' | Expected: 115 | Found: {toDecimal('01110011')}")
print(f"Input: '00011010' | Expected: 26 | Found: {toDecimal('00011010')}")

# Problem 5: Replace all Letters
def replace_all_letters(text, letter, substitute):
    return ''
    
#test cases:
print(replace_all_letters("Mas sabe el diablo por viejo que por diablo", " ", "_")) # Mas_sabe_el_diablo_por_viejo_que_por_diablo
print(replace_all_letters("Mas sabe el diablo por viejo que por diablo", "d", "D")) # Mas sabe el Diablo por viejo que por Diablo

# Problem 6: Factorial Calculator
def factorial(number):
    # TODO: Your code HERE
    return 1

#test cases:
print("Expected: 120, Got:", factorial(5))
print("Expected: 1, Got:", factorial(1))

# Bonus:
def product_of_digits_greater_than_position(n):
    # Your code here
    return -1 # Dummy return
# Test cases:
print("Bonus tests:")
print(f"Input: '348' | Expected: 32 | Found: {product_of_digits_greater_than_position('348')}")
print(f"Input: '45335' | Expected: 75 | Found: {product_of_digits_greater_than_position('45335')}")
print(f"Input: '321' | Expected: -1 | Found: {product_of_digits_greater_than_position('321')}")

