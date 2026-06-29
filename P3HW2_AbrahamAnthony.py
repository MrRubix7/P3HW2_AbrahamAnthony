 # Your Name: Antony Abraham
 # Date: 29 JUNE 2026
 # Assignment Name: P3HW2
 # A brief description of the project: Calculates pay based on regular and overtime hours worked and prints a final tabular report.

#Instructions

#You are to create a program that does the following: 
#Asks the user to enter name of employee
#Ask user to enter number of hours the employee worked this week
#Ask user to enter employee's pay rate
#Evaluate if employee has worked overtime (more than 40 hours). If yes, calculate the amount owed to employee for overtime hours
#The employee should receive 1.5 times their normal pay rate for any overtime hours worked.
#Calculate amount employee should be paid for regular hours worked.
#Display gross pay (total amount that should be paid to employee)
#The program is to display the following (Employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours and gross pay).
#Once finished, submit the finished code file through the assignment link in this folder.


#Asks the user to enter name of employee and assign this input to the employee variable
employee = input("\nEnter employee's name: ") 

#Ask user to enter number of hours the employee worked this week and assign this value to the hours variable
hours = float(input("Enter number of hours worked: ")) 

#Ask user to enter employee's pay rate and assign this value to the pay_rate variable
pay_rate = float(input("Enter employee's pay rate: "))

# create tabular divider
sym = '-'
line = sym * 50
footer = sym * 37

print(sym * 50)
print(f'{"Employee name: ":<15}{employee}\n')

print(f'{"Hours Worked":<20}{"Pay Rate":<20}{"OverTime":<20}{"OverTime Pay":<20}{"RegHour Pay":<20}{"Gross Pay":<20}') 
print(sym * 125)

#The employee should receive 1.5 times their normal pay rate for any overtime hours worked.
overtime_rate = float(pay_rate * 1.5)

#Evaluate if employee has worked overtime (more than 40 hours). If yes, calculate the amount owed to employee for overtime hours

if hours > 40:
    overtime = hours - 40
    regHour = hours - overtime
    
    #calculate pay
    overtime_pay = overtime * overtime_rate
    reg_pay = regHour * pay_rate #Calculate amount employee should be paid for regular hours worked.
    
    #Display gross pay (total amount that should be paid to employee)
    #The program is to display the following (Employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours and gross pay).
    print(f'{hours:<20}{pay_rate:<20}{overtime:<20}{"$"}{overtime_pay:<20.2f}{"$"}{reg_pay:<20.2f}{"$"}{overtime_pay + reg_pay:<20.2f}\n') 

else: 
    overtime = 0
    reg_pay = hours * pay_rate #Calculate amount employee should be paid for regular hours worked.
    overtime_pay = 0

    #Display gross pay (total amount that should be paid to employee)
    #The program is to display the following (Employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours and gross pay).
    print(f'{hours:<20}{pay_rate:<20}{overtime:<20}{"$"}{overtime_pay:<20.2f}{"$"}{reg_pay:<20.2f}{"$"}{overtime_pay + reg_pay:<20.2f}\n')