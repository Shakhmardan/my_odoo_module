from odoo import api, fields, models


class Shop(models.Model):
    _name = "shop"
    _description = "Shop"

    bunny_id = fields.Many2one('bunnies', string='Bunny')
    product_id = fields.Many2one('products', string='Product')