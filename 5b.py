import matplotlib.pyplot as plt
import math

labels = ['A', 'B', 'C', 'D', 'E']
stats = [10, 20, 30, 40, 50]

angles = [2 * math.pi * i / 5 for i in range(5)]

stats.append(stats[0])
angles.append(angles[0])

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

#ax.fill(angles, stats, alpha=0.25)
ax.plot(angles, stats)
ax.set_yticklabels([])


plt.show()