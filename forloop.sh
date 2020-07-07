#!/bin/bash

read -p "Give me one number: " num1
read -p "Give me a second number: " num2
if [[ $num1 -lt 10 || $num2 -lt 10 ]] ; then
 
	for ((i = $num1; i <= $num2; i++))
	do
		echo "number: $i"
	done
else
	let sum=$num1+$num2
	echo "The sum is: $sum"
fi
