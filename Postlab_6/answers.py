import math

# Escape sequences for colors
GREEN = "\033[92m"
RESET = "\033[0m"


# Laboratoy 6: Loops Part II

# Problem 1: Count the Vowels
def num_vowels(s):
    res = 0
    for c in s:
        if c.lower() in 'aeiou':
            res += 1
    return res


    return 
# Test cases:
print(f"{GREEN}Problem 1 tests{RESET}")
print(f"Input: '' | Expected: 0 | Found: {num_vowels('')}")
print(f"Input: 'spam spam spam' | Expected: 3 | Found: {num_vowels('spam spam spam')}")
print(f"Input: 'SpAm EgG sAuSaGe AnD sPaM' | Expected: 8 | Found: {num_vowels('SpAm EgG sAuSaGe AnD sPaM')}")


# Problem 2: Is Prime
def is_prime(n):
    i = 2
    while i <  math.ceil(math.sqrt(n)) and n % i != 0:
        i+=1
    return n % i != 0
# Test cases:
print(f"{GREEN}Problem 2 tests{RESET}")
print(f"Input: 5 | Expected: True | Found: {is_prime(5)}")
print(f"Input: 10 | Expected: False | Found: {is_prime(10)}")
print(f"Input: 13 | Expected: True | Found: {is_prime(13)}")


# Problem 3: FizzBuzz
def fizz_buzz(N):
    i = 1
    res = ""
    while i < N + 1:
        if i % 3 == 0 and i % 5 == 0:
            res += "fizz_buzz"
        elif i % 3 == 0:
            res += "Fizz"
        elif i % 5 == 0:
            res += "Buzz"
        else:
            res += str(i)
        res += " "
        i += 1  
    return res

# Test cases:
print(f"{GREEN}Problem 3 tests{RESET}")
print(f"Input: 5 | Expected: '1 2 Fizz 4 Buzz' | Found: '{fizz_buzz(5)}'")
print(f"Input: 30 | Expected: '1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 fizz_buzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 fizz_buzz' | Found: '{fizz_buzz(30)}'")
print(f"Input: 1 | Expected: '1' | Found: '{fizz_buzz(1)}'")

# Problem 4: Replace all Letters
def replace_all_letters(text, letter, substitute):
    result = ''
    for char in text:
        if char == letter:
            result += substitute
        else:
            result += char
    return result
#test cases:
print(f"{GREEN}Problem 4 tests{RESET}")
print(replace_all_letters("Mas sabe el diablo por viejo que por diablo", " ", "_")) # Mas_sabe_el_diablo_por_viejo_que_por_diablo
print(replace_all_letters("Mas sabe el diablo por viejo que por diablo", "d", "D")) # Mas sabe el Diablo por viejo que por Diablo

# Problem 5: Factorial Calculator
def factorial(number):
    result = 1
    i = 1
    while i <= number:
        result *= i 
        i += 1
    return result
    
#test cases:
print(f"{GREEN}Problem 5 tests{RESET}")
print("Expected: 120, Got:", factorial(5))
print("Expected: 1, Got:", factorial(1))

# Problem 6: Binary to Decimal
def toDecimal(binary):
    decimal = 0
    total_bits = len(binary)
    
    for n in range(total_bits):
        if binary[n] == '1':
            decimal += 2 ** (total_bits -n - 1)
  
    return decimal
# Test Cases:
print(f"{GREEN}Problem 6 tests{RESET}")
print(f"Input: '00010011' | Expected: 19 | Found: {toDecimal('00010011')}")
print(f"Input: '01110011' | Expected: 115 | Found: {toDecimal('01110011')}")
print(f"Input: '00011010' | Expected: 26 | Found: {toDecimal('00011010')}")

# Bonus:
def product_of_digits_greater_than_position(N):
    product = 1
    found = False
    i = len(N)
    while i > 0:
        curr = int(N[len(N) - i])
        if i < curr:
            product *= curr 
            found = True
        i -= 1
    if found:
        return product
    return -1
# Test cases:
print(f"{GREEN}Bonus{RESET}")
print(f"Input: '348' | Expected: 32 | Found: {product_of_digits_greater_than_position('348')}")
print(f"Input: '45335' | Expected: 75 | Found: {product_of_digits_greater_than_position('45335')}")
print(f"Input: '321' | Expected: -1 | Found: {product_of_digits_greater_than_position('321')}")
