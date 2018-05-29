#!/bin/bash

# I am creating a variable greeting
greeting='Hello World'

# I am printing the contents of greeting
echo $greeting

# Touch and print a range of files in a loop

for myfile in {A..Z}.txt;
do
    touch $myfile
    echo $myfile
done

