# Conditional Execution

hrs=float(input("enter hours:"))
rate=float(input("enter rate:"))
if  hrs>40:
    rate1=((rate*1.5)*(hrs-40))
pay=((hrs-5)*rate) + rate1
print(pay)
        
