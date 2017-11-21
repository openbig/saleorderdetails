# -*- encoding: utf-8 -*-
from openerp import models, fields, api, _

from pprint import pprint
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    print_image = fields.Boolean('Print Image', help="""If ticked, you can see
                    the product image in report of sale order/quotation""")
    image_sizes = fields.Selection([('image', 'Big sized Image'),
                                    ('image_medium', 'Medium Sized Image'),
                                    ('image_small', 'Small Sized Image')],
                                   'Image Sizes',
                                   default="image_small",
                                   help="Image size to be displayed in report")

class SaleOrderLine(models.Model):
    _inherit='sale.order.line'

    image_small = fields.Binary('Product Image',
                                related='product_id.image_small')
    purchase_description = fields.Text("Detailed Description")

    @api.onchange('product_id')
    
    def onchange_product_for_description(self):
        self.purchase_description = self.product_id and self.product_id.description_purchase or False
