
import os
import csv



file_csv = os.path.join("budget_data.csv")


exportfile = "finanalysis.txt"


profit_loss = []
monthly_chng = []
month_count = []

# Initialize the variables 
total_months = 0
first_profit = 0
total_profit = 0
tot_chng_profit = 0


# Open the CSV using the set path 

with open(file_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

    for row in csv_reader:    
      total_months = total_months + 1 
      profit_loss.append(row[1])
      total_profit = total_profit + int(row[1])
      final_profit = int(row[1])
      monthly_chng_profit = final_profit - first_profit
      monthly_chng.append(monthly_chng_profit)
      
      
      tot_chng_profit = tot_chng_profit + monthly_chng_profit
      first_profit = final_profit
      avg_change_profit = (tot_chng_profit/total_months)
      month_count.append(row[0])      
      
      
      maxprofit = max(monthly_chng)
      minprofit = min(monthly_chng)
      maxprofitdate = month_count[monthly_chng.index(maxprofit)]
      minprofitdate = month_count[monthly_chng.index(minprofit)]
    

    print (f"Financial Analysis")
    print (f"--------------------")
    print (f"Total Months: ", total_months)
    print (f"Total Profits: $",total_profit)
    print (f"Average Change: $ ", avg_change_profit)
    print (f"Greatest Increase in Profits: ", maxprofitdate, "$", maxprofit)
    print (f"Greatest Decrease in Profits: ", minprofitdate, "$", minprofit)
#Export results to new file
with open(exportfile, 'w') as file:
    file.write("Financial Analysis\n"
    f"--------------------\n"
    f"Total Months:{total_months}\n"
    f"Total Profits: ${total_profit}\n"
    f"Average Change: ${avg_change_profit}\n"
    f"Greatest Increase in Profits:{maxprofitdate}${maxprofit}\n"
    f"Greatest Decrease in Profits:{minprofitdate}${minprofit}")
    file.close()

