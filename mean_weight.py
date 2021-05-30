import csv 

with open('Height-weight.csv',newline = '')as f:
    reader=csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))

#getting the mean
n=len(new_data)
total = 0
for x in new_data:
    total += x
mean = total/n
print("the mean is : "+str(mean))