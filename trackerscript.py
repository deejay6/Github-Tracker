import requests
import json
import csv
import datetime

fields = []

base_url = "https://api.github.com"

with open('database.csv', 'rb') as f:
    reader = csv.reader(f)
    user = list(reader)
print user

z = len(user)
print z


def api_call():
    with open('database.csv', 'rb') as f:
        read_data = csv.reader(f)
        used = list(read_data)
        x = len(used)
    for i in range(0, x):
        request_url = (base_url + '/repos/%s/%s/stats/contributors') % (used[i][0], used[i][1])
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


def append_data():
    with open('database.csv', 'a') as f0:
        writer = csv.writer(f0)
        writer.writerow([])
        writer.writerow(fields)
    api_call()


def validate_before_add():
    flag = 0
    for j in range(0, z):
        if new_username == user[j][0] and new_repo == user[j][1]:
            print "User : " + user[j][0] + " ,and repo :" + user[j][1] + " ,already exists, falling back !"
            api_call()
            flag = 1
            break
    if flag == 0:
        fields.append(new_username)
        fields.append(new_repo)
        append_data()


new_username = raw_input("Enter username to add : ")
new_repo = raw_input("Enter repo to be linked : ")
validate_before_add()
