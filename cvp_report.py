import csv
import math

REPORT_FILE = 'sample_data.csv'
target_profit = float(input('Enter target profit: '))

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



for row in data:
    row['Contribution per Unit(ZMW)'] = row['Selling Price(ZMW)'] - row['Variable Cost per Unit(ZMW)']
    row['Contribution Ratio'] = (row['Selling Price(ZMW)'] - row['Variable Cost per Unit(ZMW)'])/row['Selling Price(ZMW)']
    row['Break Even(Units)'] = math.ceil(row['Fixed Costs Attributable(ZMW)']/ row['Contribution per Unit(ZMW)'])
    row['Break Even(Revenue)'] = row['Fixed Costs Attributable(ZMW)'] / row['Contribution Ratio']
    row['Margin of Safety(Units)'] = math.ceil(row['Units'] - row['Break Even(Units)'])
    row['Margin of Safety(%)'] = round(((row['Units'] - row['Break Even(Units)'])/row['Units'])*100,2)
    row['Units to Achieve Target'] = math.ceil((row['Fixed Costs Attributable(ZMW)'] + target_profit)/row['Contribution per Unit(ZMW)'])


print(data)