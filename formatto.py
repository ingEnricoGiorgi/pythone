#formatto.py

reciprociList=[]
number = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(number)):
    reciprociList.append(round(float(1 / number[i]),8))
print(reciprociList)