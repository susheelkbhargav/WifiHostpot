from wifi import Cell, Scheme
Cell.all('wlan0')
cell=Cell.all('wlan0')[0]
scheme=Scheme.for_cell('wlan0','home',cell,"Decimals10")
#in place of deciamls 10 we can get variable
scheme.save()
scheme.activate()

