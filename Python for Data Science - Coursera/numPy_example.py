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
    print
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