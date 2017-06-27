import requests
import json
import csv

BASE_URL = "https://api.github.com"
Username = raw_input("What is your Github Username? : ")
Repo = raw_input("Repository Name : ")

for line in Username.csv:
    if Username and Repo in line:
        #do something
    elif Repo not in line:
        # append username and repo
    else:
        #append username and repo both

## one file for username.csv and repo.csv
with open('username.csv', 'rb') as f:
    reader = csv.reader(f)
    username = list(reader)
print username

with open('repo.csv', 'rb') as f:
    reader = csv.reader(f)
    repo = list(reader)
print repo

z = len(username[0])
x = username[0]
y = repo[0]
print z

for i in range(0, z):
    request_url = (BASE_URL + '/repos/%s/%s/stats/contributors') % (x[i], y[i])
    print 'GET request url : %s' % request_url
    data = requests.get(request_url).json()
    with open('repo_data.json', 'w') as outfile:     # create a json data dump
        json.dump(data, outfile)

f = open('repo_data.json')
data = json.load(f)
f.close()
f = csv.writer(open('output.csv','wb+'))

for item in data:
    f.writerow([item['weeks'], item['total']] + item['author'].values())