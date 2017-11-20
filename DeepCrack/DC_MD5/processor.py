# Import libraries
from scipy.spatial.distance import *
import matplotlib.pyplot as plt
import collections

print("Libraries Imported Successfully")

# Initializations
md5_list = []
file_name = 'VirusShare_00000.md5'
MD5_BIT_LENGTH = 128

# Collect all MD5 strings into md5_list
with open(file_name) as file:
    for line in file:
        md5_list.append(line.rstrip())  # rstrip gets rid of '\n'

md5_list = md5_list[12:]    # Discard the head intro

# print(md5_list)
print("Total Length: " + str(len(md5_list)))

# Change MD5 String into Bit String
def md52bitStr(md5_str):
    return bin(int("0x" + md5_str, 16))[2:]





###### Distance Functions: Average bit value for each bit ######
# Find the average bit for each vec
bit_count_vec = [0] * MD5_BIT_LENGTH

def addBitVec(bin_str):
    return [x + int(y) for x,y in zip(bit_count_vec, list(bin_str))]

for md5_str in md5_list:
    bit_count_vec = addBitVec(md52bitStr(md5_str))

bit_count_vec = [x/len(md5_list) for x in bit_count_vec]
print(bit_count_vec)
plt.plot(bit_count_vec)
plt.show()





###### Distance Functions: Hamming Distance to 0-vector ######
def dis0Vec(bin_str):
    return bin_str.count('0')

# # Collect distances into dictionary
# lib = {}

# for md5_str in md5_list:
#     dis = dis0Vec(md52bitStr(md5_str))
#     if dis in lib:
#         lib[dis] += 1
#     else:
#         lib[dis] = 1


# # Sort lib
# sorted_lib = collections.OrderedDict(sorted(lib.items()))
# print(sorted_lib)

# # Plot
# # plt.scatter(lib.keys(), lib.values())
# plt.plot(sorted_lib.keys(), sorted_lib.values())
# plt.show()