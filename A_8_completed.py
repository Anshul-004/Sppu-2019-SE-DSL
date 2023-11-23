def take_matrix(m, n):
    out = []
    for i in range(m):
        row = []
        for j in range(n):
            element = int(input(f"Enter Element [{i}][{j}] :"))
            row.append(element)
        out.append(row)
    return out


def saddle():
    # take no. of rows and columns
    m = int(input("Enter Rows Of Matrix : "))
    n = int(input("Enter Columns Of Matrix : "))
    # take matrices A and B
    print("\n\tMATRIX A")
    A = take_matrix(m, n)

    for row in range(m):
        min_row = A[row][0]
        col_index = 0

        for col in range(n):
            if (min_row > A[row][col]):
                min_row = A[row][col]
                col_index = col

    k = 0
    for k in range(n):

        if (min_row < A[k][col_index]):
            break
        k += 1
    if k == n:
        print("Value of Saddle Point ", min_row)
        print(f"Index of {min_row} is [{row}][{col_index}]")
        return True

# main

saddle()
