#Read in from file that you are using to derive min, max, and average temperatuers of each date of each year
#Make a line graph using the plotly express module
#Make a line graph for minimum, maximum, and mean. Making a line graph of the mean is the absolute minimum.
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

figure, axis = plt.subplots(1, 2)
axis[0].plot(count, mean, color = 'blue')
axis[0].set_title('Air Temperature Means of each year checked four times a day', fontsize = 23)
x = count 
axis[0].tick_params(axis = 'both', which = 'major', labelsize = 15)
#axis[0].set_xticklabels(count, fontsize = 15)

axis[1].plot(count1, mean1, color = 'blue')
axis[1].set_title('Sea Surface Temperature Means of each year', fontsize = 23)
#plt.xticks(fontsize = 15)
#plt.yticks(fontsize = 15)
axis[1].tick_params(axis = 'both', which = 'major', labelsize = 15)
figure.tight_layout() #maintain proper spacing between two horizontally adjacent plots with humongous titles 
plt.show()
#plt.plot(count, mean)
#plt.title("Air Temperature Means of each year checked four times a day")
#plt.title("Sea Surface Temperature Means of each year")
#plt.show()
#The computer is an idiot. It can only execute what you write. Use your brain.
