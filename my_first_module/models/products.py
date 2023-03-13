from odoo import api, fields, models


class Products(models.Model):
    _name = "products"
    _description = "Products"

    product_id = fields.Many2one('products', string='Product')
    name = fields.Char(string='Product')
    price = fields.Integer(string='Price')
    price_unit = fields.Integer(related='product_id.price')
    quantity = fields.Integer(string='Quantity', default=1)
    shop_id = fields.Many2one('shop', string='Shop')
    tag_ids = fields.Many2many('product.tag', string="Tags")