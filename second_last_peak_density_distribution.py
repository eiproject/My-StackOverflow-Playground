import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import seaborn as sns

test = [8, 7, 7, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 7, 7, 7, 7, 7, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 7, 7, 7, 7, 7, 8, 12] 
ax = sns.kdeplot(test)
x = ax.lines[0].get_xdata() # Get the x data of the distribution
y = ax.lines[0].get_ydata() # Get the y data of the distribution
xy = [[x[i], y[i]] for i in range(len(x))]

# find peak
peak_coord = [xy[i] for i in find_peaks(y)[0]]
sorted_peak = sorted(peak_coord, key=lambda x: x[1])
sorted_peak.reverse() # [[7.01539631380498, 0.7002187588539351], [7.921442255354041, 0.3685891140800782], [3.984828854140883, 0.043144074377544736]]

# second peak
second_peak = sorted_peak[1] # [7.921442255354041, 0.3685891140800782]

plt.show()