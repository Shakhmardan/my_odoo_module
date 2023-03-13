from odoo import api, fields, models


class Products(models.Model):
    _name = "products"
    _description = "Products"

    name = fields.Char(string='Product')
    price = fields.Integer(string='Price')
