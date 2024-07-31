import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = [[1,2,3,4,5],[10,9,8,7,6],[11,12,13,14,15]]

corr_matrix = np.corrcoef(data)

sns.heatmap(corr_matrix)
plt.title('Correlogram')

plt.show()

sns.heatmap(data)
plt.title('Heatmap of Original Data')

plt.show()
