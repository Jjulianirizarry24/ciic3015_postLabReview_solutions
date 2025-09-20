def plusOne(digits):
    if not digits.isdigit():
        return "Invalid argument"
    num = int(digits)
    num += 1
    return str(num)