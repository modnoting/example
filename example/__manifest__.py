# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Example Module',
    'version' : '14.0.0.0.1',
    'summary': 'Example Module',
    'sequence': 10,
    'description': """
Example Module
====================
""",
    'category': 'Example',
    'website': 'https://www.odoo.com/',
    'depends' : ['base', 'product'],
    'data': ['security/ir.model.access.csv',
             'views/report_reg.xml',
             ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
