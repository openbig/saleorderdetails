# Copyright 2017 Carlos Dauden <carlos.dauden@tecnativa.com>
# Copyright 2017 Thorsten Vocks <thorsten.vocks@openbig.org>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Product Catalog Print",
    "summary": "Print product catalog with image, short name and detailed "
    "description from separate menu option, each product "
    "represents one single side in the printed product catalog.",
    "version": "12.0.1.0.0",
    "category": "Product",
    "website": "http://www.openbig.org",
    "author": "OpenBIG.org, " "Tecnativa, " "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": ["product","sale","purchase"],
    "data": [
        "views/report_product_catalog.xml",
        "wizards/product_catalog_print_view.xml",
    ],
}
