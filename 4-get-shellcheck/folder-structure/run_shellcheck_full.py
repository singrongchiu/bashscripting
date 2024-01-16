import json
import subprocess
import os
 
f = open('../3-bash_files_list.json')
data = json.load(f)

bash_files_list = data["bash_files"]
print(len(bash_files_list))

largedirname = "shellcheck-output"
isExist = os.path.exists(largedirname)

if not isExist:
    os.mkdir(largedirname)

for bashfile in bash_files_list:
    title = bashfile["ssh_link"][15:][:-4]
    print("title ", title)

    title = title.replace("/", ".")
    repo_path = largedirname + "/" + title

    isExist = os.path.exists(repo_path)
    if not isExist:
        os.mkdir(largedirname + "/" + title)

    rawlink = bashfile["permanent_link"][10:]
    rawlink = rawlink.replace("/blob", '')
    rawlink = "https://raw.githubusercontent.com" + rawlink
    print(rawlink)

    newtitle = bashfile["bash_file_loc"][2:].replace("/", ".")

    subprocess.run(["bash", "./run_shellcheck_full.sh", rawlink, "../tempbash.sh", 
                    largedirname + "/" + title + "/" + newtitle])