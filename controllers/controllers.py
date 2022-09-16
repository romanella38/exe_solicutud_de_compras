# -*- coding: utf-8 -*-
# from odoo import http


# class OrdenDeCompra(http.Controller):
#     @http.route('/orden_de_compra/orden_de_compra/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/orden_de_compra/orden_de_compra/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('orden_de_compra.listing', {
#             'root': '/orden_de_compra/orden_de_compra',
#             'objects': http.request.env['orden_de_compra.orden_de_compra'].search([]),
#         })

#     @http.route('/orden_de_compra/orden_de_compra/objects/<model("orden_de_compra.orden_de_compra"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('orden_de_compra.object', {
#             'object': obj
#         })
