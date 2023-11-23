
def insertionsort(arr):

	for i in range(1, len(arr)):

		key = arr[i]

		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key
	return arr

def shellsort(array, n):

    # Rearrange elements at each n/2, n/4, n/8, ... gaps
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap

            array[j] = temp
        gap //= 2

    return array

def display(percent):
	for i in range(len(percent)-1,4,-1):
		print(percent[i])

#main code

#take user input and store in list
n = int(input("Enter No. of students : "))
percent = []
for i in range(n):
	mks=float(input("Enter percentage of student "+str(i+1)+" : "))
	percent.append(mks)

while(1):
	print("\n\t***** Sorting Menu *****")
	ch=int(input("1. Insertion Sort, 2.Shell Sort and Top 5 Scores, 3.Exit "))

	if ch==1:
		print("\nResult of Insertion Sort is : ",insertionsort(percent))
	elif ch==2:
		print("\nResult of Shell Sort is : ",shellsort(percent,n))
		print("Top 5 Scores are : ")
		display(percent)
	elif ch==3:
		print("\n\t***** TERMINATED SUCCESSFULLY *****")
		break
	else:
		print("Invalid Choice")
