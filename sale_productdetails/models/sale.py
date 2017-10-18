# -*- encoding: utf-8 -*-
from openerp import models, fields, api, _

from pprint import pprint
import logging

_logger = logging.getLogger(__name__)

class SaleOrderLine(models.Model):
    _inherit='sale.order.line'

    purchase_description = fields.Text("Detailed Description")

    @api.onchange('product_id')
    def onchange_product_for_description(self):
        self.purchase_description = self.product_id and self.product_id.description_purchase or False
