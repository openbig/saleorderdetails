# -*- coding: utf-8 -*-
# Copyright 2017 Carlos Dauden <carlos.dauden@tecnativa.com>
# Copyright 2017 Thorsten Vocks <thorsten.vocks@openbig.org>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import _, api, fields, models
from openerp.exceptions import ValidationError


class ProductCatalogPrint(models.TransientModel):
    _name = "product.catalog.print"

    pricelist_id = fields.Many2one(
        comodel_name="product.pricelist", string="Pricelist"
    )
    partner_id = fields.Many2one(comodel_name="res.partner", string="Customer")
    show_variants = fields.Boolean()
    product_tmpl_ids = fields.Many2many(
        comodel_name="product.template",
        string="Products",
        help="Keep empty for all products",
    )
    product_ids = fields.Many2many(
        comodel_name="product.product",
        string="Products",
        help="Keep empty for all products",
    )
    show_image = fields.Boolean(string="Show Image")
    show_sale_price = fields.Boolean(string="Show Sale Price")
    show_list_price = fields.Boolean(string="Show List Price")

    @api.model
    def default_get(self, fields):
        res = super(ProductCatalogPrint, self).default_get(fields)
        if self.env.context.get("active_model") == "product.template":
            res["product_tmpl_ids"] = [
                (6, 0, self.env.context.get("active_ids", []))
            ]
        elif self.env.context.get("active_model") == "product.product":
            res["show_variants"] = True
            res["product_ids"] = [
                (6, 0, self.env.context.get("active_ids", []))
            ]
        elif self.env.context.get("active_model") == "product.pricelist":
            res["pricelist_id"] = self.env.context.get("active_id", False)
        elif self.env.context.get("active_model") == "res.partner":
            res["partner_id"] = self.env.context.get("active_id", False)
            partner = self.env["res.partner"].browse(
                self.env.context.get("active_id", False)
            )
            res["pricelist_id"] = partner.property_product_pricelist.id
        return res

    @api.multi
    def print_report(self):
        if not (self.pricelist_id or self.show_sale_price):
            raise ValidationError(
                _("You must set price list or any show price option.")
            )
        return self.env["report"].get_action(
            self, "product_catalog_print.report_product_catalog"
        )
