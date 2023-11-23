def bubble(percent):
	for i in range(len(percent)-1):
		for j in range(len(percent)-i-1):
			if percent[j]>percent[j+1]:
				percent[j],percent[j+1]=percent[j+1],percent[j]

	return percent

def selectionSort(array, size):
	
	for ind in range(size):
		min_index = ind

		for j in range(ind + 1, size):
			
			if array[j] < array[min_index]:
				min_index = j
		
		(array[ind], array[min_index]) = (array[min_index], array[ind])

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
	ch=int(input("1. Selection Sort, 2.Bubble Sort and Top 5 Scores, 3.Exit "))

	if ch==1:
		print("\nResult of Selection Sort is : ",selectionSort(percent,n))
	elif ch==2:
		print("\nResult of Bubble Sort is : ",bubble(percent))
		print("Top 5 Scores are : ")
		display(percent)
	elif ch==3:
		print("\t***** TERMINATED SUCCESSFULLY *****")
		break
	else:
		print("Invalid Choice")
