from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# Inicjalizacja przeglądarki Chrome
driver = webdriver.Chrome()

# Otwarcie okna przeglądarki
driver.get('https://www.google.pl')

#Maksymalizacja okna
driver.maximize_window()  #lepiej ustawic stała wielkosc okna zeby uniknac wykrzaczania sie testu
driver.set_window_size(1600, 800)

#znajdowanie elementu by XPath - zaakceptuj zgody
accept = driver.find_element('xpath', '//*[@id="L2AGLb"]/div')
#kliknięcie znalezionego elementu
accept.click()

#znajdz pole wyszukiwania
seach_box = driver.find_element('name', 'q')

#wproawdzenie hasła do wyszukiwarki
seach_box.send_keys('pogoda hersonissos')

#naciśnij enter
seach_box.send_keys(Keys.ENTER)

# Sleep tylko do celów debugowych, testowych, nauczania
time.sleep(10)

# //*[@id="input"] - jak // to chcemy aby szukal w kodzie takiej sekwencji jak podana po //
#zakończ działanie przeglądarki
#zamknięcie przeglądarki
driver.quit()
# zamknięcie danego okna przeglądarki driver.close()

