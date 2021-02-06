# importing libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

series = pd.Series(3 * np.random.rand(4),
                   index=['a', 'b', 'c', 'd'], name='series')

series.plot.pie(figsize=(4, 4))
plt.show()