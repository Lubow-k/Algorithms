#!/bin/bash

num_arg=${#@}

if [ $num_arg -lt 5 ]
then
    echo "Not enough parameters"
    exit 1
fi

path=$1
cd $path

good=$2
bad=$3

compil="$4 "$5

git checkout $bad &>/dev/null
hash=$(git log --pretty=format:"%h " | tac)
hash="$good ${hash#*$good}"
hash_array=($(echo $hash | tr " " "\n"))

low=0
high=${#hash_array[@]}-1


while [[ $low -lt $high ]]; do
    let "middle = ($low + $high) / 2"
    hash_mid=${hash_array[middle]}
    git checkout $hash_mid &>/dev/null
    $compil &>/dev/null
    result=$?

    find a.out &>/dev/null
    if [ $? -eq 0 ]
    then
        ./a.out &>/dev/null
	result=$?
        rm a.out
    fi

    if [[ $result -eq 0 ]]
    then
        low="$middle + 1"
    else
        high=$middle
    fi
done

git checkout $bad &>/dev/null
echo ${hash_array[low]}
