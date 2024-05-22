# Axis Camera NTP Script 
This script was written to utilize Axis VAPIX commands to mass change the NTP (Network Time Protocol) on Axis cameras to sync time on all devices at once. This script is written in python. 

## Usage
To utilize, open the devicelist.csv and add each of your cameras to the list. The first column is the device name and the second column is the device IP address. Ensure the file is saved in the same directory as the ntp.py script. The script will output log file with the results utilizing the name, IP address and whether the script suceeded or failed.

Once the devicelist.csv file is saved, run the ntp.py script. Upon start of the script, it will ask you for the device username and password (NOTE: run the script on devices with the same username and password). The script will check to see if the device is online first with a ICMP request and if alive, it will run the NTP update script. 



<a href="https://www.buymeacoffee.com/mckee3304" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-blue.png" alt="Buy Me A Coffee" height="41" width="174"></a>
