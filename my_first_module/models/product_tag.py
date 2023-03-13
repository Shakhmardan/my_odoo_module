from odoo import api, fields, models

class ProductTag(models.Model):
    _name = "product.tag"
    _description = "Product Tag"

    name = fields.Char(string='Name')
    color = fields.Integer(string='Color')
    # color_2 = fields.Char(string='Color')
