# Write a Python function that takes a list of words and returns the length
# of the longest one.
input_list = []
limit = int(input("Enter Your List Length: "))
max_length = 0
for i in range(limit):
    input_list.append(input("Enter {} Element for List: ".format(i+1)))
    if len(input_list[i])>max_length:
        max_length = len(input_list[i])
print("Length Of longest Word: {}".format(max_length))

