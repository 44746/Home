#George west
#21-10-14
#reversing a string
text = input("Please enter your string: ")
length= len(text)
length=length-1
reverse = ''
for index in range(length,-1,-1):
    reverse = reverse+text[index]
print(reverse)
 
