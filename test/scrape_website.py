import urllib.request
from bs4 import BeautifulSoup

word = input('Enter the word to find the meaning : ')

url = "https://www.dictionary.com/browse/" + word + ""
htmlfile = urllib.request.urlopen(url)
soup = BeautifulSoup(htmlfile, 'html.parser')
s1 = soup.find(class_='css-1o58fj8 e1hk9ate4')
print(s1.get_text())
#
# soup1 = soup.find(class_="short")
#
# try:
#     soup1 = soup1.get_text()
# except AttributeError:
#     print('Cannot find such word! Check spelling.')
#     exit()
#
# # Print short meaning
# print ('-' * 25 + '->',word,"<-" + "-" * 25)
# print ("SHORT MEANING: \n\n",soup1)
# print ('-' * 65)
#
# ''
#
# # Print long meaning
# soup2 = soup.find(class_="long")
# soup2 = soup2.get_text()
# print ("LONG MEANING: \n\n",soup2)
#
# print ('-' * 65)
#
# # Print instances like Synonyms, Antonyms, etc.
# soup3 = soup.find(class_="instances")
# txt = soup3.get_text()
# txt1 = txt.rstrip()
#
# print (' '.join(txt1.split()))
