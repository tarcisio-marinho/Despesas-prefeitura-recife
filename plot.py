
import numpy as np
from matplotlib.ticker import MaxNLocator
from collections import namedtuple

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

batch_size = 32
num_classes = 10
epochs = 10
hidde_n = 32
lr = 0.1




accuracy = [0.4985, 0.5836, 0.5973, 0.6044, 0.6090, 0.6212, 0.6200, 0.6150, 0.6221, 0.6255]

loss = [4.1595, 1.5810, 1.6032, 1.5167, 1.5673, 1.6020, 1.5877, 1.4854, 1.4932, 1.5265]
    
# # grafico 1
# plt.plot(accuracy, 'o--')
# plt.title("Worst config accuracy")
# plt.ylabel("Accuracy")
# plt.xlabel("epoch")
# plt.show()


# # grafico 2
# objects = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# y_pos = np.arange(len(objects))
# performance = accuracy
 
# plt.bar(y_pos, performance, align='center', alpha=0.5)
# plt.xticks(y_pos, objects)
# plt.ylabel('Accuracy')
# plt.xlabel("epoch")
# plt.title('Worst config accuracy') 
# plt.show()



x = accuracy
y = loss
plt.ylabel("loss")
plt.xlabel("accuracy")
plt.title('Worst config accuracy') 
plt.scatter(x, y)
plt.show()