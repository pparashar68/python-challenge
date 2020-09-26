def Average(list): 
    return sum(list) / len(list) 

import os
import csv

budget_file = os.path.join("Resources/","budget_data.csv")

analysis_output_file = os.path.join("analysis/","analysis_output.txt")
analysis_output = open(analysis_output_file,'w')
with open(budget_file,'r') as budget_file_handler:
    budget_file_row = csv.reader(budget_file_handler,delimiter=',')
    next(budget_file_row)
    total_profit = 0
    cnt = 0
    greatest_increase = 0
    greatest_increase_month = " "
    greatest_decrease = 0
    greatest_decrease_month = " "
    monthly_change = []
    previous_month_pl = 0
    for row in budget_file_row:
        budget_month = row[0]
        monthly_profit = row[1]
        chg = int(monthly_profit) - previous_month_pl
        if  cnt  >0:            # this will skip first month profit data from provided csv as we are calculating the change in profit
            monthly_change.append(chg)
        total_profit = total_profit + int(monthly_profit)
        cnt = cnt + 1
        previous_month_pl = int(monthly_profit)
        if  int(monthly_profit) > greatest_increase:                #To identify the month of highest profit data
            greatest_increase = int(monthly_profit)
            greatest_increase_month = budget_month
        if  int(monthly_profit) < greatest_decrease:                # To identify the month of lowest profit data
            greatest_decrease = int(monthly_profit)
            greatest_decrease_month = budget_month


Average_Change = round( Average(monthly_change),2)
greatest_profit = max(monthly_change)
least_profit = min (monthly_change)
print('Financial Analysis')
analysis_output.write('Financial Analysis \n')
print('-' * 40)
analysis_output.write('-' * 40 )
print(f'\nTotal Months: {cnt}')
analysis_output.write(f'\nTotal Months: {cnt} \n' )
print(f'Total:   ${total_profit} ')
analysis_output.write(f'Total:   ${total_profit} \n')
print(f'Average  Change: ${Average_Change}')
analysis_output.write(f'Average  Change: ${Average_Change} \n')
print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_profit})')
analysis_output.write(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_profit})" \n')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${least_profit})')
analysis_output.write(f'Greatest Decrease in Profits: {greatest_decrease_month} (${least_profit}) \n')