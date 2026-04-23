import csv
import math
import sys

REPORT_FILE = 'sample_data.csv'


data = []
# utf-8-sig strips the BOM Excel prepends to UTF-8 CSVs (otherwise it appears in the first column name).
with open(REPORT_FILE, encoding='utf-8-sig', newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #error handling for when selling price < variable costs
        while True:
            raw_selling = row['Selling Price(ZMW)']
            raw_variable = row['Variable Cost per Unit(ZMW)']

            try:
                selling_price = float(raw_selling)
            except ValueError:
                print(f"Error: Invalid Selling Price — '{raw_selling}' is not a valid number.")
                break

            try:
                variable_cost = float(raw_variable)
            except ValueError:
                print(f"Error: Invalid Variable Cost — '{raw_variable}' is not a valid number.")
                break

            if selling_price <= variable_cost:
                print(f"Error: Selling Price ({selling_price}) must be greater than Variable Cost ({variable_cost}). Halting.")
                print("\nCheck sample_data.csv data and try again.")
                sys.exit(1)  # or break, or raise — choose based on your needs

            row['Selling Price(ZMW)'] = selling_price
            row['Variable Cost per Unit(ZMW)'] = variable_cost
            break

        #zero fixed cost handling: note to inform user of break even output.
        fixed_cost = float(row['Fixed Costs Attributable(ZMW)'])
        if fixed_cost == 0:
            print("Note: Fixed costs are zero — break-even is immediate (0 units).")
        else:
            row['Fixed Costs Attributable(ZMW)'] = fixed_cost

        row['Units'] = int(float(row['Units']))

        data.append(row)



for row in data:
    # target profit must be greater than zero, if not, target profit is negative — this implies a planned loss, not a profit target.
    while True:
        try:
            target_profit = float(input('Enter target profit: '))
            if target_profit <= 0:
                raise ValueError("Target profit must be greater than zero.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    row['Contribution per Unit(ZMW)'] = row['Selling Price(ZMW)'] - row['Variable Cost per Unit(ZMW)']
    row['Contribution Ratio'] = (row['Selling Price(ZMW)'] - row['Variable Cost per Unit(ZMW)'])/row['Selling Price(ZMW)']
    row['Break Even(Units)'] = math.ceil(row['Fixed Costs Attributable(ZMW)']/ row['Contribution per Unit(ZMW)'])
    row['Break Even(Revenue)'] = row['Break Even(Units)'] * row['Selling Price(ZMW)']
    row['Margin of Safety(Units)'] = row['Units'] - row['Break Even(Units)']
    row['Margin of Safety(%)'] = ((row['Units'] - row['Break Even(Units)'])/row['Units'])*100
    row['Units to Achieve Target'] = math.ceil((row['Fixed Costs Attributable(ZMW)'] + target_profit)/row['Contribution per Unit(ZMW)'])


print(data)