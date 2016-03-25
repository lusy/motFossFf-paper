import matplotlib.pyplot as plt
import numpy as np

data = [7, 5, 1, 3]
labels = ["2 years or less", "approx. 3 years", "4 years (2004-2008)", "more than 8 years"]
colors = ('#ff8080', '#ff4d4d', '#cc0000', '#990000')

#def format_part (x, i):
#    return data[i]

#plt.pie(data, labels=labels, colors=colors, autopct=lambda x, i: data[i])
plt.pie(data, labels=labels, colors=colors)
plt.axis('equal')
#plt.axes(aspect=1)

plt.show()
