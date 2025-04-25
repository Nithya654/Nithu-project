from bs4 import BeautifulSoup

filename = "C:/Users/nithy/Downloads/dict.xml"
# Open and read the XML file
with open(filename, 'r') as f:
    data = f.read()

Bs_data = BeautifulSoup(data, "xml")
b_unique = Bs_data.find_all('unique')
print(b_unique)

b_name = Bs_data.find('child', {'name': 'Frank'})
print(b_name)

value = b_name.get('test')
print(value)

#prettify
from bs4 import BeautifulSoup
with open("C:/Users/nithy/Downloads/dict.xml") as f:
    data = f.read()
bs_data = BeautifulSoup(data, 'xml')
for tag in bs_data.find_all('child', {'name':'Frank'}):
    tag['test'] = "WHAT !!"
print(bs_data.prettify())
