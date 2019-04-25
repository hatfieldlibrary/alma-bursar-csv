import xml.etree.ElementTree as ET
import csv
import formatter

tree = ET.parse("small-charges-2019.xml")
root = tree.getroot()

ns = { 'xb': 'http://com/exlibris/urm/rep/externalsysfinesfees/xmlbeans'}

# open a file for writing

with open('charges.csv', mode='w') as breaklist_data:
	breaklist_data_writer = csv.writer(breaklist_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	for fine_list in root.findall('.//xb:userExportedFineFeesList', ns):

                user = fine_list.find('xb:user', ns)
                user_id = user.find('xb:value', ns)
                fee_list = fine_list.find('xb:finefeeList', ns)
                patron_name = fine_list.find('xb:patronName', ns)
                user_fine = fee_list.findall('xb:userFineFee', ns) 
                for fine in user_fine:
                     composite = fine.find('xb:compositeSum', ns)
                     total_due = composite.find('xb:sum', ns)
                     breaklist_data_writer.writerow([patron_name.text,user_id.text,total_due.text])




