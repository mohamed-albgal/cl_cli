#!/bin/zsh


search_strings="/Users/Maq0831/q.txt"
IFS=':'
while read -r s q min max t
do
     cl $s $q $min $max $t 
done < "$search_strings"
# link to pasta for reading a file line by line: https://www.cyberciti.biz/faq/unix-howto-read-line-by-line-from-file/
