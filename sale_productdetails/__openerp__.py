# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2017 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name" : "Detailed product description on Sale Order report.",
    "version" : "0.02 (9.0)",
    "author" : "Thorsten Vocks, Maciej Wichowski - OpenGLOBE",
    "website": "https://www.openbig.org",
    "category" : "Sale",
    'summary': 'New report for Sale Order with detailed product description',
    'depends' : ['sale', 'purchase'],
    'description':"""
====================
Detailed description
====================

This module adds field, functionality and new report required to show detailed description for product on Sale Order report.
============================================================================================================================

Fields:
-------
* **Detailed Description**:

Reports:
--------

* **Quotation / Sale Order (Details)**

""",
    'data': [
        'views/sale_view.xml',
        'views/report_saleorder.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
