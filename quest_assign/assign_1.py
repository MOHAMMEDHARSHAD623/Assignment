n = int(input('Enter the number of employees: '))

while n < 4 :
    print('Please enter at least 4 employees ')
    n = int(input(' check the number of employees(minimum 4): '))

total_gross = 0
total_deduction = 0
total_net = 0

for i in range(n):
    print('\n Enter employee',i + 1 ,'Details')

    name = input('Enter the employee name: ')
    employee_id = input('Enter employee id: ')

    while True :
        basic = float(input('Basic salary: '))
        if basic < 0 :
            print('the salary shouldn,t be negative. Enter again!!...')
        else:
            break

    hra = basic *20/100
    travel = basic *5/100

    gross = basic + hra + travel

    pf = basic *8/100
    tax = gross *5/100
    
    deduction = pf + tax 

    net =  gross - deduction


    print('\n----SALARY DETAILS----')

    print("Employee Name      :", name)
    print("Employee ID        :", employee_id)

    print("------------------------------------")

    print("Basic Salary       : Rs.", format(basic, ".2f"))
    print("HRA (20%)          : Rs.", format(hra, ".2f"))
    print("Travel Allowance   : Rs.", format(travel, ".2f"))

    print("------------------------------------")

    print("Gross Salary       : Rs.", format(gross, ".2f"))

    print("------------------------------------")

    print("PF Deduction       : Rs.", format(pf, ".2f"))
    print("Tax Deduction      : Rs.", format(tax, ".2f"))
    print("Total Deductions   : Rs.", format(deduction, ".2f"))

    print("------------------------------------")

    print("Net Salary         : Rs.", format(net, ".2f"))

    print("====================================")


    total_gross = total_gross + gross
    total_deduction = total_deduction + deduction
    total_net = total_net + net

print("\n========== PAYROLL SUMMARY ==========")

print("Total Employees    :", n)
print("Total Gross Payroll: Rs.", format(total_gross, ".2f"))
print("Total Deductions   : Rs.", format(total_deduction, ".2f"))
print("Total Net Payroll  : Rs.", format(total_net, ".2f"))

print("=====================================")