n= int(input("Enter the number of names you want this algorithm to apply: "))
j=0
while j!=n:
    name = input("Enter name of the person: ")
    list1 = list(name)
    for index,i in enumerate(list1):
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" in list1:
            list1[index]="oodle"
    str1 = ''.join(list1)
    print(str1)
    j=j+1
