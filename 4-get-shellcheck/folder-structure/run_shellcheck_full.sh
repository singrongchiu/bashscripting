#! /bin/bash
# ${1} is raw permanent link, ${2} is temp bash file, ${3} is output file

curl "${1}" -o "${2}"

shellcheck -e SC1091 -e SC2154 -e SC1090 "${2}" >> "${3}"