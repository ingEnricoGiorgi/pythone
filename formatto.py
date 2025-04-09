#formatto.py

reciprociList=[]
number = 11
for i in range(number):
    #reciprociList.append(round(float(1 / number[i]),8))
    reciproco = 1 / (i+1)
    reciprociList.append(f"{reciproco:10.8f}")
print(reciprociList)