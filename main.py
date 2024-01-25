import requests
from bs4 import BeautifulSoup
import pandas as pd
import os 


#------------------------
csv_name = "BSAIF22.csv"
#------------------------


path_roll_numbers = os.path.join("source_csv", csv_name)
roll_number = pd.read_csv(path_roll_numbers)
roll_numbers = roll_number["roll_numbers"].values

url = "https://portals.au.edu.pk/auresult/"

headers = {
    "Host": "portals.au.edu.pk",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0"
}

data_list = []

for i, roll in enumerate(roll_numbers):
    subjects = {}
    print("\nFetching Result of: ", roll)
    
    subjects["name"] = roll_number.iloc[i]["names"]
    subjects["roll_number"] = roll_number.iloc[i]["roll_numbers"]
    
    payload = {
        "__EVENTTARGET": "",
        "__EVENTARGUMENT": "",
        "__VIEWSTATE": "",
        "__VIEWSTATEGENERATOR": "",
        "ctl00$AUContent$txt_regid": str(roll),
        "__ASYNCPOST": "true",
        "ctl00$AUContent$btnShow": "Search Result"
    }
    
    response = requests.post(url, headers=headers, data=payload)
    print(response.status_code)
    
    soup = BeautifulSoup(response.text, 'lxml')
    # Find all tables on the page
    tables = soup.find_all('table')
    

    # Iterate through all tables
    if len(tables) >2:
        for row in tables[2].find_all('tr')[2:]:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            if len(cols)>1:
                subjects[cols[0]] = cols[-1]
            subjects["gpa"] = cols[0].split("\n")[-1]
    else:
        pass

    data_list.append(subjects)
    # print(subjects)
    

dataframe = pd.DataFrame(data_list)
dataframe.to_csv(os.path.join("scrapped_result", csv_name.split(".")[0]+"-result.csv"), index=False)

