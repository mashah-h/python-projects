#MPESA Withdrawal Charges
#If amount ≤ KSh 1,000, charge KSh 10.
#If 1,001 - 5,000, charge KSh 30.
#If 5,001 - 10,000, charge KSh 50.
#If >10,000, charge KSh 100.
#If agent withdrawal, add KSh 5 service fee.

def withdrawal_charge(amount,agent_withdrawal):
    if agent_withdrawal:
        if amount <=1000:
            charge =  10
        elif amount <=5000 and amount>1000:
            charge = 30
        elif amount>5000 and amount <10000:
            charge = 50
        elif amount > 10000:
            charge = 100
        charge +=5
            
    else:
        if amount <=1000:
            charge =  10
        elif amount <=5000 and amount>1000:
            charge = 30
        elif amount>5000 and amount <10000:
            charge = 50
        elif amount > 10000:
            charge = 100
    return f"Withdrawal charge: Ksh {int(charge)}"        
print(withdrawal_charge(15000, False))

            
            
        
        