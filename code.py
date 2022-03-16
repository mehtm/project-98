def dataSwap():
    file1=input("enter the file 1")
    file2=input("enter the file 2")

    with open(file1,'r') as a:
        dataA= a.read()

    with open(file2,'r') as b:
        dataB= b.read()

    with open(file1,'w') as a:
        a.write(dataB)

    with open(file2,'w') as b:
        b.write(dataA)

    print("your data in the file is swapped")

dataSwap()

