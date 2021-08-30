fileOne = input("Input your first file name: ") 
    
with open(f"{fileOne}", "rb") as a:
     file1 = a.read()

fileTwo = input("Input your second file : ") 
    
with open(f"{fileTwo}", "rb") as b:
     file2 = b.read()

fileThree = input("File where you want to merge: ") 
    
with open(f"{fileThree}", "wb") as c:
     output = file1 + file2
     c.write(output)