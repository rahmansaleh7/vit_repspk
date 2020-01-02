# -*- coding: utf-8 -*-
from odoo import http

# class VitRepspk(http.Controller):
#     @http.route('/vit_repspk/vit_repspk/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_repspk/vit_repspk/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_repspk.listing', {
#             'root': '/vit_repspk/vit_repspk',
#             'objects': http.request.env['vit_repspk.vit_repspk'].search([]),
#         })

#     @http.route('/vit_repspk/vit_repspk/objects/<model("vit_repspk.vit_repspk"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_repspk.object', {
#             'object': obj
#         })