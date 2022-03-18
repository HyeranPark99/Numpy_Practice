import numpy as np

# Q1. printing an array which all of the elements value is 3.
arr = np.full((3,4,5), 3)
new_arr = arr
print(arr, "\n")
file = open("sample.txt", "w+")
content = str(new_arr)
file.write(content)


# Q2. file=open("sample.txt", "r")
# content = file.read()
# file.close()
# Print an numpy.array consisted of random numbers.
# The range of elements value is integer (-50~50).
# Sort it by row.
# Reshape it to 1 dimension array and sort it.

arr2 = np.random.randint(-50, 50, (4,5))
print(arr2)
print(np.sort(arr2, axis=0))
print(np.sort(arr2, axis = None))

r1 = np.sort(arr2, axis=0)
r2 = np.sort(arr2, axis = None)

content1 = str(r1)
content2 = str(r2)
file.write("\n\n")
file.write(content1)
file.write("\n\n")
file.write(content2)

#Q3. Print mean, standard deviation, median
py_list = [
    np.full(3,8), 
    np.array([33, -15, 26]),
    np.linspace(17, 26, 3)
]

result_arr = []
for i in py_list:
    result_arr.append(np.mean(i))
    result_arr.append(np.std(i))
    result_arr.append(np.median(i))
print(result_arr)
file.write("\n\n")
r3 = str(result_arr)
file.write(r3)

file.close()