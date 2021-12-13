# Enter feature name here
Feature: Buscar producto

# Enter feature description here
  Como usuario
  Quiero buscar un perfume para hombre

  # Enter scenario name here
Scenario: Busco un perfume determinado para hombre en la pagina
    # Enter steps here
  Given la pagina de venta

  When se completa el "Init2021" y "2021Sabado"
  And mi cuenta de usuario se muestra en pantalla
  And busco el perfume para hombre

  Then encuentro el perfume "Pour Homme Eau de Toilette" para hombre