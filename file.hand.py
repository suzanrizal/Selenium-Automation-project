# f = open("demo.txt", "r")
# print(f.read())
# f.close()

# With With (Reading file)
# with open("demo.txt", "r") as f:
#     # print(f.read())
#     print(f.readline()) # This will read the first line of the file
#     print(f.read(10)) # This will read the next 10 characters


# For writing to a file
with open("demo.txt", "w") as f:
    f.write("\nThis is a new line added to the file.")

with open("demo.txt", "r") as f:
    print(f.read()) # This will read the entire file after writing to it






