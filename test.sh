#!/bin/sh
file=$1
name="course"
echo $file
echo $name
if [ $file = $name ];
then
    echo "Yes!"
else
    echo "No!"
fi
