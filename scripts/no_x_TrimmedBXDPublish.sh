#!/usr/bin/env bash

less TrimmedBXDPublish.csv | sed 's/x/0/g' | less > no_x_TrimmedBXDPublish.csv
