import requests, json, csv
import pandas

BASE_URL = "https://api.github.com"

username = ['rk2810', 'deejay06', 'princeyadav05']
repo = ['gemini', 'SpyChat-Application', 'spy_chat']


for i in range(0, len(username)):
    request_url = (BASE_URL + '/repos/%s/%s/stats/contributors') % (username[i], repo[i])
    print 'GET request url : %s' % request_url
    data = requests.get(request_url).json()
    with open('repo_data.json', 'w') as outfile:     # create a json data dump
        json.dump(data, outfile)

# load the json data dump to a csv file

f = open('repo_data.json')
data = json.load(f)
f.close()

f=csv.writer(open('output.csv','wb+'))

for item in data:
    f.writerow([item['weeks'], item['total']] + item['author'].values())
