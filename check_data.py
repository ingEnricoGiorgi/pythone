from datetime import datetime
# Shift + Alt + F  default formatter

data = input("Enter a date: ")
countData=0
countData = (data.count(" ") == 2 or data.count("/") == 2 or data.count("-") == 2)
if(countData>0):
    pulito = data.replace(" ", "").replace("/", "").replace("-", "")
    data_time = datetime.strptime(pulito, "%d%m%Y")
    print(data_time)