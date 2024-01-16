#! /bin/bash
# ${1} is raw permanent link, ${2} is temp bash file, ${3} is shellcheck output file, ${4} is temp shellcheck error codes file

curl "${1}" -o "${2}"

shellcheck -e SC1091 -e SC2154 -e SC1090 "${2}" > "${3}"

# find all error codes "SC[4 digits]"
grep -oh " SC[0-9][0-9][0-9][0-9]" "${3}" > "${4}"

cat "${3}"
echo "XXXXXXXXXXXXXXXXX"
cat "${4}"