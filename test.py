print("hello  hi")

a="test"
b="lab"
c="ing"
print(a+c+ b)


print("list and dictionary are mutable")
print("tuple and set are immutable")


# adding (or) concatenation of strings

str1="hello"
str2="world"

print(str1+" "+str2)

# * operation is used to repate  the value in string
print(str1*3)


# finding the lenght of string

print(len(str1))


#strin indexing and slicing

str1="sub string test"
sub=str1[3:6]
print(sub)

# indexing [ 3:6] indicate starting form 3 and ending n-1 so the out put will be starting from index 3 to 5


## striping
# removing extra spaces

str1="  hello"
print(str1.strip())

#split

str1 ="helo world removing extra spaces"
print(str1.split())


students = {
    1: {"name": "google", "age": 14},
    2: {"name": "deloite", "age": 20},
    3: {"name": "sunil", "age": 19},
    4: {"name": "pwc", "age": 12},
    5: {"name": "ss", "age": 89},
}

for student_id, details in students.items():
    print(f"Student ID: {student_id}, Name: {details['name']}, Age: {details['age']}")
