# import glob, os

# for directory_path in glob.glob("a/*"):
#     fruit_label = directory_path.split("\\")[-1]
#     for img_path in glob.glob(os.path.join(directory_path, "*.txt")):
#         print(img_path, fruit_label)

import copy
import pandas as pd
import copy
import pickle
dr = pd.date_range('2020-01-01', periods=10, freq='1H')
test = pd.DataFrame({'target':list(range(10))}, index=dr)
print(test.index.freq)
# >>> <Hour>
# _copy = test.copy(deep=True)
# _copy = copy.deepcopy(test).copy(deep=True)
_copy = pickle.loads(pickle.dumps(test)) 
print(test.index.freq)
# >>> <Hour>
_copy.index.freq = None
print(test.index.freq)
# >>> None # expectet output is <Hour>