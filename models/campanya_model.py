# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
class campanya_model(models.Model):
     _name = 'cooperativa.campanya_model'
     _description = 'Modelo de Campañas'

     fecha = fields.Datetime(string="Fecha",default=lambda self: datetime.now(), required=True)
     campaña = fields.Char(string="Campaña",default=lambda self: datetime.now().year,readonly="True",required=True)
     socio = fields.Many2one("cooperativa.socios_model", required=True)
     producto = fields.Many2one("cooperativa.productos_model", required=True)
     kilos = fields.Float(string="Cantidad")
     active = fields.Boolean(readonly=True, default=True)

     @api.constrains("kilos")
     def actualizaSalario(self):
          self.ensure_one()
          if self.kilos <= 0:
               raise ValueError("Los kilos deben contener un valor positivo")
          
     def actualizaSaldos(self):
          sociosPorContabilizar = self.search([("active","=","True")])
          for rec in sociosPorContabilizar:
               rec.socio.saldo += rec.kilos*(rec.producto.precio)
               rec.active=False
     
     def actualizaKilos(self):
          registros = self.search([("active","=","True")])
          for rec in registros:
               rec.producto.kilosTotales += rec.kilos
               

     def eliminaHistorial(self):
          historialSocios = self.search([("active","=","False")])
          for rec in historialSocios:
               rec.unlink()






