predict={
    1: {"name": "Sunil","study_time":"4hr","practically_working_hrs":2},
    2: {"name": "Tarun","study_time":"4hr","practically_working_hrs":3},
    3: {"name": "Satwik","study_time":"4hr","practically_working_hrs":4},
    4: {"name": "JC","study_time":"4hr","practically_working_hrs":5},

}

for student ,details in predict.items():
    print(f"Students :{student}, Name:{details['name']},Study_Time:{details['study_time']},Practically_Working in hr:{details['practically_working_hrs']}" )