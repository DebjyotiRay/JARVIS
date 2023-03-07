# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from whatsapp import *

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

from datetime import datetime
now = datetime.now()
current_hour=int(now.strftime("%H"))
current_min=int(now.strftime("%M"))
current_sec=now.strftime("%S")
print(current_hour)
print(current_min+1)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    message('+919830137426','hello',current_hour,current_min+2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
