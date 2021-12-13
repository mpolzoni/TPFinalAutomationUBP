# Enter feature name here
Feature: Mostrar pagina de producto

# Enter feature description here
  Como usuario de la pagina de compras
  quiero ver la página de mi producto buscado

  # Enter scenario name here
Scenario: Se muestra la pagina de mi producto
    # Enter steps here
  Given la pagina de venta

  When se completa el "Init2021" y "2021Sabado"
  And mi cuenta de usuario se muestra en pantalla
  And busco el perfume para hombre
  And selecciono un producto

  Then se muestra la pagina del producto
