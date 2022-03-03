# -*- coding: utf-8 -*-

from threading import local
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
driver.get("https://www.booking.com/taxi/index.pt-br.html")

#1º caso de teste: Selecionar opção de retorno. A página inicial carrega apenas com a opção de ida.
print('UC_001')
#Botão para habilitar opção de retorno (return)
btn_return = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/form/div[1]/fieldset/div/div[2]/label/span')
#clicar no botão de retorno
btn_return.click()
#aguardar carregamento da página
time.sleep(1)

#2º caso de teste: Digitar local de retirada inválido e clicar no botão de pesquisar
print('UC_002')
#campo para inserir local de retirada
pickup_local = driver.find_element_by_xpath('//*[@id="pickupLocation"]')
#botão pesquisar
btn_search = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/form/div[2]/undefined/div/div[2]/div/div/div[3]/div/button/span')
#limpar local de retirada
pickup_local.clear()
#digitar o local
pickup_local.send_keys('aeroporto')
#clicar no botão pesquisar
btn_search.click()
#aguardar carregamento da página
time.sleep(1)

#3º caso de teste: Usar a função autocompletar para o campo local de retirada
print('UC_003')
#limpar local de retirada
pickup_local.clear()
#digitar o local
pickup_local.send_keys('aeroporto Sao Luis')
#metódo para aguardar a pesquisa jquery do site 
time.sleep(3.0)
#encontrar o primeiro elemento que retorna do jquery 
pickup_local_autocomplete = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/form/div[2]/div[1]/div[1]/div/div[1]/fieldset/div/div/div/div[2]/ul/li[2]/button/div/h4') 
#clicar no primeiro elemento
pickup_local_autocomplete.click()
#tempo de espera rápido para envio das informações
time.sleep(0.5)
#clicar no botão pesquisar
btn_search.click()
#aguardar carregamento da página
time.sleep(1)

#4ºcaso de teste: digitar local de destino inválido
print('UC_004')
#campo para inserir local de retirada
destination_local = driver.find_element_by_xpath('//*[@id="dropoffLocation"]')
#limpar local de destino
destination_local.clear()
#digitar o local de destino
destination_local.send_keys('hotel')
#clicar no botão pesquisar
btn_search.click()
#aguardar carregamento da página
time.sleep(1)

#5º caso de teste: Usar a função autocompletar para o campo local de destino
print('UC_005')
#limpar local de destino
destination_local.clear()
#digitar o local de destino
destination_local.send_keys('Sao Luis hotel')
#metódo para aguardar a pesquisa jquery do site 
time.sleep(3.0)
#encontrar o primeiro elemento que retorna do jquery 
destination_local_autocomplete = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/form/div[2]/div[1]/div[1]/div/div[2]/fieldset/div/div/div/div[2]/ul/li[4]/button/div/h4') 
#clicar no primeiro elemento
destination_local_autocomplete.click()
#tempo de espera rápido para envio das informações
time.sleep(0.5)
#aguardar carregamento da página
time.sleep(1)

#6º caso de teste: Selecionar data de ida
print('UC_006')
#campo para inserir data de retirada
pickup_date = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/form/div[2]/div[1]/div[2]/div/div/div[1]/div/button')
#Clique para habilitar caledário
pickup_date.click()
#seleção de data
pickup_date_select_numb = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/form/div[2]/div[1]/div[2]/div/div/div[1]/div/div/div/div/div/table/tbody/tr[2]/td[4]/a')
pickup_date_select_numb.send_keys(Keys.RETURN)
time.sleep(1)

#7º caso de teste: Selecionar horário de partida na retirada
print('UC_007')
#campo para inserir horário de retirada
pickup_time = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/form/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div')
#Clique para habilitar select de horário
pickup_time.click()
#seleção de horário
pickup_time_select_hour = Select(driver.find_element_by_xpath('//*[@id="pickupHour"]'))
pickup_time_select_hour.select_by_value('13')
time.sleep(0.5)
pickup_time_select_minute = Select(driver.find_element_by_xpath('//*[@id="pickupMinute"]'))
pickup_time_select_minute.select_by_value('30')
time.sleep(0.5)
#clicar no botão confirm
btn_confirm = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/form/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/div/div/div/div/div/div/button/span')
btn_confirm.click()
time.sleep(1)

#8º caso de teste: Selecionar quantidade de passageiros
print('UC_008')
passenger = Select(driver.find_element_by_xpath('//*[@id="passengers"]'))
passenger.select_by_value('16')
time.sleep(1)

#9º caso de teste: Selecionar data de retorno
print('UC_009')
#campo para inserir data de retorno
return_date = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/form/div[2]/undefined/div/div[2]/div/div/div[1]/div/button/span')
#Clique para habilitar caledário
return_date.click()
#seleção de data
return_date_select_numb = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/form/div[2]/undefined/div/div[2]/div/div/div[1]/div/div/div/div/div/table/tbody/tr[3]/td[3]/a')
return_date_select_numb.send_keys(Keys.RETURN)
time.sleep(1)

#10º caso de teste: Selecionar horário de partida no retorno
print('UC_010')
#campo para inserir horário de retirada
return_time = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/form/div[2]/undefined/div/div[2]/div/div/div[2]/div/div[1]/div/button/span')
#Clique para habilitar select de horário
return_time.click()
#seleção de horário
return_time_select_hour = Select(driver.find_element_by_xpath('//*[@id="returnHour"]'))
return_time_select_hour.select_by_value('15')
time.sleep(0.5)
return_time_select_minute = Select(driver.find_element_by_xpath('//*[@id="returnMinute"]'))
return_time_select_minute.select_by_value('50')
time.sleep(0.5)
#clicar no botão confirm
btn_return = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/form/div[2]/undefined/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div/div/div/div/button/span')
btn_return.click()
#clicar no botão pesquisar
btn_search.click()

time.sleep(5)
driver.close()
