def take_matrix(m,n):
    out=[]
    for i in range(m):
        row=[]
        for j in range(n):
            element=int(input(f"Enter Element [{i}][{j}] :"))
            row.append(element)
        out.append(row)
    return out

#function to add two matrices
def addition():
                #take no. of rows and columns
    m=int(input("Enter Rows Of Matrix : "))
    n=int(input("Enter Columns Of Matrix : "))
                #take matrices A and B
    print("\n\tMATRIX A")
    A = take_matrix(m,n)
    print("\n\tMATRIX B")
    B = take_matrix(m,n)
                #calculate sum
    result=[]
    for i in range(m):
        row =[]
        for j in range(n):
            row.append(A[i][j]+B[i][j])
        result.append(row)
    return result

#function to subtract two matrices
def subtraction():
                #take no. of rows and columns
    m=int(input("Enter Rows Of Matrix : "))
    n=int(input("Enter Columns Of Matrix : ")) 
                #take matrices A and B
    print("\n\tMATRIX A")
    A = take_matrix(m,n)
    print("\n\tMATRIX B")
    B = take_matrix(m,n)
                #calculate difference
    result=[]
    for i in range(m):
        row =[]
        for j in range(n):
            row.append(A[i][j]-B[i][j])
        result.append(row)
    return result

#function to multiply matrices A and B
def multiplication():
                #take rows and columns of matrix A
    m=int(input("Enter Rows Of Matrix : ")) 
    n=int(input("Enter Columns Of Matrix : ")) 
    print("\n\tMATRIX A")
    A = take_matrix(m,n)
                #Take no. of columns and keep rows = columns of previous matrix
    print("\nNo. of rows are : ",n)
    x=int(input("Enter Columns : ")) 
    print("\n\tMATRIX B")
    B = take_matrix(n,x) 
                #calculate product
    result = []
    for i in range(len(A)):
        collector =[]
        for j in range(len(B[0])):
            temp = []
            for k in range(len(B)):
                temp.append(A[i][k]*B[k][j])
            row = sum(temp)
            collector.append(row)
        result.append(collector)
    return result

#function for transpose
def transpose():
                #take no. of rows and columns
    m=int(input("Enter Rows and Columns Of Matrix : "))
    n=m #as transpose is possible on square matrix only
                #take matrix A 
    print("\n\tMATRIX A")
    A = take_matrix(m,n)
                #find transpose
    result=[]
    for i in range(m):
        row =[]
        for j in range(n):
            row.append(A[j][i])
        result.append(row)
    return result

# Main Code
while (1):
    print("\n\t\t***** MATRIX OPERATIONS *****\n")
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Transpose\n5.Exit\n")
    ch = int(input("Enter Your Choice : "))
    print("")

    if ch == 1:
        W = addition()
        print("\nSum of Matrices A and B is : ")
        for row in W:
            print(row)

    elif ch == 2:
        X = subtraction()
        print("\nDifference of Matrices A and B is : ")
        for row in X:
            print(row)

    elif ch == 3:
        Y = multiplication()
        print("\nProduct of Matrices A and B is : ")
        for row in Y:
            print(row)

    elif ch == 4:
        Z = transpose()
        print("\nTranspose of Matrix A is : ")
        for row in Z:
            print(row)

    elif ch == 5:
        print("\t\t*****TERMINATED SUCCESSFULLY*****\n")
        break

    else:
        print("Invalid Choice\n")