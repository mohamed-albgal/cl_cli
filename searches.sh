#!/bin/zsh


outputfile="/Users/Maq0831/qq.txt"
search_strings="/Users/Maq0831/q.txt"
IFS=':'
echo $(date) >> $outputfile
while read -r s q min max t
do
     cl $s $q $min $max $t  >> $outputfile
done < "$search_strings"
echo "*********************" >> $outputfile
# link to pasta for reading a file line by line: https://www.cyberciti.biz/faq/unix-howto-read-line-by-line-from-file/
