import requests
from bs4 import BeautifulSoup

url = "https://portals.au.edu.pk/auresult/"
search_reg_id = "220958"  # Replace with the actual registration ID

# Define the headers
headers = {
    "Host": "portals.au.edu.pk",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
    # ... (other headers)
}

# Define the payload data dynamically
payload = {
    "__EVENTTARGET": "",
    "__EVENTARGUMENT": "",
    "__VIEWSTATE": "",
    "__VIEWSTATEGENERATOR": "",
    "ctl00$AUContent$txt_regid": search_reg_id,
    "__ASYNCPOST": "true",
    "ctl00$AUContent$btnShow": "Search Result"
}

response = requests.post(url, headers=headers, data=payload)
print(response.status_code)

soup = BeautifulSoup(response.text, 'lxml')

# Find all tables on the page
tables = soup.find_all('table')

# Initialize a set to store unique data
unique_data = set()

# Iterate through all tables
for table in tables:
    # Iterate over each row in the table (skip the header row if necessary)
    for row in table.find_all('tr'):
        # Extract the text from each cell in the row
        # and add it to a list representing that row
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        # Ensure that you have data (ignore empty/invalid rows)
        if cols:
            # Convert the list to a tuple to make it hashable
            row_tuple = tuple(cols)
            unique_data.add(row_tuple)

# Convert the set of tuples back to a list of lists
unique_data_list = [list(row_tuple) for row_tuple in unique_data]

# Now 'unique_data_list' is a list of lists with unique entries
for row in unique_data_list:
    print(row)
