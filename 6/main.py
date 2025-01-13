def has_digit(password):
    return any(letter.isdigit() for letter in password)


def is_very_long(password):
    return len(password) > 12


def has_lower_letters(password):
    return any(letter.islower() for letter in password)


def has_upper_letters(password):
    return any(letter.isupper() for letter in password)


def has_symbols(password):
    return any(not letter.isalnum() for letter in password)


def main():
    password = input("Введите пароль: ")
    functions = [
        has_digit,
        is_very_long,
        has_lower_letters,
        has_upper_letters,
        has_symbols,
    ]
    score = 0
    for function in functions:
        result = function(password)
        if result:
            score = score + 2
    print("Рейтинг пароля:", score)


if __name__ == "__main__":
    main()
