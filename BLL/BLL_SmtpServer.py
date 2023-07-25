import smtplib
from email.mime.text import MIMEText
from BE import BE_SmtpServer


class SmtpServer(object):
    def __init__(self, server, port, mail, password):
        BE_SmtpServer.SmtpServer.setServer(self, server)
        BE_SmtpServer.SmtpServer.setPort(self, port)
        BE_SmtpServer.SmtpServer.setMail(self, mail)
        BE_SmtpServer.SmtpServer.setPassword(self, password)
        self.conexionSmtp = ""



    def conectarSmtp(self):
        try:
            smtp_obj = smtplib.SMTP(self.server, int(self.port))
            smtp_obj.starttls()
            smtp_obj.login(self.mail, self.password)
            BE_SmtpServer.SmtpServer.setConexionSmtp(self, smtp_obj)
        except Exception as e:
            print(e)
    
    def desconectarSmtp(self):
            self.conexionSmtp.quit()
            BE_SmtpServer.SmtpServer.setConexionSmtp(self, "")
        