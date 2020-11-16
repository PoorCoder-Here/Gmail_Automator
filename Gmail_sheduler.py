from selenium import webdriver
import time
import datetime as dt
from selenium.webdriver.common.keys import Keys
path=input("Enter the location of your webdriver")
type=input("Enter the browser name of the webdriver")
while True:
    if type.lower()=='chrome':
        driver=webdriver.Chrome(path)
        break
    elif type.lower()=='edge':
        driver=webdriver.Edge(path)
        break
    elif type.lower()=='firefox':
        driver=webdriver.Firefox(path)
        break
    else:
        print("Please use anyone of the 'EDGE', 'CHROME','FIREFOX'")
#Enter your mail id in the gmail variable inside the double quotes
gmail=input("Enter your mail ID:")
#Enter your password in the passw variable inside the double quotes
passw=input("Enter the password of the mail ID:")
send=input("Enter the mail ID to which you want to send mail:")
sub=input("Enter the subject of the mail:")
content=input("Enter the details you want to send:")
k=input("If you have any attachment to send (yes/no):")
k=k.lower()
nom=0
attach_file=[]
if k=='yes':
    nom=int(input("Enter no of attachements:"))
    u=0
    while u<nom:
        print("Enter the location of the attachment ",u+1," correctly:")
        loc=input()
        attach_file.append(loc)
        u+=1
else:
    print("There is no any attachment in the mail")
run=True
while run:
    try:
        driver.get('https://mail.google.com/mail/')
        run=False
    except:
        driver.get('https://mail.google.com/mail/')
email=driver.find_element_by_name('identifier')
email.send_keys(gmail)
email.send_keys(Keys.ENTER)
run1=True
while run1:
    try:
        passw=driver.find_element_by_name('password')
        passw.send_keys(passw)
        passw.send_keys(Keys.ENTER)
        run1=False
    except:
        run1=True
time.sleep(15)
comp=driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div')
comp.click()
time.sleep(10)
to=driver.find_element_by_name('to')
to.send_keys(send)
time.sleep(3)
t=dt.datetime.now()
subject=driver.find_element_by_name('subjectbox')
subject.send_keys(sub)
time.sleep(3)
text=driver.find_element_by_id(':pw')
text.send_keys(content)
time.sleep(6)
attach=driver.find_element_by_name('Filedata')
inc=0
while inc<nom:
    attach=driver.find_element_by_name('Filedata')
    attach.send_keys(attach_file[inc])
    time.sleep(7)
    inc+=1
send=driver.find_element_by_id(':oh')
send.click()