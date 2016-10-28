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

