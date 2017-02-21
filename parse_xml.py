import xml.etree.ElementTree as ET
import pprint

tree = ET.parse("exampleResearchArticle.xml")
root = tree.getroot()

print("\nChildren of root:")
for child in root:
    print(child.tag)

title = root.find('./fm/bibl/title') #support basic x path expression
title_text = ''
for p in title:
    title_text += p.text
print("\nTitle:\n",title_text)

print("\nAuthor email addresses:")
for a in root.findall('./fm/bibl/aug/au'):
    email = a.find('email')
    if email is not None:
        print(email.text)




