# pickling and unpickling
# comments added from github side
# 3rd comment to test out git fetch

import pickle

integers = [1, 2, 3, 4, 5, 6]

with open('pickle-file.p', 'wb') as pfile:
    pickle.dump(integers, pfile)

with open('pickle-file.p', 'rb') as pfile:
    integers = pickle.load(pfile)
    print(integers)




