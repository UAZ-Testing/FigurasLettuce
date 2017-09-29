# -*- coding: utf-8 -*-

from lettuce import step, world
from figuras import Figuras


@step(u'Dado que ingreso el número "([^"]*)"')
def dado_que_ingreso_el_numero_group1(step, numero):
    world.figuras = Figuras()
    world.numero = float(numero)


@step(u'cuando calculo el área del cuadrado')
def cuando_calculo_el_area(step):
    world.resultado = world.figuras.obtener_area_cuadrado(world.numero)


@step(u'entonces obtengo el resultado "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, resultado):
    assert float(resultado) == world.resultado, 'El resultado esperado es ' + \
                                                resultado + ' y el obtenido es ' + \
                                                resultado


@step(u'Dado que ingreso los números "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_y_group2(step, base, altura):
    world.base = float(base)
    world.altura = float(altura)


@step(u'cuando calculo el área del rectángulo')
def cuando_calculo_el_area_del_rectangulo(step):
    world.resultado = world.figuras.obtener_area_rectangulo(world.base,
                                                            world.altura)


@step(u'cuando calculo el área del círculo')
def cuando_calculo_el_area_del_circulo(step):
    world.resultado = world.figuras.obtener_area_circulo(world.numero)
