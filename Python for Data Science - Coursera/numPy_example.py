import numpy as np

if __name__ == '__main__':
    matrix1 = np.array([[1,2,3],[4,5,6]])
    print(matrix1)
    print(matrix1.shape)  # This print out (2,3) means that this is a 2x3 matrix
    matrix2 = np.arange(1,10,1, np.int32)  # This create an 1x9 array, with entries are integer type int32bits from 1 to 9
    print(matrix2)
    matrix2 = matrix2.reshape((3,3))  # This change the matrix 2 to 3x3 matrix, with entries unchanged
    print(matrix2)
    matrix3 = np.linspace(1,5,50)  # Create a matrix 1x50 with element is evenly distributed from 1 to 5, inclusive
    print(matrix3)
    print(matrix3.shape)  # Matrix3 is a 1x50 matrix
    matrix3 = matrix3.reshape((5,10))
    print(matrix3)
    # Using resize will change both SHAPE AND SIZE of the matrix, using reshape can only change shape, it happens on the memory, so
    # we need to check to make sure there is no reference to the matrix in the code
    # matrix3.resize(5,5)  # Cannot work since there is reference to the matrix before
    matrix4 = np.linspace(1,5,50)
    print(matrix4)  # Now matrix4 is a 1x50 matrix
    matrix4.resize(5,5)  # Now matrix4 is 5x5 matrix, the last unused elements it cut down.
    print(matrix4)
    print("=========================================================================")
    matrix5 = np.array([[1,2],[3,4]], order="C")
    print(matrix5)
    matrix6 = np.array([[1,2],[3,4]], order="F")
    print(matrix6)
#     Both matrix above appear to be the same, but different in storing in memory. This difference appear when resize them.
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    matrix5.resize((2,1))
    print(matrix5)
    matrix6.resize((2,1))
    print(matrix6)
#     Both matrix now become 2x1 matrix. But matrix5 entries will be the first 2 input list, (1,2) and the matrix6 will be the first
#   element of each input lists (1,3).
#   If there is more entries needed, the extra entries will be filled with 0 when using resize, it will be a repeat of the array
#   when using reshape
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    matrix5.resize(2,3)
    matrix6.resize(2,3)
    print(matrix5)
    print(matrix6)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    # Create a 0 matrix with size 2x3
    matrix7 = np.zeros((2,3))
    print(matrix7)
    # Create an identity matrix size 5x5
    matrix8 = np.eye(5)
    print(matrix8)
#    Create a diagonal matrix from a 1D array. It will return a 2D array with the element of the 1D array along the diagonal.
    matrix9 = np.arange(9)
    matrix10 = np.diag(matrix9)
    print(matrix10)
    # Create a matrix by repeating.
    # Create a matrix with the original one repeated
    matrix11 = np.array([1,2,3]*3).reshape(3,3)
    # Create a matrix with the element in the original matrix repeated 3 times before moving on to new element.
    matrix12 = np.repeat([1,2,3],3).reshape(3,3)
    print(matrix11)
    print(matrix12)
    print("============================================================================")
    print("Basic stacking")
    print("Stack matrix on top of each other to produce new matrix")
    print(np.vstack([matrix11,matrix12]))
    print("Stack matrix side by side of each other to produce new matrix")
    print(np.hstack([matrix11,matrix12]))
    print("============================================================================")
    print("Basic operations")
    print(matrix1)
    matrix2 = np.arange(6).reshape(2,3)
    print(matrix2)
    print("Matrix adding, adding matrix1 and matrix2")
    matrix4 = matrix1 + matrix2
    print(matrix4)
    print("Matrix multiplication, multiply matrix1 and matrix2")
    print("This multiplication is not matrix multiplication, it is just multiply the element together")
    matrix4 = matrix1 * matrix2
    print(matrix4)
    print("This is the dot product of 2 matrices")
    matrix3 = np.reshape(matrix2,(3,2))
    print(matrix1)
    print(matrix3)
    matrix4 = matrix1.dot(matrix3)
    print(matrix4)
    print("Creating the transpose of an array")
    print(matrix1)
    print(matrix1.T)
    print("Checking on the type stored in the matrix")
    print(matrix1)
    print(matrix1.dtype)
    print(matrix1.argmax())
    print(matrix1.max())
    print(matrix1.sum())
    print(matrix1.std())
    print(matrix1.mean())
    matrix1 = matrix1.astype("f8")
    print(matrix1.dtype)
    print(matrix1)
    print("===============================================================================")
    print("Indexing/Slicing")
    matrix1 = np.arange(13)**2
    print(matrix1)
    matrix2 = np.arange(36).reshape(6,6)
    print(matrix2)
    print("Get the value from the 2D array")
    value22 = matrix2[2,2]
    print("Value at 3rd row, 3 col col: "+str(value22))
    print("Get the value of a row or cols entirely")
    value_row2 = matrix2[1,]
    print("Row 2:"+str(value_row2))
    print("Get the value of a row or cols in a range")
    value_col2_24 = matrix2[2:4,1]
    print("Col 2, value from row 2 to 4 exclusively: "+str(value_col2_24))
    print("Get every second data from that last row:")
    value_last_e2nd = matrix2[-1,::2]
    print(value_last_e2nd)
    # We can use the comparison inside the square bracket. It will return an array with elements match the requirement
    # from the original array.
    print("Get all element of the array that is > 25:")
    matrix3 = matrix2[matrix2>25]
    print(matrix3)
    print("Get all element of the array that is even:")
    matrix3 = matrix2[matrix2%2==0]
    print(matrix3)
    print("Set all the element that is not even to be 99, this will modified the matrix")
    matrix2[matrix2%2!=0] = 99
    print(matrix2)
    print("===============================================================================")
    print("Copying data")
    print("Create a matrix contain first 3 cols and rows of matrix2")
    matrix4 = matrix2[:3,:3]
    print(matrix4)
    print("Set all element in this matrix to be 0")
    matrix4[:] = 0
    print(matrix4)
    print(matrix2)
    # As we can see above, the original matrix2 ALSO BE CHANGED WHEN WE CHANGED matrix4.
    # If we want to copy a matrix and let the original matrix unchanged, we have to use method copy
    matrix5 = matrix2.copy()
    print(matrix5)
    matrix5[:] = 0
    print(matrix5)
    print(matrix2)
    matrix6 = matrix2.copy()[:3,:3]
    matrix6[:] = 9
    print(matrix2)
    print(matrix6)
    print("===============================================================================")
    print("Iterating over an array")
    print("Create a 4x3 array with number from 0 to 9")
    matrix10 = np.random.randint(0,10,(4,3))
    print(matrix10)
    matrix_a = np.arange(1,10,1).reshape(3,3)
    matrix_b = np.random.randint(0,10,(3,3))
    print(matrix_a+matrix_b)
