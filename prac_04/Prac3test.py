#numbers = [3, 1, 4, 1, 5, 9, 2]

#for counter in numbers:
#    print(counter)

#try:
#    print(numbers[9])
#except IndexError:
#    print("List has no such index.")

#del numbers[-1]
#print(numbers)

#numbers.remove(1)
#print(numbers)

#text = "Python"
#print(text[0:-4])

url_string = "?name=Bob&age=99&day=Wed"

url_string1 = url_string[1:]

url_string2 = url_string1.split('&')

url_string4 = []

for counter in range(len(url_string2)):
    url_string3 = url_string2[counter].split('=')
    url_string4.append(url_string3)

print(url_string4)