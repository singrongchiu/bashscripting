import json

file = open("2-outputbashcleaned.txt")

# process by bash files
bash_files = []
bash_file_count = 0
line = file.readline()
while line != "":
    repo = line.strip().split(",")
    print(repo)
    bash_file_count += 1
    print(bash_file_count)
    try: 
        if (repo[4] != ""):
            lines = []
            for i in range(8):
                lines.append(file.readline())
            # print(lines)
            num_lines = int(lines[0].split(",")[1].strip() or 0)
            num_func = int(lines[1].split(",")[1].strip() or 0)
            num_for = int(lines[4].split(",")[1].strip() or 0)
            num_if = int(lines[6].split(",")[1].strip() or 0)
            
            # perma_link = ""
            len_title_plus_2 = len(repo[2]) + 2
            perma_link = "github.com/" + repo[0][15:-4] + "/blob/" + repo[1] + repo[4][len_title_plus_2:]
            # print(perma_link)
            bash_files.append({"name": repo[2], "ssh_link": repo[0], "sha": repo[1], "bash_file_loc":repo[4], 
                            "permanent_link": perma_link, "stars": int(repo[3]), "num_lines": num_lines, 
                            "num_func": num_func, "num_for": num_for, "num_if": num_if})
    except IndexError:
        print("except IndexError!")
    line = file.readline()

print(bash_files)
with open("3-bash_files_list.json", "w") as f:
    json.dump({"bash_files": bash_files}, f, indent=4)