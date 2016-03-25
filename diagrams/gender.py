import matplotlib.pyplot as plt
import numpy as np

labels = ["female", "male"]
data = [2, 14]
colors = ["purple", "darkorange"]

xlocations = np.array(range(len(data)))+0.5
#xlocations = np.array(range(len(data)))+0.25
width = 0.5
plt.bar(xlocations, data, width=width, color=colors)
plt.yticks(range(0, 18, 2))
plt.xticks(xlocations + width/2, labels)
plt.xlim(0, xlocations[-1]+width*2)
plt.gca().get_xaxis().tick_bottom()
plt.gca().get_yaxis().tick_left()

#plt.title("Perceived gender")

plt.show()

