#I will test the file.
print('this code is working!')

#I will create the file
strPath = "text.txt"

#I will open the file and save the data to fileObject
fileObject = open(strPath, "w")

#I will write code to the text file
fileObject.write("First Astronaut on the moon\n")
fileObject.write("Neil Armstrong\n")

#I will close the file
fileObject.close()

#I will read the contents of the file
fileObject = open(strPath)

#I will read the fileObject variable
textList = fileObject.readlines()
fileObject.close()

#I will print the contents of the file
for line in textList:
    print(line)

#I will read the first line of the file
firstLine = textList[0]
print(firstLine)

#I will read the second line of the file
secondLine = textList[1]
print(secondLine)

