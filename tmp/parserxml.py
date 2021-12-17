import xml.etree.ElementTree as ET
import sqlite3



def parser(xmlfile):
    tree = ET.parse(xmlfile)
    root_xml = tree.getroot()
    data = []
    print(ET.tostring(root_xml, encoding='utf8').decode('utf8'))
"""     for element in root_xml.iter('еда'):    
        for child in element:
            data = child.attrib
            print(child.tag, child.text)       """
            



if __name__=='__main__':
    parser("import.xml")
  