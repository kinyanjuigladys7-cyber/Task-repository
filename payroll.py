EmployeeID=input("Enter EmployeeID:")
EmployeeName=input("Enter Employee name:")
BasicSalary=float(input("Enter BasicSalary:"))
Allowances=float(input("Enter Allowances:"))
Deductions=float(input("Enter Deductions:"))
GrossSalary=BasicSalary+Allowances
TaxAmount=GrossSalary*10/100
NetSalary=GrossSalary-Deductions-TaxAmount
print("/n payslip")
print("EmployeeId:",EmployeeID)
print("EmployeeName:",EmployeeName)
print("BasicSalary:",BasicSalary)
print("Allowances:",Allowances)
print("Deductions:",Deductions)
print("NetSalary:",NetSalary)
print("TaxAmount:",TaxAmount)
print("GrossSalary:",GrossSalary)



