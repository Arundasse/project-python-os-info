#!/usr/bin/python3

#SoC Project: Python OS Info: ARUN DASSE s13 cfc2407
#Lecturer name: James

print('PROJECT: Python OS Info')
print('ARUN DASSE - s13')
print('Lecturer: JAMES')

# ~ Objective: Create automation to display the operating system information.

# ~ Part 1: Display the OS version - if windows, display the windows details; if executed on Linux, display the Linux details.
# ~ Reference credit: https://www.w3resource.com/python-exercises/python-basic-exercise-43.php
#Steps: 
#1. Importing the Module = python codes that was already created. The codes can be imported and used in your current environment / script.
#2. For the part 1: Two modules were imported: os and platform;  
#3. The OS module in Python provides functions for interacting with the operating system.
#4. The platform module in Python is used to access the underlying platform's data, such as, hardware, operating system, etc.
#5. The commands os.name(), platform.system() and platform.release() helps to display the name of the operating system and its version.

# ~ Python Scritping:

import os
import platform

print("\nSection 1 displays the Linux Details:")
print("\nName of the operating system:",os.name)
print("\nName of the OS system:",platform.system())
print("\nVersion of the operating system:",platform.release())

# ~ Part2: Display the private IP address, public IP address, and the default gateway.
# ~ Steps:
#1. With the help of the command os.system(<repective linux command to display the ip address>).
#2. This sections display the private IP, public IP address and default gateway
#3. Using the Linux commands 'grep' and 'awk' (inside os.system) to display the exact info needed.

print("\nSection 2 displays the IP addresses and Deafult Gateway:")

print("\nThe private IP address of the system is:")
print(os.system("ifconfig | grep broadcast | awk '{print $2}'"))

print("\nThe public IP address of the system is:") 
print(os.system("curl ifconfig.io") )

print("\nThe Default Gateway is:")
print(os.system("route | grep default | awk '{print $2}'"))

# ~ Part3: Display the hard disk size, free and used space.
# ~ Reference credits: https://www.geeksforgeeks.org/python-shutil-disk_usage-method/#:~:text=disk_usage()%20method%20in%20Python,attributes%20total%2C%20used%20and%20free.
#Steps: 
#1. shutil module in Python provides many functions of high-level operations on files and collections of files.
#2. Defining the path, in this case, I am provide my current working directory path.
#3. With the help of the command 'shutil.disk_usage(path)' stored to a variable stat - we can get the info of hard disk size, used and free space.
#4. Print the variable stat to display the info.

print("\nSection 3 displays the Hard disk size, used and free space:")

import shutil
  
# Path
path = "/home/arun/pf/pyproject"
  
# Get the disk usage statistics
# about the given path
stat = shutil.disk_usage(path)
  
# Print disk usage statistics
print("\nDisk usage statistics:")
print(stat)

# ~ Part4: Display the top five directories and their size
# ~ Steps:
#1. The first command used in this section is os.getcwd() to print the current working directory
#2. Before displaying the specific directory/files, using the command os.listdir() to list out all the files/subfolders inside the current working directory.
#3. Saving all the files/folders to a variable dir_items.
#4. Initiating the for loop to be executed for everyitem (file or folder) saved to the variable dir_items.
#5. Next step is to check the if condition: if the size of any file/folder inside dir_items is greater than 15000 bytes.
#6. Then it will display only the folders satisfies the condition set.

print("\nSection 4 displays the top five directories and their sizes:")
print("\nThe current working directory is: ",os.getcwd())
print("\nDirectories in current working directory is: ",os.listdir())
print("\nThe top five directories in the current working folder is: ")
dir_items=os.listdir('/home/arun/pf/pyproject')
for eachitem in dir_items:
	if os.path.getsize(eachitem) > 15000:
		print(os.path.getsize(eachitem),'bytes', eachitem)

# ~ Part5: Display the CPU usage; refresh every 10 seconds
# ~ Reference Credits: https://www.geeksforgeeks.org/python-script-that-is-executed-every-5-minutes/
# ~ Steps:
#1. Importing psutil module which helps to keep track of various resources utilization in the system. Usage of resources like CPU, memory, disks, network, sensors can be monitored.
#2. The function psutil.cpu_percent() provides the current system-wide CPU utilization in the form of a percentage.
#3. The given interval in the time.sleep() function is 10 seconds and make while loop is true. 
#4. The function will sleep for the given time interval. After that, it will start executing and display the CPU utilization info.
#5. pip install psutil - Before import psutil; install the psutil in Linux/Ubuntu if the module not found.

import psutil
import time
print("\nSection 5 displays the CPU usage for every 10 seconds:")
while(True):
    print(psutil.cpu_percent())
    time.sleep(10)

