import numpy as np
import matplotlib.pyplot as plt

# def zero_pad(X, pad):
#     """
#     Pad with zeros all images of the dataset X. The padding is applied to the height and width of an image, 
#     as illustrated in Figure 1.
    
#     Argument:
#     X -- python numpy array of shape (m, n_H, n_W, n_C) representing a batch of m images
#     pad -- integer, amount of padding around each image on vertical and horizontal dimensions
    
#     Returns:
#     X_pad -- padded image of shape (m, n_H + 2 * pad, n_W + 2 * pad, n_C)
#     """
    
#     #(≈ 1 line)
#     # X_pad = None
#     # YOUR CODE STARTS HERE
#     X_pad = np.pad(X,((0,0),(pad,pad),(pad,pad),(0,0)))    
#     # YOUR CODE ENDS HERE
    
#     return X_pad

# np.random.seed(1)
# x = np.random.randn(4, 3, 3, 2)
# x_pad = zero_pad(x, 3)
# print ("x.shape =\n", x.shape)
# print ("x_pad.shape =\n", x_pad.shape)
# print ("x[1,1] =\n", x[1, 1])
# print ("x_pad[1,1] =\n", x_pad[1, 1])

# fig, axarr = plt.subplots(1, 2)
# axarr[0].set_title('x')
# axarr[0].imshow(x[0, :, :, 0])
# axarr[1].set_title('x_pad')
# axarr[1].imshow(x_pad[0, :, :, 0])


# output = [['InputLayer', [(None, 64, 64, 3)], 0],
#         ['Conv2D', (None, 64, 64, 8), 392, 'same', 'linear', 'GlorotUniform'],
#         ['ReLU', (None, 64, 64, 8), 0],
#         ['MaxPooling2D', (None, 8, 8, 8), 0, (8, 8), (8, 8), 'same'],
#         ['Conv2D', (None, 8, 8, 16), 528, 'same', 'linear', 'GlorotUniform'],
#         ['ReLU', (None, 8, 8, 16), 0],
#         ['MaxPooling2D', (None, 2, 2, 16), 0, (4, 4), (4, 4), 'same'],
#         ['Flatten', (None, 64), 0],
#         ['Dense', (None, 6), 390, 'softmax']]



