from Implementation_in_Python.WassersteinDistance import Wasserstein_Dist
from Implementation_in_Python.OnImages import AllEuclideanDistance
import os

import numpy as np
from PIL import Image

from PIL import ImageChops
import math, operator
from functools import reduce

def makeImNumpy(array):
    arr = []
    for im in array:
        arr.append(np.asarray(im))
    return(arr)

def GetImageList(path):
    XX = []
    YY = []
    
    print("Walking through the data of path: ", path)
    dirs = os.listdir(path)
    
    if not(len(dirs)==2):
        print("ERROR: The data is not in the right order. Read tutorial for more information.")
        return(0,0)
    
    path1 = os.path.join(path, dirs[0])
    path2 = os.path.join(path, dirs[1])
    
    #im1 = np.asarray(Image.open(os.path.join(path1, "0_0.jpg")))
    #im2 = np.asarray(Image.open(os.path.join(path2, "0_351.jpg")))
    im1 = Image.open(os.path.join(path1, "0_0.jpg"))
    im2 = Image.open(os.path.join(path2, "0_351.jpg"))
    
    XX.append(im1)
    YY.append(im2)
    
    print("Using the directories: ", path1, path2)
    
    return(im1,im2)
    

def compHist(im1, im2):
    # ref: https://stackoverflow.com/questions/1927660/compare-two-images-the-python-linux-way
    h1 = im1.histogram()
    h2 = im2.histogram()
    rms = math.sqrt(reduce(operator.add, map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
    return(rms)

def quickCheck(im1, im2):
    return ImageChops.difference(im1, im2).getbbox() is None


if __name__ == '__main__':

    im1, im2 = GetImageList("sample\\")
    XX = np.asarray(im1)
    YY = np.asarray(im2)
    
    #print(XX)
    
    #Dist = Wasserstein_Dist(XX, YY)
    #EucDist = AllEuclideanDistance([XX], [YY])
    
    # Histogram comparison
    hist = compHist(im1, im2)
    
    QD = quickCheck(im1, im2)
    
    #print(Dist.shape)
    
    #print("Error is : ", np.sum(Dist))
    #print("Error is : ", np.max(Dist))
    #print("Euclidean Error is : ", EucDist)
    
    print("Quick check, \"Are images same?\" ", QD)
    print("Histogram difference is : ", hist)