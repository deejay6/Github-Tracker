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
s = []

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

            f.writerow([user[i][0], user[i][1], str(contributor), str(week), str(commits), str(add), str(delete)])
    with open('combined_file1.csv', 'wb') as outcsv:
        writer = csv.DictWriter(outcsv, fieldnames=['Name', 'Repo', 'Contributor', 'Week', 'Number Of Commits', 'Number Of Lines Added', 'Number Of Lines Delted'], delimiter=' ')
        writer.writeheader()
        with open(name + ".csv", 'rb') as incsv:
            reader = csv.reader(incsv)
            for i in reader:
                s.append(i)
        print s
        for i in range(0, len(s)):
            writer.writerow({'Name': s[i][0], 'Repo': s[i][1], 'Contributor': s[i][2], 'Week': s[i][3], 'Number Of Commits': s[i][4],'Number Of Lines Added': s[i][5],'Number Of Lines Delted' :s[i][6]})


def clear_files():
    f = open(name + ".csv", "w")  # clear current output.csv
    f.truncate()
    f.close()

clear_files()
api_call()
