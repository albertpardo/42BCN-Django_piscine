#!/bin/bash

lib_folder="local_lib"

pip --version

pip install --upgrade --force-reinstall git+https://github.com/jaraco/path.git --target="${lib_folder}" &> install.log

python3 my_program.py
