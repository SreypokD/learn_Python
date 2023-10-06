import xml.etree.ElementTree as ET

# Parse XML from a file
tree = ET.parse('example.xml')
root = tree.getroot()

# Access elements and attributes
print('Root tag:', root.tag)
print('Root attributes:', root.attrib)

# Iterate over child elements
for child in root:
    print('Element:', child.tag)
    print('Text:', child.text)
    print('Attributes:', child.attrib)

# Find elements using XPath
name_elements = root.findall('.//name')
for name_element in name_elements:
    print('Name:', name_element.text)

# Create new XML elements
new_element = ET.Element('new_element')
new_element.text = 'New element content'
root.append(new_element)

# Modify existing elements
for child in root:
    if child.tag == 'name':
        child.text = child.text.upper()

# Write XML to a file
tree.write('output.xml')