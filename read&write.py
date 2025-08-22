# so we will create a file named file.txt and write some content to it first

with open("file.txt", "r") as infile:
    content = infile.read()

# This Script will Modify the content(make it uppercase)

modified_content = content.upper()

# Write to a new file

with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("Modified content has been written to output.txt")
