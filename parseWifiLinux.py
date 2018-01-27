import os
import subprocess
from piui import PiUi
ui=PiUi()

noduplist = []

def on_submit_click():
  page=ui.new_ui_page(title="login succesful")

def login_page():
  page=ui.new_ui_page(title="Login and Password", prev_text="Back", onprevclick=main_menu)
  #page.add_textbox(i,"hr")
  password= page.add_input("password","password")
  page.add_button("Submit", on_submit_click)


def main_menu():
  page= ui.new_ui_page(title="Wifi Login")
  list= page.add_list()
  for i in noduplist:
    list.add_item(i, onclick=login_page, chevron= True  )

def getssid():
  command = "nmcli -t -f ssid dev wifi| cut -d\\' -f2"  
  process = subprocess.check_output("nmcli -t -f ssid dev wifi| cut -d\\' -f2", shell=True)
  namelist= process.split('\n')
  for i in namelist:
    if i not in noduplist:
      noduplist.append(i)
  print noduplist
  main_menu()


getssid()






