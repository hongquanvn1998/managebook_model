from odoo import fields,models,api

class member(models.Model):
    _name = 'managebook.member'
    _inherit = 'managebook.mybook'
    user_id = fields.Many2one('res.users')
    
