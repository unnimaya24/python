units=int(input("Enter a number "))
if(units>0 and units<=100):
    payAmount=units*0
    fixedcharge=0
elif(units>=100 and units<=200):
    payAmount=(100*0)+(units-0)*5
    fixedcharge=500

elif(units>=200 and units<=300):
    payAmount=(100*0)+(units-100)*10
    fixedcharge=2000

else:
    payAmount=0
    fixedcharge=2500

Total=payAmount+fixedcharge;
print("\nElecticity bill=%.2f" %Total)