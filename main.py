#!/usr/bin/env python3

# Shell
# - https://docs.python.org/ko/3.7/using/unix.html?highlight=shebang#miscellaneous
# - https://docs.python.org/3.7/library/subprocess.html
# JSON
# - https://docs.python.org/ko/3.7/library/json.html?highlight=json#module-json
# Pip
# - https://docs.python.org/ko/3/installing/index.html

import subprocess
import json

k8s_ver = subprocess.check_output('kubectl version -o json' , shell=True)
print(k8s_ver)

k8s_ver = json.loads(k8s_ver)
print(k8s_ver['serverVersion'])
