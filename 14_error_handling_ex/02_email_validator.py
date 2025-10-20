class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


EMAIL_MIN_LEN = 5
VALID_DOMAINS = (".com", ".bg", ".net", ".org")


while True:
    email = input()

    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    name = email.split("@")[0]
    if len(name) < EMAIL_MIN_LEN:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = "." + email.split(".")[-1]
    if domain not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
