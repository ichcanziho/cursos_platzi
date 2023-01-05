# Curso de Selenium enfocado a la automatización de Procesos

## Objetivos del curso:

### Aprender qué es Selenium

<b>¿Qué es Selenium?</b>
Es una SUIT de herramientas para la automatización de navegadores Web.
El objetivo de Selenium NO fue para el Testing ni para el Web Scraping (aunque se puede usar para eso), por lo tanto, no es el más optimo para estas actividades.
Protocolo: WebDriver, herramienta que se conecta a un API.
Selenium WebDriver es la herramienta que utilizaremos en el curso.
-Selenium NO es un Software, ES una SUIT de Softwares.
*DDT: Data Drive Testing: Ingresar datos para que realice varias pruebas (sin intervención humana).

## Preparando SELENIUM

* pip install selenium
* pip install pyunitreport
* pip install html-testRunner


## Unittest (PyTest)

* <b> Test Fixture: </b> Preparaciones para antes y después de la prueba
* <b> Test Case: </b> Unidad de código a probar
* <b> Test Suite: </b> Colección de Test Cases
* <b> Test Runner: </b> Orquestador de la ejecución
* <b> Test Reporte: </b> Resumen de resultados

## Estructura de un sitio
![estructura](./imgs/estructura.png "estructura")  


## Selectores

* ID
* Nombre del atributo
* Nombre de la clase
* Nombre de la etiqueta
* XPath
* Selector de CSS
* Texto del link
* Texto parcial del link

# C3: Preparar assertions y test suit

### Assertions

Métodos que permiten validar un valor esperado en la ejecución del test. Si el resultado es verdadero el test continúa,
en caso contrario "falla" y termina. 

### Test Suits

Colección de test unificados en una sola prueba, permitiendo tener resultados grupales e individuales.

![test_suit](./imgs/test_suit.png "test_suit")  

------------------------

# WebDriver y WebElement
## Clase WebDriver
Cuenta con una serie de propiedades y métodos para interactuar directamente con la ventana del navegador y sus elementos relacionados, como son pop-ups o alerts. Por ahora nos centraremos a las más utilizadas.

### Propiedades de la clase WebDriver

| Propiedad | Descripción | Ejemplo|
|-----------|-------------|--------|
|current_url	|Obtiene la URL del sitio en la que se encuentra el navegador	|driver.get_url|
|current_window_handle	|Obtiene la referencia que identifica a la ventana activa en ese momento	|driver.current_window_handle|
|name	|Obtiene el nombre del navegador subyacente para la instancia activa	|driver.name|
|orientation	|Obtiene la orientación actual del dispositivo móvil	|driver.orientation|
|page_source	|Obtiene el código fuente de disponible del sitio web	|driver.page_source|
|title	|Obtiene el valor de la etiqueta <title> del sitio web	|driver.title|
## Clase WebElement
Esta clase nos permite interactuar específicamente con elementos de los sitios web como textbox, text area, button, radio button, checkbox, etc.



## Propiedades más comunes de la clase WebElement
| Propiedad | Descripción                                        | Ejemplo         |
|-----------|----------------------------------------------------|-----------------|
| size      | Obtiene el tamaño del elemento                     | login.size      |
| tag_name	 | Obtiene el nombre de la etiqueta HTML del elemento | 	login.tag_name |
| text	     | Obtiene el texto del elemento	                     | login.text      |

## Métodos más comunes de la clase WebElement

|Método|Descripción| Ejemplo                                                                  |
|------|-----------|--------------------------------------------------------------------------|
|clear()	|Limpia el contenido de un textarea	| first_name.clear()                                                       |
|click()	|Hace clic en el elemento	| send_button.click()                                                      |
|get_attribute(name)	|Obtiene el valor del atributo de un elemento	| submit_button.get_attribute(‘value’) last_name.get_attribute(max_length) |
|is_displayed()	|Verifica si el elemento está a la vista al usuario	| banner.is_displayed()                                                    |
|is_enabled()	|Verifica si el elemento está habilitado	| radio_button.is_enabled()                                                |
|is_selected()	|Verifica si el elemento está seleccionado, para el caso de checkbox o radio button	| checkbox.is_selected()                                                   |
|send_keys(value)	|Simula escribir o presionar teclas en un elemento	| email_field.send_keys(‘team@platzi.com’)                                 |
|submit()	|Envía un formulario o confirmación en un text area	| search_field.submit()                                                    |
|value_of_css_property(property_name)	|Obtiene el valor de una propiedad CSS del elemento	| header.value_of_css_property(‘background-color’)                         |
|clear()	|Limpia el contenido de un textarea	| first_name.clear()                                                       |
|click()	|Hace clic en el elemento	|send_button.click()|
|get_attribute(name)	|Obtiene el valor del atributo de un elemento	|submit_button.get_attribute(‘value’) last_name.get_attribute(max_length)|
|is_displayed()	|Verifica si el elemento está a la vista al usuario	|banner.is_displayed()|
|is_enabled()	|Verifica si el elemento está habilitado	|radio_button.is_enabled()|
|is_selected()	|Verifica si el elemento está seleccionado, para el caso de checkbox o radio button	|checkbox.is_selected()|
|send_keys(value)	|Simula escribir o presionar teclas en un elemento	|email_field.send_keys(‘team@platzi.com’)|
|submit()	|Envía un formulario o confirmación en un text area	|search_field.submit()|
|value_of_css_property(property_name)	|Obtiene el valor de una propiedad CSS del elemento	|header.value_of_css_property(‘background-color’)|

# Demoras

### Implícita
Busca uno o varios elementos en el DOM si no se encuentran disponibles por la cantidad de tiempo asignado
### Explícita
Utiliza condiciones de espera determinadas y continúa hasta que se cumplan
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://somedomain/url_that_delays_loading")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    driver.quit()
```
### Condiciones explicitas
* title_is
* title_contains
* presence_of_element_located
* visibility_of_element_located
* visibility_of
* presence_of_all_elements_located
* text_to_be_present_in_element
* text_to_be_present_in_element_value
* frame_to_be_available_and_switch_to_it
* invisibility_of_element_located
* element_to_be_clickable
* staleness_of
* element_to_be_selected
* element_located_to_be_selected
* element_selection_state_to_be
* element_located_selection_state_to_be
* alert_is_present

```python
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))
```

https://selenium-python.readthedocs.io/waits.html
