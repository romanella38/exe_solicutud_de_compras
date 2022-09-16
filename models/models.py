# -*- coding: utf-8 -*-

from odoo import models, fields, api

class bank(models.Model):
    _inherit = 'purchase.order'

    bank_partner_id = fields.Many2one('res.partner.bank')
    entrega = fields.Char('Dirección de entrega')

    





# class orden_de_compra(models.Model):
#     _name = 'orden_de_compra.orden_de_compra'
#     _description = 'orden_de_compra.orden_de_compra'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
