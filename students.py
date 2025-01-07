predict={
    1: {"name": "Sunil","study_time":"4hr","practically_working_hrs":2},
    2: {"name": "Tarun","study_time":"4hr","practically_working_hrs":3},
    3: {"name": "Satwik","study_time":"4hr","practically_working_hrs":4},
    4: {"name": "JC","study_time":"4hr","practically_working_hrs":5},

}

for student ,details in predict.items():
    print(f"Students :{student}, Name:{details['name']},Study_Time:{details['study_time']},Practically_Working in hr:{details['practically_working_hrs']}" )






import pandas as pd
data=[2,3,4,5,6,7,89,0,99]
No_of_studied = data[4:8]
print("No.of hours_studied",No_of_studied)
Age = data[9:13]
print("Studnet_age",Age)
Screen_time = data[3:6]
print("Screen_time",Screen_time)
Data_Frame = pd.DataFrame(data)
print(Data_Frame)