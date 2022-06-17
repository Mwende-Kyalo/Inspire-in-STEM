import requests
from bs4 import BeautifulSoup as bs

#input("Enter your user name :")
user_name = "Mwende-Kyalo"
#input("Enter site Url :")
url ="https://github.com/" + user_name
results=requests.get(url)

soup = bs(results.content, "html.parser")
profile_picture = soup.find('img',{'alt':'Avatar'})['src']
print(profile_picture)