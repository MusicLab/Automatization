import unittest
from BLL import BLL_Fecha
import datetime
import time


class Test_Fecha(unittest.TestCase):
    fecha = BLL_Fecha.Fecha()

    def test_ahora(self): 
        self.assertEqual(self.fecha.ahora().strftime('%m%d%y'), datetime.datetime.now().strftime('%m%d%y'))

    def test_ayer(self):
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        self.assertEqual(self.fecha.fechaInicio("diario").strftime('%m%d%y'), yesterday.strftime('%m%d%y'))

    def test_fechaInicio(self):
        atras15 = datetime.datetime.now() - datetime.timedelta(days=15)
        self.assertEqual(self.fecha.fechaInicio("diario", 15).day, atras15.day)

    def test_fechaInicioMensual(self):
        print(self.fecha.fechaInicio("mensual"))
        self.assertEqual(type(self.fecha.fechaInicio("mensual")), datetime.datetime)

    def test_fechaInicioSemanal(self):
        print(self.fecha.fechaInicio("semanal", 2))
        self.assertEqual(type(self.fecha.fechaInicio("semanal", 2)), datetime.datetime)
    

    def test_fechaFin(self):
        ayer = datetime.datetime.now() - datetime.timedelta(days=1)
        self.assertEqual(self.fecha.fechaFin().day,ayer.day)

    def test_isoFormat(self):
        fecha = self.fecha.isoFormat()
        self.assertEqual(type(fecha), str)

    def test_pasoTiempo(self):
        fechaInicio = BLL_Fecha.Fecha().fechaInicio("mensual")
        fechaFin = BLL_Fecha.Fecha().fechaFin()
        print(fechaInicio, fechaFin, BLL_Fecha.Fecha().ahora())
        time.sleep(5)
        print(fechaInicio, fechaFin, BLL_Fecha.Fecha().ahora())



