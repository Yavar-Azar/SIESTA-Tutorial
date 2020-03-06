import numpy as np
import matplotlib.pyplot as plt
import sys


filename=sys.argv[1]
print("dos file is  ", sys.argv[1])

dosdata=np.loadtxt(filename)

plt.xlabel("Energy (eV) ", fontsize=18)
plt.ylabel("DOS  (states/eV)", fontsize=18)
plt.ylim(0, np.max(dosdata[:,1]*1.05))
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)



plt.plot(dosdata[:,0], dosdata[:,1], linewidth=2)
plt.savefig("test2.png", dpi=300, bbox_inches="tight")

plt.show()
        






