import pandas as pd
from IPython.display import display

Patient_info = {
    'Patient_Name' : ['John', 'Alice', 'Bob', 'Eve'],
    'Age' : [2, 6, 7,4],
    'Date_of_appointment' : ['06-01-2025','08-01-2025','10-01-2025','12-01-2025'],
    'Patient_id' : ['001','002','003','004']
}
Patient_df = pd.DataFrame(Patient_info)
print("Patient Data: ")
print(Patient_df)

drug_quantity = {
    'drug_name' : ['dolo650','paracetamol','myospas','sinarest'],
    'quantity' : [100, 200, 300, 400],
    'Patient_id' : ['002','004','005','006']
}
drug_df = pd.DataFrame(drug_quantity)
print("\nDrug Data: ")
print(drug_df)

display(Patient_df.merge(drug_df,on='Patient_id',how='inner'))

display(Patient_df.loc[Patient_df['Age'] <6])