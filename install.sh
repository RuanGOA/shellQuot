#!/bin/bash

WAY2PY=$(pwd cot.py);

echo "alias quot='python3 $WAY2PY/cot.py $@'"  >> ~/.bashrc;
exec bash