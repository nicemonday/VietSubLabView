import xml.etree.ElementTree as ET 

class MyXML():
    def __init__(self, path):
        self.file = path
        self.tree = ET.parse(self.file)
        self.root = self.tree.getroot()
        self.elems = []

    def GetAllElementByTag(self, tag):
        for elem in self.tree.iter():
            if elem.tag == tag:
                self.elems.append([elem, elem.text, ""])

    def Save(self):
        self.tree.write(self.file, encoding="utf-8", xml_declaration=None, default_namespace=None, method="xml")
    
