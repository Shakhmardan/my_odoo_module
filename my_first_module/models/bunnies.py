from odoo import api, fields, models


class Bunnies(models.Model):
    _name = "bunnies"
    _description = "Funs of NWJNS(just for fun,for the first test module)"

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
