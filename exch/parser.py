import xml.etree.ElementTree as ET





def proccesing_uploaded_file(xmlfile):
    tree = ET.parse(xmlfile)
    root_xml = tree.getroot()
    for child in root_xml.iter('name'):
        print(child.text)