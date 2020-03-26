import xml.etree.ElementTree as ET
data='''
    <person>
        <name>
            Kedar
        </name>
        <phone>
            7249195345
        </phone>
        <email hide="yes">
    </person>'''
tree = ET.parse(data)
root = tree.getroot()
