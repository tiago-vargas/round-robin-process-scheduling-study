import pandas as pd
from process import Process
from scheduler import *

p1 = Process(1, 8)
p2 = Process(2, 2)
p3 = Process(3, 7)
p4 = Process(4, 3)
p5 = Process(5, 5)

process_list = [p1, p2, p3, p4, p5]

scheduler(process_list)

data = {
    "Process": cpu_scheduling_pname,
    "Start": scheduling_starts,
    "End": scheduling_ends
}

df = pd.DataFrame(data)

df["Quanta"] = df["End"] - df["Start"]

print(df)