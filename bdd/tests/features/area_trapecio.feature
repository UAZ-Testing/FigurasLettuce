Feature: Área de un trapecio
  Como usuario del programa
  deseo calcular el área de un trapecio
  con la finalidad de obtener el resultado correcto

  Scenario: Área trapecio de 5 de base menor, 10 de base mayor y 10 de altura
  Dado que ingreso los números "5", "10" y "10"
  cuando calculo el área del trapecio
  entonces obtengo el resultado "75"

  Scenario: Área trapecio de 10 de base menor, 100 de base mayor y 5 de altura
  Dado que ingreso los números "10", "100" y "5"
  cuando calculo el área del trapecio
  entonces obtengo el resultado "275"