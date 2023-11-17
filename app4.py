# Email Slicer 

# It takes an email and slices it into the username, domain and extension
#Steps 

#collect email from user 
#slice or split the email using regex (split at the @)
#further split the domain into 2 parts on the . 

def main():
    print("Welcome to the email slicer" + "\n")

    email_input = input("Input your email address: ")

    (username,domain) = email_input.split("@")
    (domain, extension) = domain.split(".")
    print(f"username is {username}")
    print(f"domain is {domain}")
    print(f"extension is {extension}")
while True:
    main()
