#!/usr/bin/env bash

less ../data/TrimmedBXDPublish.csv | sed 's/x/0/g' | less > ../data/no_x_TrimmedBXDPublish.csv
