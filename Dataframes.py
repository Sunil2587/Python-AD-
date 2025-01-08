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