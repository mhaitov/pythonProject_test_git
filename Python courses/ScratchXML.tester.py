from xml.entree import ElementTree

tree = ElementTree.parse('xml_files/cd_catalog.xml')
# print(tree)
#
root = tree.getroot()
#
# print(root.tag, root.attrib)
#
# for element in root.iter('SELLS'):
#     sold_albums = 0
#     for year in element:
#         sold_albums += int(year.text)
#         print(type(year.text))

cd = root[0]
data = next(cd.iter('Y1985'))
print(data.next)

data.text = str(int(data.text) + 50000)

total_sold = ElementTree.Element('TOTAL')
total_sold.text = '200000'

cd.append(total_sold)

title = cd.find('TITLE')
cd.remove(title)

tree.write('xml_files/axml_copy.xml')

