from netCDF4 import Dataset #Import Dataset from netCDF4 library 
import numpy as np #Import the use of numpy 
import matplotlib.pyplot as plt #Import pyplot from matplotlib library to display a plot 
from mpl_toolkits.basemap import Basemap #Import Basemape from mpl_toolkits.basemap library 
import sys

#Create a dataset using the file mentioned below to model air temperature around the world 
nc_file = 'sst.mon.mean.nc' #File name stored within a variable called nc_file
fh = Dataset(nc_file, mode = 'r') #nc_file stored within a Dataset called fh, which is a handle of the netCDF file  
print (fh.variables.keys()) #Prints out the variables associated with fh as keys in a dictionary 
print('\n') #return a new line 
print (fh.variables['sst']) #Prints out all variables associated with sst in fh 
print(sys.argv[0]) #Prints out the name of the inputted file 
#If statement to check the numeric integer value inputted after the run command of this file 
lons = fh.variables['lon'][:] #form an array of all variables with the keyword 'lon'
lats = fh.variables['lat'][:] #form an array of all variables with the keyword 'lat'
sst = fh.variables['sst'][:] #Takes all the three dimensional arrays contained in variable sst from the Dataset fh
tmax_units = fh.variables['sst'].units
'''for month in time: 
    year = sst / 12
'''
print(fh.variables['time'][:]) #print out all values contained in variable time in Dataset fh 
total = 0
months = []
averages = []
for month in range(len(fh.variables['time'][:])): #loop through variable time in fh to sum up all value of variable sst 
    monthAv = np.average(sst[month,:,:]) #Takes the average of each month
    with open ('SST_Monthly_Average', 'a') as f: 
        f.write(str(month) + " " + str(monthAv) + "\n")
        months.append(month + 1)
        averages.append(monthAv)
    plt.plot(months, averages, color = "blue")
    f.close()
#Editing the tick font size, i.e. editing the font size of the numbers displayed on the x and y axes 
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
# naming the x axis
plt.xlabel('Months', fontsize = 25)
# naming the y axis
plt.ylabel('Monthly Average Sea Surface Temperature', fontsize = 25)
plt.title("Monthly Average of Sea Surface Temperature 1991-2020", fontsize = 40)
plt.show()
print(sst[1,:,:])
print("The type of tmax is {} and the size is {}.".format(type(sst), sst.ndim))

fh.close()
