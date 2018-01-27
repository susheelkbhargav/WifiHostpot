import functools
import os
import subprocess
import random
import time
from piui import PiUi


ui=PiUi()

noduplist = []
class wifi_module(object):
  
  def __init__(self):
    self.ui = PiUi()

  def on_submit_click(self):
    self.page=self.ui.new_ui_page(title="login succesful")

  def login_page(self):
    self.page = self.ui.new_ui_page(title="Login and Password", prev_text="Back", onprevclick=main_menu)
    login=self.page.add_textbox('username',"h1")
    password= self.page.add_input("password","password")
    button=self.page.add_button("Submit", on_submit_click)

  def getssid(self):
    command = "./getESSID"
    process = subprocess.check_output(command, shell=True)
    namelist= process.split('\n')
    for i in namelist:
      #print i
      if i not in noduplist and i!='':
        noduplist.append(i)
    print noduplist
    self.page = self.ui.new_ui_page(title="Wifi Login")
    list1= self.page.add_list()
    print list1
    for i in noduplist:
      list1.add_item(i, onclick=self.login_page, chevron= True  )
    self.ui.done()
  

if __name__ == '__main__':
    obj = wifi_module()
    obj.getssid()
