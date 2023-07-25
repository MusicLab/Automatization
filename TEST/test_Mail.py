import unittest
import pandas as pd
import smtplib

from BLL import BLL_Cliente
from BLL import BLL_Fecha
from BLL import BLL_Archivo
from BLL import BLL_Log
from BLL import BLL_SmtpServer
from DAL import DAL_Mapper_Hash
from DAL import DAL_Mapper_Archivo
from DAL import DAL_Mapper_Log
from DAL import DAL_Mapper_Request
from DAL import DAL_Mapper_Cliente
from DAL import DAL_Mapper
from DAL import DAL_Mapper_Eventos
from DAL import DAL_Conexion



class Test_Mail(unittest.TestCase):

    def test_ConexionMailSMTP(self):
        
        smtpServer = BLL_SmtpServer.SmtpServer("smtp.outlook.com", "587", "soccrate@outlook.com", "Kilometraje32")
        smtpServer.conectarSmtp()
        self.assertEqual(type(smtpServer.conexionSmtp), smtplib.SMTP)
        
        smtpServer.desconectarSmtp()
        self.assertEqual(smtpServer.conexionSmtp, "")
        



    