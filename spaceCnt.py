'''write a code to find  more than one space in a row between words from a string '''

str4=input("Enter a string to find the frequency occurence of characters")
cnt = 1
space = " "
i = 0

for i in range (len(str4)):
    if str4[i]  == space and str4[i+1] == space :
        cnt = cnt + 1
        pos = i
        if cnt > 1:
            print("the entered string has more than one space in a row")
        else:
            print("No space ")


