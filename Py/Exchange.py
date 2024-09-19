print("===============================")
print("Welcome to $$ EXCHANGE STORE $$")
print("===============================\n")
a=input("Exchange from (USD ,EUR, SAR): ").upper()
b=float(input("How Much? "))
c=input("Exchange to (USD, EUR, SAR): ").upper()
USDtoEUR=float(round((b*0.99)))
USDtoSAR=float(round((b*3.75)))
EURtoUSD=float(round(b/0.99))
SARtoUSD=float(round(b/3.75))
EURtoSAR=float(round((b/0.99)*3.75))
SARtoEUR=float(round((b/3.75)*0.99))
if a==c:
    print("Please enter another currency! ")
    exit()
elif a=="SAR" and c=="USD":
    print(f"You will give {b} SAR and will take {SARtoUSD} USD")
elif a=="SAR" and c=="EUR":
    print(f"You will give {b} SAR and will take {SARtoEUR} EUR")
elif a=="USD" and c=="SAR":
    print(f"You will give {b} USD and will take {USDtoSAR} SAR")
elif a=="USD" and c=="EUR":
    print(f"You will give {b} USD and will take {USDtoEUR} EUR")
elif a=="EUR" and c=="USD":
    print(f"You will give {b} EUR and will take {EURtoUSD} USD")
elif a=="EUR" and c=="SAR":
    print(f"You will give {b} EUR and will take {EURtoSAR} SAR")
else:
    print("Please enter vaile currency")