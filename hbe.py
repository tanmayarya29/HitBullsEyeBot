import os
try:
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from tkinter import Tk,Label
    from tkinter import simpledialog,Radiobutton
    import os
    import time
    import datetime
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
except:
    os.system('pip install selenium')
    os.system('pip install webdriver-manager')
    os.system('pip install datetime')
    os.system('pip install tk')
    os.system('pip install urllib3')
finally:
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from tkinter import Tk
    from tkinter import simpledialog
    import os
    import time
    import datetime
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys

root=Tk()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.set_window_size(683,768)

def get_details():
    global usrnm
    global pswd
    root.withdraw()
    if os.path.isfile('login_up.txt'):
        f=open('login_up.txt','r+')
        usrnm=f.readline()
        pswd=f.readline()
        f.close()
    else:
        f=open('login_up.txt','w')
        usrnm=simpledialog.askstring(title="Username",prompt="Enter the Username here:")
        f.write("u-"+usrnm+"\n")
        pswd=simpledialog.askstring(title="Password",prompt="Enter the Password here:")
        f.write("p-"+pswd)
        f.close()
        f=open('login_up.txt','r+')
        usrnm=f.readline()
        pswd=f.readline()
        f.close()
    
    usrnm=usrnm[2:12]
    pswd=pswd[2:]

def login():
    driver.get("https://www.hitbullseye.com/")
    driver.find_element_by_xpath('//*[@id="mba-w-1"]/div[3]/div/header/div/div/div[3]/ul/li[1]/a').click()
    get_details()
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(usrnm)
    driver.find_element_by_xpath('//*[@id="userpassword"]').send_keys(pswd)
    driver.find_element_by_xpath('//*[@id="loginbtn"]').click()

def type():
    typ="o"
    typ=simpledialog.askstring(title="Type(O/T)",prompt="Enter the Test-type here(T - for time bound || O - for open):")
    if typ=="t" or typ=="T":
        driver.find_element_by_xpath('/html/body/app/body/div/div/div[2]/app-testzone/app-testzonemenus/div/div/div/div[4]/div[8]/a').click()
    else:
        driver.find_element_by_xpath('/html/body/app/body/div/div/div[2]/app-testzone/app-testzonemenus/div/div/div/div[4]/div[9]/a').click()

#list tests 
def list_tests():
    time.sleep(4)
    global rem_test_names,rem_test_start
    rem_test_names=[]
    rem_test_start=[]
    x=driver.find_elements_by_tag_name('tr')
    for i in x:
        if "Start Now" in i.get_attribute('innerHTML') or "Resume Test" in i.get_attribute('innerHTML'):
            rem_test_names.append(i.find_elements_by_tag_name('td')[0].get_attribute('innerHTML').strip().strip('\n')[:35].strip('\n').strip())
            rem_test_start.append(i.find_elements_by_tag_name('a'))
    for i in range(len(rem_test_names)):
        print(str(i+1)+" - "+rem_test_names[i])
    print(rem_test_start)
    rem_test_start[0][0].click()
    driver.find_element_by_xpath('//*[@id="instPaginationa"]').click()
    driver.find_element_by_xpath('//*[@id="disclaimer"]').click()
    driver.find_element_by_xpath('//*[@id="secondPagep2"]/div/input').click()
def attempt():
    anskey=[]
    ansfile=open('anskey.txt','r')
    for i in ansfile.readlines():
        anskey.append(i.strip('\n'))
    ansfile.close()
    print(anskey)
    time.sleep(1)
    for i in range(len(anskey)):
        if(anskey[i]=="A" or anskey[i]=="a"):
            driver.find_element_by_xpath('//*[@id="A_'+str(i+1)+'"]').click()
        elif (anskey[i]=="B" or anskey[i]=="b"):
            driver.find_element_by_xpath('//*[@id="B_'+str(i+1)+'"]').click()
        elif (anskey[i]=="C" or anskey[i]=="c"):
            driver.find_element_by_xpath('//*[@id="C_'+str(i+1)+'"]').click()
        elif (anskey[i]=="D" or anskey[i]=="d"):
            driver.find_element_by_xpath('//*[@id="D_'+str(i+1)+'"]').click()
        driver.find_element_by_xpath('//*[@id="foot"]/div[1]/div[3]/a').click()
    driver.find_element_by_xpath('//*[@id="demo-page"]/div[1]/a[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="activator"]/a').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="popupLogin"]/div/form/div[1]/label/span').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="close_confirmed"]').click()
def main():
    login()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/app/body/div/div/div[2]/dash-land/div[2]/div/div[1]/div[2]/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/app/body/div/div/div[2]/app-testzone/app-testzonemenus/div/div/div/div[4]/div[1]/a').click()
    time.sleep(2)
    type()
    time.sleep(2)
    list_tests()
    time.sleep(3)
    attempt()
main()
    


