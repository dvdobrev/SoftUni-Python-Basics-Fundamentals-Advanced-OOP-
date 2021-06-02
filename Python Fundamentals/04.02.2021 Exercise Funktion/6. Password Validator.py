def if_password_is_valid(p):
    is_valid = True
    digit_count = 0
    if not 6 <= len(p) <= 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")

    if not p.isalnum():
        is_valid = False
        print("Password must consist only of letters and digits")

    for el in p:
        if el.isdigit():
            digit_count += 1

    if digit_count < 2:
        is_valid = False
        print("Password must have at least 2 digits")

    return is_valid


password = input()
result = if_password_is_valid(password)

if result:
    print("Password is valid")