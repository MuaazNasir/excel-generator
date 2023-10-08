import pandas as pd
import requests
URL = "https://hub.dummyapis.com/employee?noofRecords=100&idStarts=100"
r = requests.get(URL)
r.raise_for_status()
if r.status_code == 200 and r.text :
    rData = r.json()
    df = pd.DataFrame(rData)
    
    file_name = "emloyees.xlsx"
    writer = pd.ExcelWriter(file_name,engine="xlsxwriter")
    
    df.to_excel(writer,sheet_name="Employees Data",index=False)
    writer._save()
    
    print(f"created a file name '{file_name}'")
else :
    print("error occured")