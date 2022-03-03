from threading import local
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

#Selecionar navegador através de um driver executável (pode fazer o download na internet)
web = webdriver.Edge(
    executable_path="E:\Aplicativos\Web\WebDriver\msedgedriver.exe") #alterar local

#definição de variável pois ovu repeti-la
local = 'São Luís, Maranhão'

#função para selecionar o picker de data só quando a página carregar
def date_picker():
    try:
        retirada_date_picker = Select(
            web.find_element_by_xpath('//*[@id="puMonth_select"]'))
        retirada_date_picker.select_by_value('3-2022')
    except:
        time.sleep(1)
        date_picker()

#início da iteração primeiro link
web.get('https://www.booking.com/cars/index.pt-br.html')

#Pirmeiro caso de teste - Procurar através do xpath o campo para digitação do local de retirada de veículos e armazenar em variável, encontrar botão de pesquisar e clicar
print('UC_001')
local_retirada = web.find_element_by_xpath('//*[@id="ss_origin"]') #Campo para digitação
btn_search = web.find_element_by_xpath(
    '//*[@id="frm"]/div[2]/div[4]/div[2]/button') #botão pesquisar
btn_search.click() #ação de clicar
input() #metódo pessoal para aguardar comando no console para continuar para o próximo caso

#Segundo caso de teste - Digitar o local de retiradana variável e clicar no botão de pesquisar
print('UC_002')
local_retirada.send_keys(local)
btn_search.click()
input()

#Terceiro caso de teste - Identificar o campo autocomplete que aparece após digitação (comporatmento do site) 
print('UC_003')
local_retirada.clear() #limpar o campo

local_retirada.send_keys(local) #digitar o local
time.sleep(1.5) #metódo para aguardar a pesquisa jquery do site
local_retirada_autocomplete = web.find_element_by_xpath(
    '//*[@id="frm"]/div[2]/div[1]/div/div[1]/ul[1]/li[1]') #encontrar o primeiro elemento que retorna do jquery

local_retirada_autocomplete.click() #clicar no primeiro elemento
time.sleep(0.5) #tempo de espera rápido para envio das informações

idade_motorista_checkbox = web.find_element_by_xpath(
    '//*[@id="frm"]/div[3]/label/span[1]') #encontrar checkbox

idade_motorista_checkbox.click() #desmarcar checkbox
time.sleep(0.5)
btn_search.click()
input()

print('UC_004')  # UC_004
retirada_date_picker = Select(web.find_element_by_xpath('//*[@id="puMonth_select"]'))  #utilizar metodo select pois é um dropdown list
retirada_date_picker.select_by_value('3-2022')  #utilizar select by value e tirar do site o valor que é atribuido ao selecionar o que eu quero testar
time.sleep(0.5)
devolucao_date_picker = Select(
    web.find_element_by_xpath('//*[@id="doMonth_select"]'))
devolucao_date_picker.select_by_value('2-2022')
btn_search2 = web.find_element_by_xpath('//*[@id="proceed"]/button')
btn_search2.click()
input()

print('UC_005')# UC_005
web.get('https://www.booking.com/cars/index.pt-br.html')
time.sleep(1.5)
local_retirada = web.find_element_by_xpath('//*[@id="ss_origin"]')
local_retirada.send_keys(local)
time.sleep(1.5)
local_retirada_autocomplete = web.find_element_by_xpath(
    '//*[@id="frm"]/div[2]/div[1]/div/div[1]/ul[1]/li[1]')
local_retirada_autocomplete.click()
time.sleep(0.5)
idade_motorista_checkbox = web.find_element_by_xpath(
    '//*[@id="frm"]/div[3]/label/span[1]')
idade_motorista_checkbox.click()
time.sleep(0.5)
idade_motorista_input = web.find_element_by_xpath('//*[@id="driverAgeInput"]')
idade_motorista_input.send_keys('5')
time.sleep(0.5)
btn_search = web.find_element_by_xpath(
    '//*[@id="frm"]/div[2]/div[4]/div[2]/button')
btn_search.click()
input()

print('UC_006')  # UC_006
idade_motorista_checkbox.click()
local_retirada.clear()
local_retirada.send_keys(local)
time.sleep(1.5)
local_retirada_autocomplete = web.find_element_by_xpath(
    '//*[@id="frm"]/div[2]/div[1]/div/div[1]/ul[1]/li[1]')
local_retirada_autocomplete.click()
btn_search.click()
date_picker()
btn_search = web.find_element_by_xpath('//*[@id="proceed"]/button')
btn_search.click()
input()

print('UC_007')  # UC_007
web.get('https://www.booking.com/cars/index.pt-br.html')
radio2 = web.find_element_by_xpath('//*[@id="frm"]/div[1]/div[2]/label')
radio2.click()
btn_search = web.find_element_by_xpath('//*[@id="frm"]/div[2]/div[4]/div[2]/button')
btn_search.click()
input()

print('UC_008')  # UC_008
#web.get('https://www.booking.com/cars/index.pt-br.html')
radio2 = web.find_element_by_xpath('//*[@id="frm"]/div[1]/div[2]/label')
radio2.click()
time.sleep(0.5)
local_retirada = web.find_element_by_xpath('//*[@id="ss_origin"]')
local_retirada.send_keys(local)
time.sleep(1.5)
local_retirada_autocomplete = web.find_element_by_xpath(
    '//*[@id="frm"]/div[2]/div[1]/div/div[1]/ul[1]/li[1]')
local_retirada_autocomplete.click()
time.sleep(0.5)
btn_search = web.find_element_by_xpath('//*[@id="frm"]/div[2]/div[4]/div[2]/button')
btn_search.click()
input()

print('UC_009')  # UC_009
#web.get('https://www.booking.com/cars/index.pt-br.html')
radio2 = web.find_element_by_xpath('//*[@id="frm"]/div[1]/div[2]/label')
radio2.click()
for i in range(len(local)):
    local_retirada.send_keys(Keys.BACKSPACE)
time.sleep(1)
local_devolucao = web.find_element_by_xpath('//*[@id = "ss"]')
local_devolucao.send_keys(local)
time.sleep(1.5)
local_retirada_autocomplete = web.find_element_by_xpath(
    '//*[@id="frm"]/div[2]/div[2]/div/div[1]/ul[1]/li[1]')
local_retirada_autocomplete.click()
btn_search = web.find_element_by_xpath('//*[@id="frm"]/div[2]/div[4]/div[2]/button')
btn_search.click()
input()

print('UC_010')# UC_010
#web.get('https://www.booking.com/cars/index.pt-br.html')
radio2 = web.find_element_by_xpath('//*[@id="frm"]/div[1]/div[2]/label')
radio2.click()
time.sleep(0.5)
local_retirada = web.find_element_by_xpath('//*[@id="ss_origin"]')
local_retirada.send_keys(local)
time.sleep(1.5)
local_retirada_autocomplete = web.find_element_by_xpath(
    '//*[@id="frm"]/div[2]/div[1]/div/div[1]/ul[1]/li[1]')
local_retirada_autocomplete.click()
time.sleep(0.5)
local_devolucao = web.find_element_by_xpath('//*[@id = "ss"]')
local_devolucao.send_keys(local)
time.sleep(1.5)
local_retirada_autocomplete = web.find_element_by_xpath(
    '//*[@id="frm"]/div[2]/div[2]/div/div[1]/ul[1]/li[1]')
local_retirada_autocomplete.click()
btn_search = web.find_element_by_xpath('//*[@id="frm"]/div[2]/div[4]/div[2]/button')
btn_search.click()
input()
