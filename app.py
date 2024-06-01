import numpy as np

# a=np.array(range(1,10))
# b=np.arange(1,10,0.1)
# print(a)
# print(b)

# a=np.zeros((3,4))
# print(a)
# a=np.ones((3,4))
# print(a)
# a=np.arange(0,10,1).reshape(2,5)
# print(a)
# a=a.reshape(5,2)
# print(a)

import numpy as np
import random
"""
linspace
arange
reshape
np.zeros((2,3))
np.ones((2,3))
np.full((2,3),100)
a.min(axis=0)
a.max(axis=1)
a.sum(axis=0)
np.insert(a,1,4,axis=0)
np.linalg.solve(a,b)
np.linalg.det(b)
np.append(a,b)
np.append(a, np.array([[2, 3, 4, 5, 6]]), axis=0)
np.matmul(a,b)
a=np.full((2,4),25)
a=np.eye(4)

"""

# import numpy as np
# import random
# print(np.insert(a,1,4,axis=0))
# print(np.insert(a,1,4,axis=1))
# print(np.random.randint(0,10,size=10).reshape(5,2))
# a=np.random.rand(5,2)
# a=np.random.randint(0,10,size=10)
# print(a)
# a=a.reshape(5,2)
# print(a)
# a=a.flatten()
# print(a)
# a=a.reshape(2,5)
# print(a)
# a = np.append(a, np.array([[2, 3, 4, 5, 6]]), axis=0)
# print(a)
# a=np.full((2,4),25)
# print(a)
# a=np.eye(4)
# print(a)












import numpy as np
import random


a=np.array([[2,3],[4,5]])
print(a)
a=np.random.randint(0,10,size=16).reshape(4,4)
b=np.random.randint(0,10,size=16).reshape(4,4)
# print(np.matmul(a,b))
# print(a)
print(b)
b=np.insert(b,1,np.array([[1,2,3,4]]),axis=0)
print(b)
b=np.insert(b,4,np.array([[1,2,3,4,5]]),axis=1)
print(b)
print( )
b=np.append(b, np.array([[1],[2],[3],[4],[5]]), axis=1)
print(b)
b=np.insert(b,4,np.array([[1],[2],[3],[4],[5]]), axis=1)
print(b)
b=np.insert(b, 2,2, axis=1)
print(b)
b=np.insert(b, 2,2, axis=0)
print(b)



# a=np.random.rand(2,3)
# print(a)
# a=a.flatten()
# print(a)

