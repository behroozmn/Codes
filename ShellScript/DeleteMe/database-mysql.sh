set -f        # disable globbing
IFS=$'\n'     # set field separator to NL (only)
arr=($(mysql -u root -p123456 "sadrsds" -h localhost -Bse "SELECT * FROM raiddisk;"))
 
for i in "${arr[@]}"
do
   echo "$i"
done



# /usr/local/mysql/bin/mysql -u root -p123456 "sadrsds" -h localhost -Bse "SELECT * FROM raiddisk INTO OUTFILE '/tmp/myfilename.csv' FIELDS TERMINATED BY ','  ENCLOSED BY '\"' LINES TERMINATED BY '\n'"