#site connectivity checker 


#we'll us urllib.request to get the data from the website 
# define a function that takes a URL and returns a response 

import urllib.request as urllib



def main(url):
    print("Checking connectivity \n")

    response = urllib.urlopen(url)
    print(f"Connected to {url} successfully")
    print(f"The response code was: {response.getcode()}")

print("This is a site connectivity checker program \n")
input_url = input("Kindly input the URL of the site you want to check: ")

main(input_url)


