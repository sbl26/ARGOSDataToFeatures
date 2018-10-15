##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2018
## Author: Sarah.Lanier@duke.edu for ENV859)
##---------------------------------------------------------------------

#Import modules
import sys, os, arcpy

# Set input variables (Hard-wired)
inputFile = 'V:/ARGOSTracking/Data/ARGOSData/1997dg.txt'
outputFC = "V:/ARGOSTracking/Scratch/ARGOStrack.shp"

#open the ARGOS data file for reading
inputFileObj =  open(inputFile, 'r')

#get the first line so we can loop
lineString= inputFileObj.readline()
print(lineString)
while lineString:
    #set code to run only if the line contrains the string "Date: "
    if("Date :" in lineString):

        #split the line string into a list
        lineList= lineString.split()

        #get attributes from first line
        tagID= lineList[0]
        break
        
    #get the next line
    lineString= inputFileObj.readline()
    
   
        