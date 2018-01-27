import os
import subprocess
from piui import PiUi

def getssid():

  command = "nmcli -t -f ssid dev wifi| cut -d\\' -f2"  
  process = subprocess.check_output("nmcli -t -f ssid dev wifi| cut -d\\' -f2", shell=True)
  namelist= process.split('\n')
  noduplist = []
  for i in namelist:
    if i not in noduplist:
      noduplist.append(i)
  print (noduplist)

  ui = PiUi()
  page = ui.new_ui_page(title="Available Networks")
  page_form= ui.new_ui_page(title= "Enter Login Details")
  txt= page_form.add_input("text","loginID")
  txt2= page_form.add_input("text","password")
  button= page.add_button("submit", onButtonClick)
  list =page.addlist()
  for i in nonduplist:
    list.add_item(nonduplist[i], onclick= page_form)
	
def onButtonClick(self):
	#ifconnected to wifi
	title.set_text("connected to" + noduplist[i])

getssid()