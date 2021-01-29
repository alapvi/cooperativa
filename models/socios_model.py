# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from time import time
from odoo.exceptions import ValidationError
class socios_model(models.Model):
     _name = 'cooperativa.socios_model'
     _description = 'Modelo de Socios'
     _sql_constraints = [("sql_cons_check_dni_socio","UNIQUE(dni)","Error en socio. El dni del socio ya existe!"),
                         ("sql_cons_check_id_socio","UNIQUE(id_socio)","Error en socio. El id  del socio ya existe!"),]

     id_socio = fields.Char(string="Id Socio",readonly=True,index=True,default=str(int(time())))
     foto = fields.Binary()
     name = fields.Char(string="Nombre")
     apellidos = fields.Char(string="Apellidos")
     dni = fields.Char(string="DNI",size=9,index=True)
     fechaAlta = fields.Date(string="Fecha", default=lambda self: datetime.today())
     telf = fields.Char(string="Teléfono", size=9)
     email = fields.Char(string="email")
     saldo = fields.Float(string="Saldo",readonly=True)
     registros = fields.One2many("cooperativa.campanya_model","socio",string="Registros Pendientes",readonly=True)

     @api.constrains("telf")
     def checkTelf(self):
          if len(self.telf) != 9:
               raise ValidationError("Error en teléfono. Debe contener 9 dígitos")

     @api.constrains("dni")
     def checkDni(self):
          letra = self.dni[-1]
          num = self.dni[:-1]
          posicion = num%23
          if len(self.dni) != 9:
               raise ValidationError("Error en dni")


               


