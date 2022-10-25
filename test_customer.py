import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLoginCustomer:

    def setup(self):
        self.email = 'nikus17222342342347@mail.ru'
        self.password = '5555'
        self.phone = '8888881114'
        self.name = 'Петр'
        self.inn = '7701002520'
        self.company_name = 'MyCompany'

    def registration_customer(self):
        self.browser_customer.find_element(By.XPATH, "//a[contains(text(),'Регистрация')]").click()
        self.browser_customer.find_element(By.ID, 'company_inn').send_keys(self.inn)
        WebDriverWait(self.browser_customer, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'7701002520')]"))).click()
        self.browser_customer.find_element(By.ID, 'person_name').send_keys(self.name)
        self.browser_customer.find_element(By.ID, 'email').send_keys(self.email)
        self.browser_customer.find_element(By.ID, 'phone').send_keys(self.phone)
        self.browser_customer.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()
        assert WebDriverWait(self.browser_customer, 5).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Заявка')]")))

    def open_lending(self):
        self.browser_customer = webdriver.Chrome()
        self.browser_customer.get('https://dev.mobistaff.ru/')

    def open_customer(self):
        self.browser_customer = webdriver.Chrome()
        self.browser_customer.get('https://dev.mobistaff.ru/customer/login')

    def close_customer(self):
        self.browser_customer.quit()

    def login_customer(self):
        self.browser_customer.find_element(By.ID, 'email').send_keys(self.email)
        self.browser_customer.find_element(By.ID, 'password').send_keys(self.password)
        self.browser_customer.find_element(By.ID, 'agree').click()
        self.browser_customer.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        assert WebDriverWait(self.browser_customer, 5).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Профиль')]")))

    def test_podbor_1(self):
        self.open_lending()
        self.browser_customer.find_element(By.XPATH, "//button[contains(text(),'Подобрать исполнителя')]").click()
        self.browser_customer.find_element(
            By.XPATH, "/html[1]/body[1]/div[1]/div[1]/section[2]/div[1]/div[9]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]").send_keys(self.name)
        self.browser_customer.find_element(
            By.XPATH, "/html[1]/body[1]/div[1]/div[1]/section[2]/div[1]/div[9]/div[2]/div[1]/div[1]/div[1]/form[1]/div[2]/input[1]").send_keys(self.phone)
        self.browser_customer.find_element(
            By.XPATH, "/html[1]/body[1]/div[1]/div[1]/section[2]/div[1]/div[9]/div[2]/div[1]/div[1]/div[1]/form[1]/div[3]/input[1]").send_keys(self.email)
        self.browser_customer.find_element(
            By.XPATH, "/html[1]/body[1]/div[1]/div[1]/section[2]/div[1]/div[9]/div[2]/div[1]/div[1]/div[1]/form[1]/div[4]/input[1]").send_keys(self.company_name)
        self.browser_customer.find_element(By.XPATH, "//button[contains(text(),'Оставить заявку')]").click()
        assert WebDriverWait(self.browser_customer, 5).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Хорошо')]")))
        self.close_customer()

    def test_nachat_dialog(self):
        self.open_lending()
        self.browser_customer.execute_script("window.scrollTo(0,2000)")
        time.sleep(3)
        WebDriverWait(self.browser_customer, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Начать диалог')]"))).click()
        self.browser_customer.find_element(
            By.XPATH, "/html[1]/body[1]/div[1]/div[1]/section[2]/div[1]/div[9]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]").send_keys(self.name)
        self.browser_customer.find_element(
            By.XPATH, "/html[1]/body[1]/div[1]/div[1]/section[2]/div[1]/div[9]/div[2]/div[1]/div[1]/div[1]/form[1]/div[2]/input[1]").send_keys(self.phone)
        self.browser_customer.find_element(
            By.XPATH, "/html[1]/body[1]/div[1]/div[1]/section[2]/div[1]/div[9]/div[2]/div[1]/div[1]/div[1]/form[1]/div[3]/input[1]").send_keys(self.email)
        self.browser_customer.find_element(
            By.XPATH, "/html[1]/body[1]/div[1]/div[1]/section[2]/div[1]/div[9]/div[2]/div[1]/div[1]/div[1]/form[1]/div[4]/input[1]").send_keys(self.company_name)
        self.browser_customer.find_element(By.XPATH, "//button[contains(text(),'Оставить заявку')]").click()
        assert WebDriverWait(self.browser_customer, 5).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Хорошо')]")))
        self.close_customer()

    def test_otpravit(self):
        self.open_lending()
        #self.browser_customer.maximize_window()
        #self.browser_customer.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(self.browser_customer, 5).until(
            EC.presence_of_element_located((
            By.CSS_SELECTOR, ".mb-4:nth-child(1) .border-gray-100"))).send_keys(self.name)
        self.browser_customer.find_element(
            By.CSS_SELECTOR, ".mb-4:nth-child(2) .border-gray-100").send_keys(self.phone)
        self.browser_customer.find_element(
            By.CSS_SELECTOR, ".mb-4:nth-child(3) .border-gray-100").send_keys(self.email)
        self.browser_customer.find_element(
            By.CSS_SELECTOR, ".mb-4:nth-child(4) .border-gray-100").send_keys(self.company_name)
        self.browser_customer.find_element(By.CSS_SELECTOR, ".\!h-12").click()
        assert WebDriverWait(self.browser_customer, 5).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Хорошо')]")))
        self.close_customer()

    def test_login_customer(self):
        self.open_customer()
        WebDriverWait(self.browser_customer, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Войти')]")))
        self.login_customer()
        self.close_customer()

    def test_registration_customer(self):
        self.open_customer()
        self.registration_customer()
        self.close_customer()