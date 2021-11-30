"""
The US federal personal income tax is calculated based
on the filing status and taxable income. There are four
filing statuses: single filers, married filing jointly, married
filing separately, and head of household. The tax rates
for 2009 are shown below.
"""
status = int(input("\nPlease enter your filing status:\n\
                      [1] for single,\n\
                      [2] for married filing jointly or qualifying widow(er),\n\
                      [3] for married filing separately, \n\
                      [4] for head of household\n"))
1
income = int(input("Please enter your taxable income\n"))

if (status == 1 or status == 3) and ((income > 0) and (income <= 8350)):
    print(f"Your tax rate is 10% and tax amount is {income * (10 / 100)}.")
elif (status == 1 or status == 3) and ((income > 8350) and (income <=33950)):
    print(f"Your tax rate is 15% and tax amount is {income * (15 / 100)}.")
elif (status == 1) and ((income > 33950) and (income <= 82250)):
    print(f"Your tax rate is 25% and tax amount is {income * (25 / 100)}.")
elif (status == 1) and ((income > 82250) and (income <= 171550)):
    print(f"Your tax rate is 28% and tax amount is {income * (28 / 100)}.")
elif (status == 1) and ((income >=171551) and (income <=372950)):
    print(f"Your tax rate is 33% and tax amount is {income * (33 / 100)}.")
elif (status == 1) and (income >=372951):
    print(f"Your tax rate is 35% and tax amount is {income * (35 / 100)}.")

elif (status == 3) and ((income > 33950) and (income <= 68525)):
    print(f"Your tax rate is 25% and tax amount is {income * (25 / 100)}.")
elif (status == 1) and ((income > 68525) and (income <= 104425)):
    print(f"Your tax rate is 28% and tax amount is {income * (28 / 100)}.")
elif (status == 1) and ((income >= 104426) and (income <= 186475)):
    print(f"Your tax rate is 33% and tax amount is {income * (33 / 100)}.")
elif (status == 1) and (income > 186475):
    print(f"Your tax rate is 35% and tax amount is {income * (35 / 100)}.")


elif (status == 2) and ((income > 0) and (income <= 16700)):
    print(f"Your tax rate is 10% and tax amount is {income * (10 / 100)}.")
elif (status == 2) and ((income >=16701) and (income <=67900)):
    print(f"Your tax rate is 15% and tax amount is {income * (15 / 100)}.")
elif (status == 2) and ((income >=67901) and (income <=137050)):
    print(f"Your tax rate is 25% and tax amount is {income * (25 / 100)}.")
elif (status == 2) and ((income >=137051) and (income <=208850)):
    print(f"Your tax rate is 28% and tax amount is {income * (28 / 100)}.")
elif (status == 2) and ((income >=208851) and (income <=372950)):
    print(f"Your tax rate is 33% and tax amount is {income * (33 / 100)}.")
elif (status == 2) and (income >=372951):
    print(f"Your tax rate is 35% and tax amount is {income * (35 / 100)}.")

elif (status == 4) and ((income >=0) and (income <=11950)):
    print(f"Your tax rate is 10% and tax amount is {income * (10 / 100)}.")
elif (status == 4) and ((income >=11951) and (income <=45500)):
    print(f"Your tax rate is 15% and tax amount is {income * (15 / 100)}.")
elif (status == 4) and ((income >=45501) and (income <=117450)):
    print(f"Your tax rate is 25% and tax amount is {income * (25 / 100)}.")
elif (status == 4) and ((income >=117451) and (income <=190200)):
    print(f"Your tax rate is 28% and tax amount is {income * (28 / 100)}.")
elif (status == 4) and ((income >=190201) and (income <=372950)):
    print(f"Your tax rate is 33% and tax amount is {income * (33 / 100)}.")
elif (status == 4) and (income >=372951):
    print(f"Your tax rate is 35% and tax amount is {income * (35 / 100)}.")
