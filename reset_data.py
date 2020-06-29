import os
'''
This document just resets the 'database'
being used for this project
'''

os.system("rm users/*.json")

with open('completed_users.txt', "w") as f:
    f.write("")

with open('completed_ssns.txt', "w") as f:
    f.write("")

