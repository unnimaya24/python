n=int(input("Enter a number "))
if(n>0 and n<=100):
    payAmount=n*0
    fixedcharge=0
elif(n>100 and n<=200):
    payAmount=(100*5)
    fixedcharge=500.00
elif(n>200 and n<=300):
    payAmount=(200*10)
    fixedcharge=2000
else:
    payAmount=0
    
Total= payAmount
print("\nElecticity bill pay=%.2f: " %Total)