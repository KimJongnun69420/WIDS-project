import numpy as np
import numpy as np

def numpy_spiral_order(matrix):
    
    result = []
    if matrix.size == 0:
        return result

    top, bottom = 0, matrix.shape[0] - 1
    left, right = 0, matrix.shape[1] - 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top, col])
        top += 1

        for row in range(top, bottom + 1):
            result.append(matrix[row, right])
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom, col])
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row, left])
            left += 1

    return result




def find_greater (arr,mean)-> int:
    for i in range (5) :
        for j in range (5):
            if arr[i][j]>mean:
                return arr[i][j]
    return mean

        
# to make a random shape 
rand_array=np.random.randint(1,100,(5,5))#you can set the value as a tuple or a list
print (rand_array)
print()
print(f"The middle element of the matrix is {rand_array[2,2]}")
print ()
mean=rand_array.sum(axis=1)/5
print (f"the mean of each row is \n {mean}")#printing the mean of each row in the array
print()
overall_mean=rand_array.sum()/25
print(f" the overall mean is {overall_mean}")

find=find_greater(rand_array,overall_mean)
print()
print(find)
new_array=np.full((5,5),0)

if find==overall_mean:
    new_array=np.full((5,5),find)
else :

    for i in range(5):
        for j in range (5):
            if rand_array[i][j]>overall_mean:
                new_array[i][j]=rand_array[i][j]
            else:
                new_array[i][j]= find
print()
print(f" the array with the same elements as the original array is and also greater than the mean is \n {new_array}")

list=numpy_spiral_order(rand_array)
print()
print("the spiral order is")
for i in list:
    print (i, end=' ')
    






