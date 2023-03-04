# -*- coding: utf-8 -*-
# Part of Browseinfo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    image_128 = fields.Image(
        string="Image", compute="_onchange_product_images")

    @api.depends('product_id')
    def _onchange_product_images(self):
        for line in self:
            line.image_128 = line.product_id.image_128
