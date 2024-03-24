elements =  [1, 2, 3, 4]

reversed_elements = []

# for i in range(len(elements)):
#     reversed_elements.insert(0, elements[i])

# print(reversed_elements)


index = len(elements) - 1
while index >=0 : 
    reversed_elements.append(elements[index])
    index -= 1

print(reversed_elements)