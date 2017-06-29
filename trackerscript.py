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
    add_to_output()
    # exit() >> review


def add_to_output():
    for i in range(0, z):
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
                        ",\n Number of Commits : " + str(commits) + "\n"])

    exit()


def clear_files():
    f = open("output.csv", "w")  # clear current output.csv
    f.truncate()
    f.close()


def validate_before_add():
    clear_files()
    for j in range(0, z):
        if new_username == user[j][0]:
            if new_repo == user[j][1]:
                print user[j][0]
                print "Already exists, falling back !"
                api_call()
            else:
                print "pseudo Append script"
                api_call()
                add_to_output()
        else:
            print "Failed"


new_username = raw_input("Enter username to add : ")
new_repo = raw_input("Enter repo to be linked : ")
validate_before_add()
