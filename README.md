
# Android Wifi Config Store XML to TXT
Hello! This is a python script for the "WifiConfigStore.xml" that Android devices use for saving Wi-Fi credentials. This script takes SSIDs and passwords from the file ( you can extract it from /data/misc/apexdata/com.android.wifi/ ) and exports them to a "data.txt" file with the following format:

    SSID: Example
    Password: Example12345
    
    SSID: Lorem
    Password: Ipsum12345

# Usage
In order to use it, execute it from the command console adding the .xml file as an argument:

    python main.py "WifiConfigStore.xml"

The script will leave you with a "data.txt" file in the executing directory.
