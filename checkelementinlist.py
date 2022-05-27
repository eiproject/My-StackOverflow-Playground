import numpy as np

matrix2 = ([['high','h ight','hi ght','h i g ht'],
       ['man','ma n','ma th','mat h'],
       ['ja cket','j a ck et','jack et','ja m'],
       ['ma nkind','jack',' hi ','hi']])

matrix3 = []
for mat in matrix2:
    tmp = []
    for m in mat:
        tmp.append(m.split(' '))
    matrix3.append(tmp)

list2 = ['hi']#, 'ma', 'ja']

matrix4 = []
for mat in matrix3:
    tmp = []
    for m in mat:
        print(np.isin(m, list2))
        tmp.append(np.isin(m, list2))

    # if len(tmp) > 1:
    #     print(len(tmp))
    #     matrix4.append(np.logical_or(tmp))


print(matrix4)