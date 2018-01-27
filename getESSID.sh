sudo iwlist wlan0 scan | grep 'ESSID'  > WifiList 
sed -i 's/ESSID://g;s/"//g;s/\n//g;s/ //g' WifiList
cat WifiList
