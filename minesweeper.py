from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://minesweeper.online/fr/")

def GetID(first, second):
    first = str(first)
    second = str(second)
    ID = "cell_" + first + "_" + second
    return ID

def defien(i, j):
    d = driver.find_element(By.ID, GetID(i, j)).get_attribute('class')[16]
    if d == "o":
        return "o"
    else:
        if len(driver.find_element(By.ID, GetID(i, j)).get_attribute('class')) >= 25:
            return "f"
        else:
            return "c"
    

pathe=[]

def fill():
    for j in range(16):
        for i in range(16):
            l=str(j)+","+str(i)
            pathe.append(l)

def Situation():
    if driver.find_element(By.ID, "top_area_face").get_attribute('class')[41] == "l" :
        driver.find_element(By.ID, "top_area_face").click()
    return driver.find_element(By.ID, "top_area_face").get_attribute('class')[41]
    
def GetJ(Worde):
    H = ""
    for t in Worde:
        if t == ",":
            return int(H)
        else:
            H = H + t

def GetI(Worde):
    p=1
    for t in Worde:
        if t != ",":
            p = p + 1
        else:
            return int(Worde[p:])
            
def DeleateItem(i):
    n=0
    for z in range(3):
        for m in range(3):
            if z-1+GetI(i) >= 0 and z-1+GetI(i) <= 15 and m-1+GetJ(i) >= 0 and m-1+GetJ(i) <= 15:
                if defien(z-1+GetI(i), m-1+GetJ(i)) == "o" or defien(z-1+GetI(i), m-1+GetJ(i)) == "f":
                    n = n + 1
    if n == 9:
        print("deleated item ", i)
        pathe.remove(i)
        
                
def login():
    driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/button[2]').click()
    time.sleep(2)
    name = driver.find_element(By.ID, 'sign_in_username')
    name.send_keys("julip")
    time.sleep(2)
    password = driver.find_element(By.ID, 'sign_in_password')
    password.send_keys("julip147")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="S66"]/div/div/form/div[3]/button[2]').click()




def checke(i, j, num):
    k = 0
    array = []
    array2 = []
    for z in range(3):
        for m in range(3):
            if z-1+i >= 0 and z-1+i <= 15 and m-1+j >= 0 and m-1+j <= 15:
                if defien(z-1+i, m-1+j) == "c":
                    k = k + 1
                    array.append(z-1+i)
                    array2.append(m-1+j)
                elif defien(z-1+i, m-1+j) == "f":
                    num = num - 1
    if num == 0:
        for f in range(k):
            driver.find_element(By.ID, GetID(array[f],array2[f])).click()
    elif k == num:
        for f in range(k):
            element = driver.find_element(By.ID, GetID(array[f], array2[f]))
            actions.context_click(element).perform()

print(GetID(7, 7))



driver.maximize_window()

actions = ActionChains(driver)


  # import time
time.sleep(2)

# login()

time.sleep(2)

driver.find_element(By.CLASS_NAME, 'level2-link').click()



#print(int(GetI(pathe[10])),int(GetJ(pathe[15])),pathe[224],len(pathe))

time.sleep(3)
def method1():
    fill()
    while Situation() == "u":
        driver.find_element(By.ID, GetID(7, 7)).click()
        driver.find_element(By.ID, GetID(7, 6)).click()
        driver.find_element(By.ID, GetID(8, 6)).click()
        driver.find_element(By.ID, GetID(8, 7)).click()
        for i in pathe:
            Situation()  
            if defien(GetI(i),GetJ(i)) == "o":
                if len(driver.find_element(By.ID, GetID(GetI(i),GetJ(i))).get_attribute('class')) > 30:
                    num = int(driver.find_element(By.ID, GetID(GetI(i),GetJ(i))).get_attribute('class')[31])
                if num > 0:
                    checke(GetI(i),GetJ(i), num)
            DeleateItem(i) 
            print(GetI(i),GetJ(i)) 



def method2():
    driver.find_element(By.ID, GetID(0,0)).click()
    while Situation() == "u":
        driver.find_element(By.ID, GetID(0,0)).click()
        i = 0
        while i < 15 or defien(i,j) !="c" :
            j = 0
            while j < 15 or defien(i,j) !="c" :
                if defien(i,j) !="f":
                    if len(driver.find_element(By.ID, GetID(i,j)).get_attribute('class')) > 30:
                        num = int(driver.find_element(By.ID, GetID(i,j)).get_attribute('class')[31])
                        if num > 0:
                            checke(i,j, num)
                j = j + 1
            print(i,j)
            i = i + 1
        Situation()
        

method1()











# for i in pathe:
#     print(i)

#pathe.remove(pathe[10])
#
#for i in pathe:
#    print(i)
time.sleep(20)



driver.quit()
