from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Chrome driver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open the Minesweeper game webpage
driver.get("https://minesweeper.online/fr/")

# Function to get the cell ID based on row and column
def GetID(first, second):
    first = str(first)
    second = str(second)
    ID = "cell_" + first + "_" + second
    return ID

# Function to define the state of a cell (open, flagged, or closed)
def defien(i, j):
    d = driver.find_element(By.ID, GetID(i, j)).get_attribute('class')[16]
    if d == "o":
        return "o"
    else:
        if len(driver.find_element(By.ID, GetID(i, j)).get_attribute('class')) >= 25:
            return "f"
        else:
            return "c"

# List to store cell paths
pathe = []

# Function to fill the path list with cell coordinates
def fill():
    for j in range(16):
        for i in range(16):
            l = str(j) + "," + str(i)
            pathe.append(l)

# Function to check the game situation (win, lose, or ongoing)
def Situation():
    if driver.find_element(By.ID, "top_area_face").get_attribute('class')[41] == "l":
        driver.find_element(By.ID, "top_area_face").click()
    return driver.find_element(By.ID, "top_area_face").get_attribute('class')[41]

# Function to get the column index from a coordinate string
def GetJ(Worde):
    H = ""
    for t in Worde:
        if t == ",":
            return int(H)
        else:
            H = H + t

# Function to get the row index from a coordinate string
def GetI(Worde):
    p = 1
    for t in Worde:
        if t != ",":
            p = p + 1
        else:
            return int(Worde[p:])

# Function to delete an item from the path list if all surrounding cells are open or flagged
def DeleateItem(i):
    n = 0
    for z in range(3):
        for m in range(3):
            if z-1+GetI(i) >= 0 and z-1+GetI(i) <= 15 and m-1+GetJ(i) >= 0 and m-1+GetJ(i) <= 15:
                if defien(z-1+GetI(i), m-1+GetJ(i)) == "o" or defien(z-1+GetI(i), m-1+GetJ(i)) == "f":
                    n = n + 1
    if n == 9:
        pathe.remove(i)



# Function to check and click cells based on the number of surrounding mines
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
            driver.find_element(By.ID, GetID(array[f], array2[f])).click()
        tabel.remove(GetID(i, j))
    elif k == num:
        for f in range(k):
            element = driver.find_element(By.ID, GetID(array[f], array2[f]))
            actions.context_click(element).perform()
        tabel.remove(GetID(i, j))


# Initialize ActionChains for right-click actions
actions = ActionChains(driver)

# Wait for the page to load
time.sleep(2)



# Click on the 'level2-link' to start the game
driver.find_element(By.CLASS_NAME, 'level2-link').click()

# Wait for the game to start
time.sleep(3)

# Method 1: Click cells and check their status
def method1():
    fill()
    while Situation() == "u":
        driver.find_element(By.ID, GetID(7, 7)).click()
        driver.find_element(By.ID, GetID(7, 6)).click()
        driver.find_element(By.ID, GetID(8, 6)).click()
        driver.find_element(By.ID, GetID(8, 7)).click()
        for i in pathe:
            Situation()
            if defien(GetI(i), GetJ(i)) == "o":
                if len(driver.find_element(By.ID, GetID(GetI(i), GetJ(i))).get_attribute('class')) > 30:
                    num = int(driver.find_element(By.ID, GetID(GetI(i), GetJ(i))).get_attribute('class')[31])
                if num > 0:
                    checke(GetI(i), GetJ(i), num)
            DeleateItem(i)

# Function to create a new table of cell IDs
def newtabel(tabel):
    for i in range(16):
        for j in range(16):
            tabel.append(GetID(i, j))
    return tabel



# Method : Click cells and check their status
def method():
    driver.find_element(By.ID, GetID(7, 7)).click()
    driver.find_element(By.ID, GetID(7, 6)).click()
    driver.find_element(By.ID, GetID(8, 6)).click()
    driver.find_element(By.ID, GetID(8, 7)).click()
    driver.find_element(By.ID, GetID(9, 7)).click()
    driver.find_element(By.ID, GetID(9, 8)).click()
    Situation()
    while Situation() == "u":
        i = 0
        while i < len(tabel):
            if defien(int(tabel[i].split('_')[1]), int(tabel[i].split('_')[2])) == 'o' and len(driver.find_element(By.ID, tabel[i]).get_attribute('class')) > 30:
                checke(int(tabel[i].split('_')[1]), int(tabel[i].split('_')[2]), int(driver.find_element(By.ID, tabel[i]).get_attribute('class')[31]))
            i += 1

# Initialize the table with cell IDs
tabel = []
tabel = newtabel(tabel)

# Run method to solve the Minesweeper game
method()

# Wait for 20 seconds to see the result
time.sleep(20)

# Close the browser
driver.quit()