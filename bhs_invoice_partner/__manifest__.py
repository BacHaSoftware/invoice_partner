# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Invoice currency by customer',
    'author': 'Bac Ha Software',
    'website': 'https://bachasoftware.com',
    'maintainer': 'Bac Ha Software',
    'version': '1.0',
    'category': 'Invoice',
    'sequence': 75,
    'summary': 'Invoice currency by customer',
    'description': "Invoice currency by customer",
    'depends': ['account'],
    'data': ['views/res_partner.xml'],
    "external_dependencies": {},
    'images': ['static/description/banner.gif'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
}
