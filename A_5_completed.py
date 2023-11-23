def longest():
    str1 = input("Enter the string : ")
    str=str1+" "
    longest_word = ""
    max_length = 0
    current_word = ""
    current_length = 0

    for word in str:
     
        if word == ' ' or word == str[-1]:
        
            if current_length > max_length:
                max_length = current_length
                longest_word = current_word

            current_word = ""
            current_length = 0
        else:

            current_word += word
            current_length += 1

    return longest_word

def occur():
    str = input("Enter the string : ")
    ch = input("Which character do you want to search in string : ")
    cnt =0

    for char in str:
        if char==ch:
            cnt+=1
            
    print(ch,"Occured", cnt,"times.")
    
def palindrome():
    str=input("Enter String To Check Palindrome : ")
    str1=str[::-1]

    if str1==str: 
        print("It is a Palindrome.")
    else :
        print("It is Not a Palindrome.")

def find_sub():
 
    str = input("Enter the string : ")

    sub_str = input("Enter the Substring to search for : ")


    index = str.find(sub_str)

    if index != -1:
        print(f"The index of the first occurrence of '{sub_str}' is: {index}")
    else:
        print(f"'{sub_str}' not found in the input substring.")

def occur_word():
    str1 = input("Enter the string : ")
    str = str1+" "
    word_list ={}
    current_word= ""

    for word in str:
        if word == ' ' or word ==str[-1]:
            if current_word in word_list:
                word_list[current_word]+=1
            else:
                word_list[current_word] = 1
            current_word = ""

        else:
            current_word+= word
    print("Word --> Occurences")
    for key in word_list:
        print(f'{key} --> {word_list[key]}')


#main code
while (1):
    print("\n\t\t*****STRING OPERATIONS*****\n")
    print("1.Word with longest length\n2.Frequency of a character\n3.Check Palindrome\n4.Index of first substring\n5.Count occurence of each word in string\n6.Exit\n")
    ch = int(input("Enter Your Choice : "))
    print("")

    if ch == 1:
        print("The word with longest length is : ",longest())

    elif ch == 2: 
        occur()

    elif ch == 3:
        palindrome()

    elif ch == 4:
        find_sub()

    elif ch == 5:
        occur_word()

    elif ch == 6:
        print("\t\t*****TERMINATED SUCCESSFULLY*****\n")
        break

    else:
        print("Invalid Choice\n")
