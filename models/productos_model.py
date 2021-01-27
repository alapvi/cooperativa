# -*- coding: utf-8 -*-

from odoo import models, fields, api
class productos_model(models.Model):
     _name = 'cooperativa.productos_model'
     _description = 'Modelo de Productos'
     _sql_constraints = [("sql_cons_check_name_producto","UNIQUE(name)","Error en producto. El nombre del producto ya existe!"),]

     name = fields.Char(string="Nombre", required=True,index=True)
     descripcion = fields.Html(string="Descripción",required=True)
     precio = fields.Float(string="Precio",required=True)
     kilosTotales = fields.Float(string="Kilos totales", readonly=True, default=0)
     
     @api.constrains("precio")
     def checkPrecio(self):
          self.ensure_one()
          if self.precio <= 0:
               raise ValueError("Precio de producto erróneo!")

     def limpiaKilos(self):
          productos = self.search([])
          for rec in productos:
               rec.kilosTotales = 0


