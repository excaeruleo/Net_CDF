from netCDF4 import Dataset
import requests
import re
from datetime import *
import urllib
import numpy as np 
import sys 
import os

part = "https://downloads.psl.noaa.gov/Datasets/ncep.reanalysis/surface/" #This is for air temperatures 
spec_file = "air.sig995."
year = 1948
for i in range(74):
    temp = part + spec_file + str(year) + ".nc" #Add part and year together to get the precise directory of sea surface temperature at a certain year
    url = requests.get(temp) #get the contents of temp, of the page
    print("Downloading from URL: " + temp) #print out the full URL of each file from reanalysis data set for the convenience of the user running the program 
    file_name = spec_file + str(year) + ".nc"
    with open (file_name, "wb") as f: #Download the contents of each file link in file_name
        f.write(requests.get(temp).content)
        fh = Dataset(file_name, mode = 'r') #nc_file stored within a Dataset called fh, which is a handle of the netCDF file
        lons = fh.variables['lon'][:] #form an array of all variables with the keyword 'lon'
        lats = fh.variables['lat'][:] #form an array of all variables with the keyword 'lat'
        tmax = fh.variables['air'][:] #Will pictographically display the sea surface temperature of the world using the inputted numeric integer value - 1. Arrays in Python and Java always start with 0, 1, 2, etc....
        tmax_units = fh.variables['air'].units
        lon_0 = lons.mean()
        lat_0 = lats.mean()
        for n in range(len(tmax)):
            tmax = fh.variables['air'][n]
            #print("tmax count: "  + str(n))
            with open ('Air_Temp_Min_Max_Mean_Data_Daily', 'a') as f:
                f.write(file_name + " " + str(np.min(tmax)) + " " + str(np.max(tmax)) + " " + str(np.mean(tmax)) + "\n")
            n += 1
            # print(np.min(tmax))
            # print(np.max(tmax))
            # print(np.mean(tmax))
        fh.close()
    os.remove(file_name)
    year += 1 #Increment the year by one
