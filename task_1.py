import os
import psutil
import pathlib

print("task.txt is running")

# Measuring CPU in time interval
interval = 5

# creating file to put information in
file = "Usage.txt"

# Current working directory
cwd = os.getcwd()

# returning process id to measure number of handles
process = psutil.Process(os.getpid())

# Absolute file path
path = os.path.abspath(file)
Currect_path = cwd

# Measuring CPU through interval
CPU_usage = str(psutil.cpu_percent(interval))

# Measuring RAM used to run this process
# psutil.virtual_memory() outputs list of 5 numbers, total memory,
# used memory, percentage, available memory and free memory
RAM_memory = str(psutil.virtual_memory()[2])

# Number of working set bytes
Working_set = str(psutil.virtual_memory()[0])

# Number of private bytes
private_bytes = str(psutil.virtual_memory()[1])

# Number of handles
Number_of_handles = psutil.Process.num_handles(process)

# Creating opanable file through console
file_path = pathlib.Path(path).as_uri()

# printing out measured information
print(f"Current path: {cwd} \n")
print(f"The CPU usage is: {CPU_usage} % in {interval} second \n")
print(f"RAM memory used: {RAM_memory} % \n")
print(f"Working set: {Working_set} \n")
print(f"Private bytes:{private_bytes} \n")
print(f"Number of open handles: {Number_of_handles} \n")
print(f"file path:{file_path}\n")

# Putting information into text file
with open(file, "w") as f:
    f.write(f"Current path: {cwd} \n")
    f.write(f"The CPU usage is: {CPU_usage} in {interval} second \n")
    f.write(f"RAM memory used: {RAM_memory} % \n")
    f.write(f"Working set: {Working_set} \n")
    f.write(f"Private bytes:{private_bytes} \n")
    f.write(f"Number of open handles: {Number_of_handles} \n")

