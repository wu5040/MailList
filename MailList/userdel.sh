#!/bin/bash

for user in $(cat users.txt)

do

userdel -r $user

echo "del $user ok"

done

