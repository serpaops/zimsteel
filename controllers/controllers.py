# -*- coding: utf-8 -*-
# from odoo import http


# class Zimsteel(http.Controller):
#     @http.route('/zimsteel/zimsteel', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zimsteel/zimsteel/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('zimsteel.listing', {
#             'root': '/zimsteel/zimsteel',
#             'objects': http.request.env['zimsteel.zimsteel'].search([]),
#         })

#     @http.route('/zimsteel/zimsteel/objects/<model("zimsteel.zimsteel"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zimsteel.object', {
#             'object': obj
#         })

