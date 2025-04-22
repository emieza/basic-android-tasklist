import unittest, random, string, sys
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.enricmieza.basictasklist',
    appActivity='.MainActivity',
    noReset=True,
#    language='en',
#    locale='US'
)
 
appium_server_url = 'http://localhost:4723'
 
class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
 
    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_crea_tasca_Normal(self) -> None:
        try:
            # generem text aleatori
            task_text = ''.join(random.choice(string.ascii_letters) for _ in range(10))

            # posem títol de la tasca
            self.driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.EditText').send_keys(task_text)

            # cliquem botó
            self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Afegir"]').click()

            # verificar al ListView (text normal)
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, f'//*[contains(@text,"{task_text}")]'))
                )
            #print("✅ Verificació exitosa")
        except:
            # si no es troba el serch box (edit text) o el botó, és que l'aplicació no s'executa
            raise Exception("ERROR: l'aplicació no funciona. Cal arrencar-la manualment.")

 
    def test_crea_tasca_hackejada(self) -> None:
        try:
            # generem text aleatori
            task_text = ''.join(random.choice(string.ascii_letters) for _ in range(10))

            # posem títol de la tasca
            self.driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.EditText').send_keys(task_text)

            # cliquem botó
            self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Afegir"]').click()
        except:
            # si no es troba el serch box (edit text) o el botó, és que l'aplicació no s'executa
            raise Exception("ERROR: l'aplicació no funciona. Cal arrencar-la manualment.")

        # verificar al ListView (text normal o hackejat)
        hacked_text = task_text + "-HACKED!"
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, f'//*[@text="{task_text}" or @text="{hacked_text}"]'))
        )
        if element.text == hacked_text:
            #print("✅ Verificació exitosa")
            pass
        elif element.text == task_text:
            raise Exception("L'aplicació funciona, però no s'ha hackejat amb Frida!")
        else:
            raise Exception("ERROR desconegut.")

if __name__ == '__main__':
    unittest.main()
