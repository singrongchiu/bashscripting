import subprocess

file = open("1-output.txt", 'r+')
lines = file.readlines()
for line in lines:
    comma_separated = line.strip().split(",")

    starcount = int(comma_separated[0])
    name = comma_separated[1]
    ssh_link = comma_separated[2]

    subprocess.run(["bash", "./find_bash.sh", "%s" % (ssh_link), "%s" % (name),
        "%d" % starcount, "2-outputbashcleaned.txt"])