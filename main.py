# Create your own code here
def get_matrix():
    #gets rows and columns for matrix
    print("\n<-----New Matrix----->")
    rows = int(input("Enter rows: "))
    columns = int(input("Enter columns: "))

    #create empty matrix (2d array)
    #create a new row with values of zero for however many columns there are in each row
    matrix = [[0] * columns for _ in range(rows)]
    #print empty matrix for visualization of size of matrix
    print(f"Empty Matrix: {matrix}")

    #iterate through and add values to matrix
    for i in range(rows):
        for j in range(columns):
            #loop through and add values how we read a book, left to right, top to bottom
            matrix[i][j] = int(input(f"Enter int row value {i} column value {j}: "))
    #final version of matrix
    return matrix


# takes two matrices as parameters, verifies that they can be added together, adds them together, and returns the sum.
def add_matrix(matrix1, matrix2):

    #check if matrices can be summed if not terminate program and return none
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrix size is incorrect")
        return None

    #create new matrix to become the added matrix
    rows = len(matrix1)
    columns = len(matrix1[0])
    matrix = [[0] * columns for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            #same logic as last time except adding together each position into new matrix
            matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    print(f"\nSUM: {matrix}")
    return matrix

if __name__ == "__main__":
    matrix1 = get_matrix()
    matrix2 = get_matrix()
    print("\n<----Filled Matrices----->")
    print(f"Matrix One: {matrix1}")
    print(f"Matrix Two: {matrix2}")
    add_matrix(matrix1, matrix2)