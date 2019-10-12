# Copyright 2017 Carlos Dauden <carlos.dauden@tecnativa.com>
# Copyright 2017 Thorsten Vocks <thorsten.vocks@openbig.org>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests.common import SavepointCase
from odoo.exceptions import ValidationError


class TestProductCatalogPrint(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super(TestProductCatalogPrint, cls).setUpClass()
        cls.pricelist = cls.env.ref("product.list0")
        cls.product = cls.env["product.product"].create(
            {"name": "Product for test", "default_code": "TESTPROD01"}
        )

        cls.partner = cls.env["res.partner"].create(
            {
                "name": "Partner for test",
                "property_product_pricelist": cls.pricelist.id,
            }
        )

        cls.wiz_obj = cls.env["product.catalog.print"]

    def test_defaults(self):
        wiz = self.wiz_obj.new()
        res = wiz.with_context(
            active_model="product.pricelist", active_id=self.pricelist.id
        ).default_get([])
        self.assertEqual(res["pricelist_id"], self.pricelist.id)
        res = wiz.with_context(
            active_model="res.partner", active_id=self.partner.id
        ).default_get([])
        self.assertEqual(
            res["pricelist_id"], self.partner.property_product_pricelist.id
        )
        res = wiz.with_context(
            active_model="product.template",
            active_ids=self.product.product_tmpl_id.ids,
        ).default_get([])
        self.assertEqual(
            res["product_tmpl_ids"][0][2], self.product.product_tmpl_id.ids
        )
        res = wiz.with_context(
            active_model="product.product", active_ids=self.product.ids
        ).default_get([])
        self.assertEqual(res["product_ids"][0][2], self.product.ids)
        self.assertTrue(res["show_variants"])

        with self.assertRaises(ValidationError):
            wiz.print_report()

        wiz.show_sale_price = True
        res = wiz.print_report()
        self.assertIn("report_name", res)
