# Import libraries
from scipy.spatial.distance import *
import matplotlib.pyplot as plt
import collections

print("Libraries Imported Successfully")

# Collect all MD5 strings into md5_list
md5_list = []
file_name = 'VirusShare_00000.md5'

with open(file_name) as file:
    for line in file:
        md5_list.append(line.rstrip())  # rstrip gets rid of '\n'

md5_list = md5_list[12:]    # Discard the head intro

# print(md5_list)
print("Total Length: " + str(len(md5_list)))

# Change MD5 String into Bit String
def md52bitStr(md5_str):
    return bin(int("0x" + md5_str, 16))[2:]

###### Distance Functions ######
def dis0Vec(bin_str):
    return bin_str.count('0')








# Collect distances into dictionary
lib = {}

for md5_str in md5_list:
    dis = dis0Vec(md52bitStr(md5_str))
    if dis in lib:
        lib[dis] += 1
    else:
        lib[dis] = 1


# Sort lib
sorted_lib = collections.OrderedDict(sorted(lib.items()))
print(sorted_lib)

# Plot
# plt.scatter(lib.keys(), lib.values())
plt.plot(sorted_lib.keys(), sorted_lib.values())
plt.show()