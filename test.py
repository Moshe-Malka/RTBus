from selenium import webdriver
from time import sleep
import sys 

m_link = "https://moovitapp.com/?from=%D7%A8%D7%95%D7%98%D7%A9%D7%99%D7%9C%D7%93%20140&to=%D7%90%D7%97%D7%93%20%D7%94%D7%A2%D7%9D%2028&fll=32.080492_34.883785&tll=32.06515_34.775467&customerId=4908&metroId=1&lang=he"

w_driver = webdriver.PhantomJS()
w_driver.set_window_size(1920,1080)

w_driver.get(m_link)
sleep(3)

try:
    rows = w_driver.find_elements_by_css_selector(".legs-container.layout-column.flex")
except:
    print "[*] Error: could not find main selector named '.legs-container.layout-column.flex' "
    sys.exit(0)

for r in rows:
    if("82" in r.text):
        print "Line Number: " + r.text.split("\n")[0]
        star_time = r.find_element_by_class_name("start-time")
        #end_time =  r.find_element_by_class_name("end-time")
        print "Leaving At: " + star_time.text
        duration = r.find_element_by_class_name("duration")
        print "Duration: " + duration.text
        try:
            eta = r.find_element_by_class_name("eta")
            if(eta):
                print "ETA: "+ eta.text
        except:
            print "[*] Error: could not find class named 'eta' "
            sys.exit(0)


w_driver.close()
