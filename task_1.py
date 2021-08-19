import os
import psutil
import pathlib
import pandas as pd
import matplotlib.pyplot as plt

file = "Usage.csv"
cwd = os.getcwd()
path = os.path.abspath(file)
process = psutil.Process(os.getpid())
time_interval = int(input("set mesuring time interval(in seconds): "))
time_range = int(input("set lenght of measuring: "))


TIME, CPU, RAM = [], [], []
print("task is running")
with open(file, "w", newline="") as csvfile:
    for i in range(1, time_range+1):
        if i % time_interval == 0 or i == time_range:
            CPU_usage = str(psutil.cpu_percent(time_interval))
            RAM_memory = str(psutil.virtual_memory()[2])
            TIME.append(str(i))
            CPU.append(str(CPU_usage))
            RAM.append(str(RAM_memory))
            print(i, "  ", CPU_usage, "  ", RAM_memory)

Number_of_handles = psutil.Process.num_handles(process)
Working_set = str(psutil.virtual_memory()[0])
private_bytes = str(psutil.virtual_memory()[1])
file_path = pathlib.Path(path).as_uri()

new_data = {"TIME": TIME, "CPU": CPU, "RAM": RAM}
df = pd.DataFrame(data=new_data)
df.to_csv(file)

print(f"Current path: {cwd} ")
print(f"Working set: {Working_set} ")
print(f"Private bytes:{private_bytes} ")
print(f"Number of open handles: {Number_of_handles}")
print(f"Data path:{file_path} ")
vs = input("want to see graph: y/n ")
if vs == "y":
    plt.style.use("fivethirtyeight")
    xpoints = TIME
    plt.xlabel("TIME")
    ypoints = list(map(float, CPU))
    plt.ylabel("CPU")
    plt.plot(xpoints, ypoints)
    plt.title("TIME/CPU ratio")
    plt.subplots_adjust(left=0.14, bottom=0.14)
    plt.show()
input("click to exit")
