#splitted array
import numpy as np
arr=np.array([1,2,3,4,5,6])
newarr=np.array_split(arr,3)
print("Original array : ",arr)
print("splitted array : ",newarr)
print("---------")
#splitting arrays into 4 parts
arr=np.array([1,2,3,4,5,6])
newarr=np.array_split(arr,4)
print("Original array : ",arr)
print("splitted array : ",newarr)
print("---------")
#splitting 2D arrays
arr=np.array([[1,2],[3,4],[5,6],[7,8],[9,10]])
newarr=np.array_split(arr,3)
print("Original array : ",arr)
print("splitted array : ",newarr)
print("---------")