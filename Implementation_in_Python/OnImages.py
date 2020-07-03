'''
Using distance to find similarities between two images.
1. Euclidean distance
2. Wasserstein distance
'''

import numpy as np

def EuclideanDistance(image1, image2):
    return np.sum((image1-image2)**2)
    
def AllEuclideanDistance(imgSet1, imgSet2):
    dis = []
    n = 0
    for im1, im2 in zip(imgSet1, imgSet2):
        n += 1
        dis.append(EuclideanDistance(im1, im2))
    return(sum(dis)/n)


if __name__ == '__main__':
    
    '''
    Size = [n, X, Y, L] 
    n -- number of samples
    X -- x dmension
    y -- y dimension
    L -- number of layers
    '''
    
    XX = np.random.normal(1, 1, size=[3, 1024, 768, 3])
    YY = np.random.normal(3, 1, size=[3, 1024, 768, 3])
    
    Dist = AllEuclideanDistance(XX, YY)
    
    print("Euclidean distance is: ", Dist)