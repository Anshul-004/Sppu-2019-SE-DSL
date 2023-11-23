def partition(array, low, high):

	pivot = array[high]
	i = low - 1

	for j in range(low, high):

		if array[j] <= pivot:
			i = i + 1
			(array[i], array[j]) = (array[j], array[i])

	(array[i + 1], array[high]) = (array[high], array[i + 1])
	return i + 1

def quickSort(array, low, high):
	if low < high:
		pi = partition(array, low, high)
		
		quickSort(array, low, pi - 1)
		quickSort(array, pi + 1, high)

def display(percent):
	for i in range(len(percent)-1,4,-1):
		print(percent[i])

#main code
print("\t ***** PRACTICAL - 07 *****")
n = int(input("Enter No. of students : "))
percent = []
for i in range(n):
	mks=float(input("Enter percentage of student "+str(i+1)+" : "))
	percent.append(mks)

size = len(percent)
quickSort(percent, 0, size-1)

print("Sorted Array using quick sort is :", percent)
print("Top 5 scores are : ") 
display(percent)