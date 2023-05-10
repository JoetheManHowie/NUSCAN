#!/bin/bash

path_to_execute="./nuscan"
save_to="../datasets"

$path_to_execute $1 $2 $3 $4 $5 > ${save_to}/$1.test
