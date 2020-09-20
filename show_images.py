import numpy as np
from matplotlib import pyplot as plt


results = np.load('pred_imgs.npy')
print(results[0,:,:,:].shape)

img = results[3,0,:,:]
imShape = img.shape
# img = np.reshape(img, (img.shape[2],img.shape[1],img.shape[0]))

print(img.shape)

image =plt.figure()
plt.imshow(img, interpolation='nearest')

plt.show()
plt.savefig("output.png")
