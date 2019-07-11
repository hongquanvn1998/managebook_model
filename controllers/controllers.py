# -*- coding: utf-8 -*-
from odoo import http

class Managebook(http.Controller):
    @http.route('/managebook/sale', auth='public')
    def index(self, **kw):
        books = http.request.env['managebook.mybook'].search([('id','=',1)])

        return http.request.render('managebook.mainpage',{'books':books})

class Hello(http.Controller):
    @http.route('/helloworld', auth='public')
    def helloworld(self):
        return('<h1>Hello World!</h1>')

#     @http.route('/managebook/managebook/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('managebook.listing', {
#             'root': '/managebook/managebook',
#             'objects': http.request.env['managebook.managebook'].search([]),
#         })

#     @http.route('/managebook/managebook/objects/<model("managebook.managebook"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('managebook.object', {
#             'object': obj
#         })