import numpy as np
import matplotlib.pyplot as plt

# ===============================
# Input file settings
# ===============================

inputfile = "./data/1D_data.txt"   # Path to the input data file
Encoding  = "utf-8"                # Character encoding of the input file

# ===============================
# Read data from file
# ===============================

data = []
try:
    with open(inputfile, mode="r", encoding=Encoding) as f:
        for line in f:
            data.append(line.split())
except FileNotFoundError:
    print("File not found. Please check the path.")
except UnicodeDecodeError:
    print("Failed to read the file. Check the encoding.")

data = np.array(data, dtype=float).T
#print(data)

# ===============================
# Output file settings
# ===============================

outputfile = "./1D_data.png"

# Plot style settings
#plt.rcParams["font.family"] = "Arial"           #for Windows
plt.rcParams['font.family'] = 'Liberation Sans' #for Linux

# Create figure and axes
fig, ax1 = plt.subplots(figsize = (5, 4), facecolor = "w")

# Axis labels and title
plt.title(r'Sample Graph')
plt.xlabel(r'Time, $t$ [s]',fontsize=14)
plt.ylabel(r'Height, $h_z$ [m]',fontsize=14)

# Axis limits
plt.xlim(0.0, 20.0)
plt.ylim(-1.5, 1.5)

# Tick label size
plt.tick_params(labelsize=12)

# Custom ticks (optional)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
#ax1.set_xticks(np.arange(0.0, 25.0, 5.0))
#ax1.set_yticks(np.arange(-1.5, 2.0,  0.3))

# ===============================
# Plot data
# ===============================

ax1.plot([-1.0e10, 1.0e10], [0.0, 0.0], color='black', linestyle='--', linewidth = 0.5)
ax1.plot(data[0], data[1], color='black', marker='o', markerfacecolor='white', linestyle='-',  label=f'Column 1', linewidth = 1)
ax1.plot(data[0], data[2], color='blue',  marker='^',                          linestyle='--', label=f'Column 2', linewidth = 1)
ax1.plot(data[0], data[3], color='red',   marker='x', markerfacecolor='white', linestyle=':',  label=f'Column 3', linewidth = 1)
ax1.plot(data[0], data[4], color='green', marker='s', markerfacecolor='white', linestyle='-.', label=f'Column 4', linewidth = 1)

# Legend and layout
plt.legend(fontsize=10, edgecolor="black", facecolor='white', framealpha=1.00)
plt.tight_layout()

# Save figure
plt.savefig(outputfile, dpi=300)
#plt.show()   # Uncomment to display the figure