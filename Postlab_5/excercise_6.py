def count_vowels(word):
    vowels = "AaEeIiOoUu"
    count = 0

    for letter in word:
        if letter in vowels:
            count += 1
    return count