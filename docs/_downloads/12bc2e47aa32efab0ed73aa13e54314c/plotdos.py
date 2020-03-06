import argparse

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import sys

import os


parser = argparse.ArgumentParser()
parser.add_argument('-f','--fname', help=' dos file name')
parser.add_argument('-fe','--fermi',  required=False, help='fermi energy')
args = parser.parse_args()


filename=args.fname

dosdata=np.loadtxt(filename)


plt.xlabel("Energy (eV) ", fontsize=18)
plt.ylabel("DOS  (states/eV)", fontsize=18)
plt.ylim(0, np.max(dosdata[:,1]*1.05))
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.plot(dosdata[:,0], dosdata[:,1], linewidth=1)

if (args.fermi!=None):
    fenergy=float(args.fermi)
    ndata=dosdata[dosdata[:,0] < fenergy]
    plt.fill_between(ndata[:,0],ndata[:,1],y2=0, alpha=0.65, color="#764b94", label="Occupied")


plt.legend(fontsize=16)

fig = plt.gcf()
fig.set_size_inches(10, 5.5)

plt.savefig("test.png", dpi=300, bbox_inches="tight")
plt.show()