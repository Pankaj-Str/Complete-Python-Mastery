name = input('Enter Employee Name - ')
id = input('Enter Employee ID - ')
salary  = int(input('Enter Employee Salary (Monthly) - '))
leave_days = int(input('Enter Leave (Days) - '))
tds = int(input('TDS % - '))
month = int(input('month - '))
year = int(input('year - '))


print('Employee Name = ',name)
print('Employee ID = ',id)
print('Employee Monthly Salary ',salary)
ctc = salary *12
print('CTC (Yearly Salary ) = ',ctc)
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    day_salary = salary/31
else:        
    day_salary = salary/30
print('Day Salary = ',day_salary)    
leave_amount = leave_days * day_salary 
print('leave Amount = ',leave_amount)    