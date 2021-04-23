import json

with open('accounts/accounts.json') as f:
    accounts_list = json.load(f)
    accounts_list['account'] = []

titles = ["test", "test2", "test3"]
dates = ["test", "test2", "test3"]
links = ["test", "test2", "test3"]

for title, date, link in zip(titles, dates, links):
    
    with open('accounts/accounts.json') as json_file:
        accounts_list['account'].append({
            'title':title,
            'date':date,
            'link':link
        })
   
    with open('accounts/accounts.json', 'w') as f:
        json.dump(accounts_list, f)

