import numpy as np

output = np.array([[1,1,1,1,1],[1,0,0,0,1],[1,0,9,0,1],[1,0,0,0,1],[1,1,1,1,1]], dtype= 'int16')
output_2 = np.ones((5,5))
output_2[1,1:4] = 0
output_2[3,1:4] =0
output_2[2,1:4] = [0,9,0]

print(output_2 )