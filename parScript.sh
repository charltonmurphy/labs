#!/bin/bash

open ex.json
#output=$(grep "ID" ex.json | cut -d: -f2)
#echo "The value of ID is: "$output
echo -n "Please type the key of the value you want: "; read x 
output=$(grep "$x" ex.json | cut -d: -f2)
output2=$(grep "$x" ex.json | cut -d: -f3)
echo "The value of "$x" is: "$output $output2
echo -n "Please type the value of the key you want: "; read y
output1=$(grep "$y" ex.json | cut -d: -f1)
echo "The key of "$y" is: " $output1
echo "OH HELL YEA!!!"
