import re

def email_slicer(email):
    # Using regex to extract username, domain, and extension
    match = re.match(r'^(.+)@([^.]+)\.(.+)$', email)
    if match:
        username, domain, extension = match.groups()
        return username, domain, extension
    else:
        return None, None, None

def main():
    print("Welcome to the email slicer\n")

    email_input = input("Input your email address: ")

    username, domain, extension = email_slicer(email_input)

    if username and domain and extension:
        print(f"Username: {username}")
        print(f"Domain: {domain}")
        print(f"Extension: {extension}")
    else:
        print("Invalid email address format.")

if __name__ == "__main__":
    main()
