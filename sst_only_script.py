import matplotlib.pyplot as plt
import numpy as np

count1 = []
minimum1 = []
maximum1 = []
mean1 = []
f = open("SST_Min_Max_Mean_Data_For_Each_Day", "r")
lines = f.readlines()
lc = 0 #line count
for line in lines:
    lc += 1
    token = line.split(" ") #split the line according to spaces, and make a token value that is a list of all parts split by a space for each line
    if (len(token) == 0):
        continue
    count1.append((lc / 365) + 1988) #lc is the count for the graph
    minimum1.append(token[1]) #token[1] = min
    maximum1.append(token[2]) #token[2] = max
    mean1.append(float(token[3].strip())) #Mean has to treated as a number, hence the float(), and strip() is used to get rid of \ns after the token
f.close()
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
plt.plot(count1, mean1, color = 'blue')
plt.xlabel('Years', fontsize = 23)
plt.ylabel('Sea Surface Temperature Annual Mean', fontsize = 23)
plt.title('Sea Surface Temperature Means of each year', fontsize = 23)
plt.show()
