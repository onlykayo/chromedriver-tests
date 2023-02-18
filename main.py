from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class RobloxCatalog:
    def __init__(self, user, password, login_url, catalog_url):
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome()
        self.driver.get(login_url)

        username_box = self.driver.find_element(By.ID, "login-username")
        username_box.send_keys(user)

        pass_box = self.driver.find_element(By.ID, "login-password")
        pass_box.send_keys(password)
        time.sleep(1)

        botao_logar = self.driver.find_element(By.ID, "login-button")
        botao_logar.click()
        time.sleep(6)
        try:
            check_2fa = self.driver.find_element(By.CLASS_NAME, "modal-dialog") #verificar 2fa
            test = check_2fa.text
            print("2FA/Authenticator Detectado, coloque seu código para continuar")

            ## verificar se o usuário ja logou
            while True:
                self.check_currentlink(catalog_url)
                break

        except Exception:
            print(Exception)
            ## verificar se o usuário ja logou
            self.check_currentlink(catalog_url)


    def check_currentlink(self, catalog_url):
        while True:
            if self.driver.current_url == "https://www.roblox.com/home":
                print("enviando para a página de catálogo")
                self.planilhar(catalog_url)
                break
            time.sleep(1)
        self.planilhar(catalog_url)
        


    def planilhar(self, catalog_url):
        self.driver.get(catalog_url)
        print("página: ")
        time.sleep(5)




print("iniciando em 5 segundos...")
time.sleep(5)
bot = RobloxCatalog("usuario", "senha", "https://roblox.com/login", "https://create.roblox.com/creations/upload?assetType=TShirt")
