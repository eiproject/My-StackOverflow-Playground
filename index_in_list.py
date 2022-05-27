import numpy as np

def change_val_in_nchannel(layer, nchannel, value):
    a, b, c = layer.shape
    for i in range(layer.shape[0]):
        for j in range(layer.shape[1]):
            if i != j:
                layer[i, j, nchannel - 1] = value

    return layer

layer4= np.zeros((2, 2, 4),dtype=np.uint8)
print(layer4)
layer4[1 < 2, :, :] = 1
#layer4 = change_val_in_nchannel(layer4, 4, 10)
value = 10
nchannel = 1
layer4 = [layer4[i, j, nchannel - 1] * 0 + value for i in range(layer4.shape[0]) for j in range(layer4.shape[1]) if i != j]
print(layer4)