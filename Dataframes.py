import pandas as pd
screen_time = [2,4,5,6]
sleep_hours =[3,4,5,3]
practice_hours=[2,3,4,3]
st_name=["sunil","jc","satwik","tarun"]
dict1 = {
    "screen_time":screen_time,
    "sleep_hours":sleep_hours,
    "st_name":st_name,
    "practice_hours":practice_hours,
    }
print(dict1)

df = pd.DataFrame(dict1)
print(df)


#list comprehesion

#list =[1,2,3,4]
#res=[i+1 for i in range(1,20)]
#print(res)

list =[1,2,3,4,5,6,7,8,9]
res=[i for i in list if i%2==0]
print("even number",res)
od=[i for i in list if i%2 !=0]
print("odd number:",od)
# lower and upper case letters in list
words =["Lower","W","PYTHON"]
lower =[i.lower() for i in words]
print(lower)
words =["ood","fss","sunil"]
lower =[i.upper() for i in words]
print(lower)

# creating dictionary  comprehension from mtwo lists

keys =["name","age","city"]
values =["sunil",19,"Hyd"]
list =[i for i in list]
dict ={k:v for k,v in zip(keys,values)}
print(dict)

# tuple  comprehension 

import math
num = [1,4,16,9,25]
sq=tuple(math.sqrt(i) for i in num)


print(sq)


# Give me the produt details with the price less then 500 use of dict comp

products =[
    {"name":"laptop","price":800},
     {"name":"tablet","price":500},
      {"name":"phone","price":400}
]

affordable_products = {i["name"]:i["price"] for i in products if i["price"]<500}
print(affordable_products)




