import numpy as np

file = open("sample2.txt", "w+")

#Q4. Divide numpy.array 3 based on rows. 
# square each elements and merge them based on the original array's rows
arr = np.arange(2, 20, 2).reshape((3,3))
print(arr)

s1 = np.vsplit(arr, 3)
print(s1)
s2 = np.square(s1)
print(s2)
s3 = np.squeeze(s2, axis= 1)
print(s3)
result_arr = np.vstack((arr, s3))
print(result_arr)
content1 = str(result_arr)
file.write("Q.4\n")
file.write(content1)
file.write("\n\n")

#Q.5
#Create numpy.array that has 0deg, 30deg, 60deg, 90deg and find 
# sin, cos, tan of each degrees. 

arr2 = np.arange(0, 91, 30)
print(arr2)

lst = []
lst.append(np.sin(arr2*np.pi/180))
lst.append(np.cos(arr2*np.pi/180))
lst.append(np.tan(arr2*np.pi/180))

file.write("Q.5\n")
for value_lst in lst:
    for value in value_lst:
        if value > 999999999:
            print("INF")
            continue;
        print(value)
        content2 = str(value) 
        file.write(content2)
        file.write("\n")
    print()
    file.write("\n")

#Q6. By using numpy.array, printout the pattern 
# 0 1 0 1 0 1 0
# 1 0 1 0 1 0 1
# 0 1 0 1 0 1 0
# 1 0 1 0 1 0 1
# 0 1 0 1 0 1 0
# 1 0 1 0 1 0 1
# 0 1 0 1 0 1 0

arr3 = np.zeros((7,7), dtype = int)
arr3[::2, 1::2] =1
arr3[1::2, ::2] =1
for row in range(7):
    for col in range(7):
        print(arr3[row, col], end=" ")
    print()

file.write("Q.6\n")
content3 = str(arr3) 
file.write(content3)

file.close()