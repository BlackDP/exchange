import xml.etree.ElementTree as ET
import sqlite3








def parser(xmlfile):
    tree = ET.parse(xmlfile)
    root_xml = tree.getroot()
    data = []
    for element in root_xml.iter('Группы'):    
        for child in element:
            data = child.attrib
            print(child.tag, child.text)      
            

    





if __name__=='__main__':
    parser("import0_1.xml")
  