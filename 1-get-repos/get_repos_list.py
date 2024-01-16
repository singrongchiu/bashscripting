import requests
import json
import subprocess
import heapq

class MyGit(object):
    stars = 0
    name = ""
    ssh_link = ""
    def __init__(self, val, name, ssh_link):
        self.stars = val
        self.name = name
        self.ssh_link = ssh_link
    def __lt__(self, other):
        a = self.stars
        b = other.stars
        return a < b
    def __eq__(self, other): 
        if not isinstance(other, MyGit):
            return NotImplemented
        return self.name == other.name and self.ssh_link == other.ssh_link
    def __repr__(self):
         return "<MyGit [%d,%s,%s]>" % (self.stars, self.name, self.ssh_link)
    def __str__(self) -> str:
        return "<MyGit [%d,%s,%s]>" % (self.stars, self.name, self.ssh_link)

all_pages = 10
heap = []

file = open("1-output.txt", 'r+')
lines = file.readlines()
for line in lines:
    comma_separated = line.strip().split(",")
    newItem = MyGit(int(comma_separated[0]), comma_separated[1], comma_separated[2])
    if heap.__contains__(newItem):
        continue
    else:
        heap.append(newItem)

file.close()

for i in range(all_pages):
    q = "q=language:java&sort=stars&order=desc&per_page=100&page=" + str(i)
    # q = "q=language:java&sort=stars&order=desc&per_page=100&page=1&stars%3A>6000"
    url = "https://api.github.com/search/repositories?" + q

    print(url)
    r = requests.get(url)
    del url
    response = json.loads(r.text) 
    del r
    urlname_lst = []
    urlname_lst = [(e['ssh_url'], e['name'], e['html_url'], e['stargazers_count']) for e in response['items']]
    del response

    for tupleUrl in urlname_lst:
        starcount = int(tupleUrl[3])
        name = tupleUrl[1]
        ssh_link = tupleUrl[0]
        newItem = MyGit(starcount, name, ssh_link)
        if heap.__contains__(newItem):
            heap.remove(newItem)
            heap.append(newItem)
            continue
        else:
            heap.append(newItem)

    del urlname_lst
    heapq.heapify(heap)
    nlargestlist = heapq.nlargest(1000, heap)

    heap = nlargestlist

fileOut = open("1-output.txt", 'w')
for item in nlargestlist:
    fileOut.write("%d,%s,%s\n" % (item.stars, item.name, item.ssh_link))

fileOut.close()