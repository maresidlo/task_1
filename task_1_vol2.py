import os
import subprocess
import psutil
import pathlib
import pandas as pd
import matplotlib.pyplot as plt

# Creating info_file to put information in
info_file = input("Name of file to save values: ")
info_file += ".csv"

# select process
path = pathlib.PurePath(input("input path: "))
time_interval = int(input("set measuring time interval(in seconds): "))
print("----------------------------------------------")
print("TIME CPU_USAGE  RAM         WSET       PSET ")
shell_process = subprocess.Popen([path], shell=True)
parent = psutil.Process(shell_process.pid)

# Make sure process is created
while parent.children() == []:
    continue
children = parent.children(recursive=True)
child_pid = children[0].pid
Number_of_handles = psutil.Process.num_handles(parent)


# collecting data in lists
TIME, CPU, RAM, WSET, PSET = [], [], [], [], []
i = 0
while shell_process.poll() is None:
    i += 1
    if i % time_interval == 0:
        Working_set = str(parent.memory_info()[0])
        private_bytes = str(parent.memory_info()[1])
        CPU_usage = str(psutil.cpu_percent(time_interval))
        RAM_memory = str(psutil.virtual_memory().percent)
        TIME.append(str(i))
        CPU.append(str(CPU_usage))
        RAM.append(str(RAM_memory))
        WSET.append(str(Working_set))
        PSET.append(str(private_bytes))
        print(i,"   ",CPU_usage,"    ", RAM_memory, "    ", Working_set, "  ", private_bytes)

# Time of measurement can be added here to end process sooner
# Subprocess.check_output("Taskkill /PID %d /F" % child_pid) to kill open process

# Putting data into table
new_data = {"TIME": TIME, "CPU": CPU, "RAM": RAM, "WSET":WSET, "PSET":PSET}
df = pd.DataFrame(data=new_data)
df.to_csv(info_file)
file_path = pathlib.Path(os.path.abspath(info_file)).as_uri()
# Printing values out
print(f"Current path: {os.getcwd()} ")
print(f"Number of open handles: {Number_of_handles}")
print(f"Data path:{file_path} ")
vs = input("Graph: y/n ")

#Creating plot of measured values
plt.style.use("fivethirtyeight")
plt.xlabel("TIME")
plt.ylabel("CPU")
plt.title("TIME/CPU ratio")
xpoints = TIME
ypoints = list(map(float, CPU))
plt.plot(xpoints, ypoints)
plt.subplots_adjust(left=0.14, bottom=0.14)
if vs == "y":
    plt.show()
input()
