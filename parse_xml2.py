
# extract data from xml on authors of an article and add it to a list, one item for an author.

import xml.etree.ElementTree as ET

article_file = "exampleResearchArticle.xml"


def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()

def get_author(root):
    authors = []
    for author in root.findall('./fm/bibl/aug/au'):
        data = { "fnm": None, "snm": None,"email": None,"insr": []}
        data["fnm"] = author.find('./fnm').text
        data["snm"] = author.find('./snm').text
        data["email"] = author.find('./email').text
        insr = author.findall('./insr')
        for i in insr:
            data["insr"].append(i.attrib["iid"])

        authors.append(data)

    return authors

