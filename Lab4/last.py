# Python3 program to implement
# the above approach

# Utility function to find cross product
# of two vectors
def CrossProduct(A):
    X1 = (A[1][0] - A[0][0])
    Y1 = (A[1][1] - A[0][1])
    X2 = (A[2][0] - A[0][0])
    Y2 = (A[2][1] - A[0][1])
    return (X1 * Y2 - Y1 * X2)

# Function to check if the polygon is
# convex polygon or not
def isConvex(points):
    N = len(points)
    prev = 0
    curr = 0
    for i in range(N):
        temp = [points[i], points[(i + 1) % N],
            points[(i + 2) % N]]
        curr = CrossProduct(temp)

        if (curr != 0):
            if (curr * prev < 0):
                return False
            else:
                prev = curr
    return True

# Driver code
if __name__ == "__main__":
    points = [ [0, 0], [10, 0],[10, 9], [9, 9],[9, 10], [0, 10] ]
    if (isConvex(points)):
        print("Yes")
    else:
        print("No")

# This code is contributed by SURENDRA_GANGWAR


# print(cross_product([[0, 0], [10, 0],[10, 9], [9, 9],[9, 10], [0, 10]]))
