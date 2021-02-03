# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from time import time
from odoo.exceptions import ValidationError
class socios_model(models.Model):
     _name = 'cooperativa.socios_model'
     _description = 'Modelo de Socios'
     _order="apellidos"
     _sql_constraints = [("sql_cons_check_dni_socio","UNIQUE(dni)","Error en socio. El dni del socio ya existe!"),
                         ("sql_cons_check_id_socio","UNIQUE(id_socio)","Error en socio. El id  del socio ya existe!"),]

     id_socio = fields.Char(string="Id Socio",readonly=True,index=True,default=str(int(time())))
     foto = fields.Binary()
     name = fields.Char(string="Nombre", required=True)
     apellidos = fields.Char(string="Apellidos")
     dni = fields.Char(string="DNI",size=9,index=True)
     fechaAlta = fields.Date(string="Fecha", default=lambda self: datetime.today())
     telf = fields.Char(string="Teléfono", size=9, required=True)
     email = fields.Char(string="email", required=True)
     saldo = fields.Float(string="Saldo",readonly=True)
     registros = fields.One2many("cooperativa.campanya_model","socio",string="Registros Pendientes",readonly=True)

     @api.constrains("telf")
     def checkTelf(self):
          if len(self.telf) != 9:
               raise ValidationError("Error en teléfono. Debe contener 9 dígitos")

     @api.constrains('dni')
     def validate_dni(self):
        if not self.check_DNI(self.dni):
            raise ValidationError("Error en DNI!!!!")
    
     def check_DNI(self, ndni):
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        dig_ext = "XYZ"
        reemp_dig_ext = {'X':'0', 'Y':'1', 'Z':'2'}
        numeros = "1234567890"
        dni = ndni.upper()
        if len(dni) == 9:
            dig_control = dni[8]
            dni = dni[:8]
            if dni[0] in dig_ext:
                dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
            return len(dni) == len([n for n in dni if n in numeros]) \
                and tabla[int(dni)%23] == dig_control
        return False



               


