import requests
import json
import csv
import datetime

base_url = "https://api.github.com"

with open('database.csv', 'rb') as f:
    reader = csv.reader(f)
    user = list(reader)
print user

z = len(user)
date = datetime.datetime.now()
name = date.strftime("%d-%m-%Y")

print z


def api_call():
    for i in range(0, z):
        request_url = (base_url + '/repos/%s/%s/stats/contributors?'
                                  'client_id=6ffcb5c447f054babff3&client_secret='
                                  '6b889df62e3474104a6b23d949c0c55f86a8e50a') % (user[i][0], user[i][1])
        print 'GET request url : %s' % request_url
        data = requests.get(request_url).json()
        with open('repo_data.json', 'w') as outfile:
            json.dump(data, outfile)

        f = open('repo_data.json')
        data = json.load(f)
        f.close()
        f = csv.writer(open(name + '.csv', 'a'))

        for item in data:
            week = datetime.datetime.fromtimestamp(
                int(item['weeks'][-1]['w'])
            ).strftime('%Y-%m-%d')

            contributor = item['author']['login']
            commits = item['weeks'][-1]['c']
            add = item['weeks'][-1]['a']
            delete = item['weeks'][-1]['d']

            f.writerow(["Name : " + user[i][0] + ", " + "\n Repo : " + user[i][1] +
                        ",\n Contributor : " + str(contributor) + ",\n Week : " + str(week) +
                        ",\n Total Number of Commits : " + str(commits) + "\n Lines added : " + str(add)
                        + "\n Lines deleted : " + str(delete)])
            f.writerow([])


def clear_files():
    f = open("output.csv", "w")  # clear current output.csv
    f.truncate()
    f.close()

clear_files()
api_call()
