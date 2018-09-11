
import numpy as np
from matplotlib.ticker import MaxNLocator
from collections import namedtuple

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

def worst():
    # worst config
    batch_size = 32
    num_classes = 10
    epochs = 10
    hidde_n = 32
    lr = 0.1




    accuracy = [0.4985, 0.5836, 0.5973, 0.6044, 0.6090, 0.6212, 0.6200, 0.6150, 0.6221, 0.6255]

    loss = [4.1595, 1.5810, 1.6032, 1.5167, 1.5673, 1.6020, 1.5877, 1.4854, 1.4932, 1.5265]
        
    # grafico 1
    plt.plot(accuracy, 'o--')
    plt.title("Worst config accuracy")
    plt.ylabel("Accuracy")
    plt.xlabel("epoch")
    plt.show()


    # grafico 2
    objects = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    y_pos = np.arange(len(objects))
    performance = accuracy
    
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Accuracy')
    plt.xlabel("epoch")
    plt.title('Worst config accuracy') 
    plt.show()


    # grafico 3
    x = accuracy
    y = loss
    plt.ylabel("loss")
    plt.xlabel("accuracy")
    plt.title('Worst config accuracy') 
    plt.scatter(x, y)
    plt.show()

def good():

    epoch = 10
    batch_size = 512
    lr = 0.001
    hidden = 128

    accuracy = [0.8469, 0.9225, 0.9423, 0.9519, 0.9591, 0.9637, 0.9677, 0.9709, 0.9728, 0.9747]
    loss= [0.5567, 0.2670, 0.2032, 0.1663, 0.1427, 0.1248, 0.1102, 0.1002, 0.0914, 0.0844]


    # grafico 1
    plt.plot(accuracy, 'o--')
    plt.title("best config accuracy")
    plt.ylabel("Accuracy")
    plt.xlabel("epoch")
    plt.show()


    # grafico 2
    objects = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    y_pos = np.arange(len(objects))
    performance = accuracy
    
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Accuracy')
    plt.xlabel("epoch")
    plt.title('Best config accuracy') 
    plt.show()


    # grafico 3
    x = accuracy
    y = loss
    plt.ylabel("loss")
    plt.xlabel("accuracy")
    plt.title('best config accuracy') 
    plt.scatter(x, y)
    plt.show()

if __name__ == "__main__":
    worst()
    good()