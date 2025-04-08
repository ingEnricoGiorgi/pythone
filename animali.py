#animali

isPet=False
nItems = 0
prices=[]
temp=[]
inputPrice=input("Digita prezzi: ")
while inputPrice !="-1":
      if "Y" in inputPrice:
        isPet=True
      prices.append(float(inputPrice[0:inputPrice.find(" ")]))
      nItems+=1
      inputPrice=input("Digita prezzi: ")

def discount(prices, nItems):
    sconto=0
    if(nItems>5):
        sconto=0.20*sum(prices)
    return sconto 

if  nItems>6 and isPet:
    sconto= discount(prices, nItems)        
    print("lo sconto e:", sconto, nItems)
else:
    print("non hai diritto a sconto")
    
