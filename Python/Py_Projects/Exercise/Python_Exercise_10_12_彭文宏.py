# %% 
from encodings import utf_8
import json
fltred_list = []
with open('Questions/Exercise_10/drugstore.json','r',encoding='utf_8') as jsonFile:
    content = json.load(jsonFile)
    for row in content:
        if row[1] == '新北市': #and row['機構狀態'] == '開業':
            json.dump(fltred_list,row,ensure_ascii=False)
            print(fltred_list)

# %%
