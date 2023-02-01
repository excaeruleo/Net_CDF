import matplotlib.pyplot as plt
import numpy as np

count = [] #will contain count of total days of all 34 years from 1988-2021
minimum = [] #will contain all minimum sea surface temperature values
maximum = [] #will contain all maximum sea surface temperature values
mean = [] #will contain all mean sea surface temperature values
f = open("Air_Temp_Min_Max_Mean_Data_For_Each_Year", "r") #Opens text file containing min, max, and average sea surface temperature of each day in each year from 1988 to 2021
lines = f.readlines() #Reads every single line contained in f
#lines.split(' ') #Split each line via the spaces between the values and then place into a list, with each part separated by a space becoming an element
lc = 0 #line count
for line in lines:
    lc += 1
    #print(line)
    token = line.split(" ") #split the line according to spaces, and make a token value that is a list of all parts split by a space for each line
    if (len(token) == 0):
        continue
    count.append(lc + 1948) #lc is the count for the graph
    minimum.append(str(float(token[1]) - 273)) #token[1] = min
    maximum.append(str(float(token[2]) - 273)) #token[2] = max
    mean.append(float(token[3].strip()) - 273) #Mean has to treated as a number, hence the float(), and strip() is used to get rid of \ns after the token
#print(count)
#print(mean)
#print(lines[0]) #URL of file
#print(lines[1]) #Minimum
#print(lines[2]) #Maximum
#print(lines[3]) #Mean
#print(lines) #each iteration will print out a line of f
f.close() #close f to end the program

plt.plot(count, mean, color = 'blue')
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
plt.xlabel('Years', fontsize = 23)
plt.ylabel('Annual Mean Air Temperature checked four times daily', fontsize = 23)
plt.title('Air Temperature Means of each year checked four times a day', fontsize = 23)
plt.show()
