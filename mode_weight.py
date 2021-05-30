import csv 
from collections import Counter

with open('Height-weight.csv',newline = '')as f:
    reader=csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))

#calculating mode

data = Counter(new_data)
mode_data_for_range={
    "75-85":0,
    "85-95":0,
    "95-105":0,
    "105-115":0,
    "115-125":0,
    "125-135":0,
    "135-145":0,
    "145-155":0,
    "155-165":0,
    "165-175":0


}
for height,occourence in data.items():
    if 75<float (height)<85:
        mode_data_for_range["75-85"]+= occourence 

    elif 85<float(height)<95:
        mode_data_for_range["85-95"]+= occourence 
    elif 95<float(height)<105:
        mode_data_for_range["95-105"]+= occourence
    elif 105<float(height)<115:
        mode_data_for_range["105-115"]+= occourence 
    elif 115<float(height)<125:
        mode_data_for_range["115-125"]+= occourence 
    elif 125<float(height)<135:
        mode_data_for_range["125-135"]+= occourence 
    elif 135<float(height)<145:
        mode_data_for_range["135-145"]+= occourence 
    elif 145<float(height)<155:
        mode_data_for_range["145-155"]+= occourence 
    elif 155<float(height)<165:
        mode_data_for_range["155-165"]+= occourence 
    elif 165<float(height)<175:
        mode_data_for_range["165-175"]+= occourence 



mode_range,mode_occourence = 0,0
for range,occourence in  mode_data_for_range.items():
    if occourence>mode_occourence   :
        mode_range,mode_occourence=[int(range.split("-")[0]),int(range.split("-")[1])],occourence
mode = float((mode_range[0]+mode_range[1])/2)
print("mode is : "+str(mode))

