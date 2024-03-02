import os

shutdown = input("Shutdown Your Pc? (Yes/No): ")

if shutdown == 'no':
    exit()

else:
    os.system("shutdown /s /t 1")
    