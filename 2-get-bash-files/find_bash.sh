#! /bin/bash
# ${1} is ssh link to repo, ${2} is repo name, ${3} is star count, ${4} is output text file 

git clone "${1}"

# find sha values
cd "${2}" || exit
sha=$(git log --pretty=format:'%h' -n 1)
sha_long=$(git log --pretty=format:'%H' -n 1)
cd ..

# find .sh files in repo
x=$(find "./${2}" -name "*.sh")
echo "find .sh files:" 
echo "$x"
shfiles=("${x// / }")

# full_title_length=$((${#2}+3))
# echo ${full_title_length}

if (( ${#shfiles[@]} )); then
    for addr in ${shfiles[@]}
    do
        echo "${1},${sha_long},${2},${3},${addr}" >> "${4}"
        echo "lines,"$(wc -l "${addr}" | awk '{ print $1 }') >> "${4}"

        # remove content after '#' so not picked up
        sed -i '/^[[:blank:]]*#/d;s/#.*//' "${addr}"

        # find functions
        numfunc1=$(grep -c ^function "${addr}") 
        numfunc2=$(grep -c "[A-Za-z_-]\+[ ]*()" "${addr}")
        # subtract overlap i.e. "function func_name ()"
        numfuncwithboth=$(grep -c "function [A-Za-z_-]\+[ ]*()" "${addr}")
        echo "function,"$(($numfunc1+$numfunc2-$numfuncwithboth)) >> "${4}"
        echo $(grep ^function "${addr}") >> "${4}"
        echo $(grep "[A-Za-z_-]*[ ]*()" "${addr}") >> "${4}"

        # find fors
        echo "for,"$(grep -c 'for ' "${addr}") >> "${4}"
        echo $(grep 'for ' "${addr}") >> "${4}"
        
        # find ifs
        echo "if,"$(grep -c 'if ' "${addr}") >> "${4}" 
        echo $(grep 'if ' "${addr}") >> "${4}"   
    done
else
    echo "${1},${sha_long},${2},${3}," >> "${4}"
    echo "this repo has no .sh files!!"
fi

rm -rf "${2}"

echo "ended"