import requests
import json
import csv

base_url = "https://api.github.com"

with open('database.csv', 'rb') as f:
    reader = csv.reader(f)
    user = list(reader)
print user

z = len(user)
print z

for i in range(0, z):
    request_url = (base_url + '/repos/%s/%s/stats/contributors') % (user[i][0], user[i][1])
    print 'GET request url : %s' % request_url
    data = requests.get(request_url).json()
    with open('repo_data.json', 'w') as outfile:
        json.dump(data, outfile)
    f = open('repo_data.json')
    data = json.load(f)
    f.close()
    f = csv.writer(open('output.csv', 'a'))

    for item in data:
        f.writerow([user[i][0], user[i][1], item['weeks'], item['total']])
        f.writerow(\n)