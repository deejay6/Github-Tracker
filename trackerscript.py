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
print z


def api_call():
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
            week = datetime.datetime.fromtimestamp(
                int(item['weeks'][-1]['w'])
            ).strftime('%Y-%m-%d')

            contributor = item['author']['login']
            commits = item['weeks'][-1]['c']

            f.writerow(["Name : " + user[i][0] + ", " + "\n Repo : " + user[i][1] +
                        ",\n Contributor : " + str(contributor) + ",\n Week : " + str(week) +
                        ",\n Total Number of Commits : " + str(commits)])
            f.writerow([])


def clear_files():
    f = open("output.csv", "w")  # clear current output.csv
    f.truncate()
    f.close()

clear_files()
api_call()
