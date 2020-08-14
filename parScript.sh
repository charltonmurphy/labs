#!/bin/bash


readonly outFile=output.txt
echo -n "Please type file name: "; read file

if [ -f $file ]; then 
	
	echo -n "Please type in the key for the value you want to find: "; read x
	output="$(grep "$x" "$file" | cut -d: -f2,3)"
	echo  "The value is: "$output > $outFile
	
	echo -n "Please type in the value for the Key you want to find: "; read y
	output1="$(grep "$y" "$file" | cut -d: -f1)"
	echo  "The key is: "$output1 >> $outFile
else 
	echo "$file does not exist!" > $outFile
	exit
fi
