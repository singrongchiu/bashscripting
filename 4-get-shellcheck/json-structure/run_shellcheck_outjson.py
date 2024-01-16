import json
import subprocess
 
f = open('../3-bash_files_list.json')
data = json.load(f)
newdata = []

bash_files_list = data["bash_files"]
print(len(bash_files_list))

for bashfile in bash_files_list:

    rawlink = bashfile["permanent_link"][10:]
    rawlink = rawlink.replace("/blob", '')
    rawlink = "https://raw.githubusercontent.com" + rawlink
    print(rawlink)

    subprocess.run(["bash", "./run_shellcheck_outjson.sh", rawlink, "../tempbash.sh", 
                    "../tempshellcheck.txt", "../temperrorcodes.txt"])
    
    data = ""
    with open("../temperrorcodes.txt", 'r') as file:
        data = file.read().replace('\n', ' ')
    
    errorcodes = data.split()

    bashfile["shellcheck_errors"] = errorcodes

    newdata.append(bashfile)

with open("4-bash_files_list_sc.json", "w") as f:
    json.dump({"bash_files": newdata}, f, indent=4)
