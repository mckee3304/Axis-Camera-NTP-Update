import csv
import os
import requests
import sys
import time
from datetime import datetime, date

# define time
now = datetime.now()

# define script start time
startTime = time.time()
startTimeNormal = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time())) #converts time from epoch to normal

# define log file name to include filename + time
logSavePath = './'
logFileNameString = str("ScriptLog-")
logFileDate = now.strftime("%m%d%Y")
LogFileDateString = str(logFileDate)
logFileExtension = ".txt"
logFileName =  os.path.join(logSavePath, logFileNameString + LogFileDateString + logFileExtension)

# create log file
logFile = open(logFileName, "a")

# start script 
print("Starting NTP Update on Axis Cameras...\n")
logFile.write("Start Time: " + str(startTimeNormal) + "\n")

# prompt for usename & password
username = input("Enter Username of Camera: ")
password = input("Enter Password of Camera: ")
NTPServer = input("Enter new NTP Server IP Address/Hostname: ")

# open list of devices
with open('devicelist.csv', 'r') as csvinput:
    reader = csv.DictReader(csvinput)       
    for row in reader:
        ip = row["IPAddress"]
        auth = requests.auth.HTTPDigestAuth(username, password)
        body = {
            "apiVersion": "1.1",
            "method": "setNTPClientConfiguration",
            "params": {
                "serversSource": "static", 
                "staticServers": [NTPServer]
            }    
        }
        response = os.popen(f"ping {ip} -n 1").read()
        if "Received = 1" in response:   
            r = requests.post("http://{}/axis-cgi/ntp.cgi".format(ip), json=body,  auth=auth)
            if r.status_code == 200:
                device = row["Device"]
                ipAddress = ip
                statusCode = str("Success ")
                # write device issue to log
                logFile.write(str(statusCode) + "     " + str(ipAddress) + "   " + str(device) + "\n")
            elif r.status_code == 401:
                device = row["Device"]
                ipAddress = ip
                statusCode = str("Authentication Failed ") + str(r.status_code)
                # write device issue to log
                logFile.write(str(statusCode) + "     " + str(ipAddress) + "   " + str(device) + "\n")              
            else:
                device = row["Device"]
                ipAddress = ip
                statusCode = str("Failed ") + str(r.status_code)
                # write device issue to log
                logFile.write(str(statusCode) + "     " + str(ipAddress) + "   " + str(device) + "\n")             
        else:
            logFile.write(str("Ping Failed") + "     " + str(ipAddress) + "   " + str(device) + "\n")  
            continue     

# calculate time it took to complete script
endTime = time.time()
endTimeNormal = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time())) #converts time from epoch to normal
executionTime = ((endTime - startTime)/60)
calulatedTime = round(executionTime, 2)

# close log file
logFile.write("End Time: " + str(endTimeNormal) + "\n")
logFile.write("Total Execution Time: " + str(calulatedTime) + " Minutes" + "\n")
logFile.close()

# script complete
print("\n" + "NTP Update Complete!")