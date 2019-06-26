import os
import re

from ip_time_trace import *

my_dict = {}

f = open(os.path.join(".", 'fw.log'), "r")
array = f.read().split("\n")
for line in array:
    x = re.search(
        r"(\d{4}\-\d{2}\-\d{2}) (\d{2})\:\d{2}\:\d{2}	(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})	(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", line)
    if x:
        if x[1] == "2019-05-27" and (int(x[2]) <= 6 or int(x[2]) >= 18) and x[4] == '54.93.202.69':
            if x[3] in my_dict:
                my_dict[x[3]].append(Trace(int(x[2]), x[4]))
            else:
                my_dict[x[3]] = [Trace(int(x[2]), x[4])]

print(len(my_dict))

# list_sandwich = []
# set_sandwich = set([])
# list_src = []
# set_src = set([])

# for src_ip, traces in my_dict.items():
#     for trace in range(0, len(traces) - 3):
#         if traces[trace].dst_ip != traces[trace+1].dst_ip and traces[trace+1].dst_ip == traces[trace+2].dst_ip and traces[trace].dst_ip == traces[trace+3].dst_ip:
#             list_sandwich.append(traces[trace+1].dst_ip)
#             set_sandwich.add(traces[trace+1].dst_ip)
#             list_src.append(src_ip)
#             set_src.add(src_ip)

# print(len(list_sandwich))
# print(len(set_sandwich))
# print(len(list_src))
# print(len(set_src))
