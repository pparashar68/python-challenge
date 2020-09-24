import os
import csv

budget_file = os.path.join("Resources/","budget_data.csv")
print('Financial Analysis')
print('-' * 40)

with open(budget_file,'r') as budget_file_handler:
    budget_file_row = csv.reader(budget_file_handler,delimiter=',')
    next(budget_file_row)
    total_profit = 0
    cnt = 0
    greatest_increase = 0
    greatest_increase_month = " "
    greatest_decrease = 0
    greatest_decrease_month = " "
    for row in budget_file_row:
        budget_month = row[0]
        monthly_profit = row[1]
        total_profit = float(total_profit) + float(monthly_profit)
        cnt = cnt + 1
        if float(monthly_profit) > float(greatest_increase):
            greatest_increase = float(monthly_profit)
            greatest_increase_month = budget_month
        if float(monthly_profit) < float(greatest_decrease):
            greatest_decrease = float(monthly_profit)
            greatest_decrease_month = budget_month


Average_Change = total_profit / cnt
print(f'Total Months: {cnt}')
print(f'Total:   ${total_profit} ')
print(f'Average  Change: ${Average_Change}')
print(f'Greates Increase in Profits: {greatest_increase_month} (${greatest_increase})')
print(f'Greates Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')
