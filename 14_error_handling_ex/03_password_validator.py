class PasswordTooShortError(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass


class PasswordContainsSpacesError(Exception):
    pass


def password_too_common(passw: str, special_chars: tuple) -> bool:
    only_digits = passw.isdigit()
    only_letters = passw.isalpha()
    only_specials = all(ch in special_chars for ch in passw)
    return only_digits or only_letters or only_specials


PASS_MIN_LEN = 8
SPECIAL_CHARS = ("@", "*", "&", "%")


while True:
    password = input()

    if password == "Done":
        break

    if len(password) < PASS_MIN_LEN:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if password_too_common(password, SPECIAL_CHARS):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not any(ch in SPECIAL_CHARS for ch in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    print("Password is valid")
