import csv

REPORT_FILE = 'sample_data.csv'

data = []
# utf-8-sig strips the BOM Excel prepends to UTF-8 CSVs (otherwise it appears in the first column name).
with open(REPORT_FILE, encoding='utf-8-sig', newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row['Selling Price(ZMW)'] = float(row['Selling Price(ZMW)'])
        row['Variable Cost per Unit(ZMW)'] = float(row['Variable Cost per Unit(ZMW)'])
        row['Fixed Costs Attributable(ZMW)'] = float(row['Fixed Costs Attributable(ZMW)'])
        row['Units'] = int(float(row['Units']))

        data.append(row)

print(data)