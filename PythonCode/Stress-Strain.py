import re
import matplotlib.pyplot as plt
import numpy as np
import math
import os

pattern = re.compile("_SampleName")
pattern = re.compile("Comment")

time = []
load = []
strain1 = []
slack = []
stress = []
strain = []
extension = []

# for line in open("TESTTEXT.txt"):
#     for match in re.finditer(pattern, line):
#         print(line)

with open('TESTTEXT.txt', 'r') as f:
    textfile_temp = f.readlines()
    config_found = False

    for line in textfile_temp:
        if re.match(r'\s*EndData', line):
            config_found = False
        elif config_found:
            i = line.strip()
            i = i.split(",")
            stress_val =float(i[4])
            stress.append(stress_val)
            strain_val = float(i[5])
            strain.append(strain_val)
        elif re.match(r'\s*"min", "N", "mm", "mm", "MPa", "%", "mm"', line):
            config_found = True

strain_beg = list(filter(lambda x: x<=(0.1), strain))
stress_beg = []

for i in range(len(strain_beg)):
    stress_beg.append(stress[i])

rise = (stress_beg[0] - stress_beg[-1])
run = (strain_beg[0] - strain_beg[-1])
slope = rise/run

strain_line = list(filter(lambda x: x<=1, strain))
# print(strain_line)

x = np.array(strain_line)
y = slope*(x - 0.2)

uts = max(stress)
print(uts)
el = max(strain)
print(el)
plt.plot(strain, stress, linestyle = '-', color = 'k', linewidth = 1)
plt.plot(x, y, linestyle='-', color = 'gray', linewidth = 1)
plt.xlim([-.1, max(strain)*1.25])
plt.ylim([-1, max(stress)*1.25])
plt.xlabel("Strain")
plt.ylabel("Stress")
plt.title(os.path.basename(f.name))
plt.show()
