# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': "Product Image On Invoice/Vendor Bill/Sale/Purchase Line",
    'version': "16.0.0.0",
    'category': "Accounting",
    'license': 'OPL-1',
    'price': '12.0',
    'currency': 'USD',
    'summary': "Display product image on invoice line print product image on invoice report print image on invoice line product image print product image on invoice line product image in invoice line print Product image on vendor bill line",
    'description': """
						
			Display product image on invoice/vendor bill/Purchase/Sale line. It will also display product image on invoice/vendor bill/Purchase/Sale report. 
			
			Product Image On Invoice/Vendor/Purchase/Sale Bill Line in odoo,
			Invoice/Vendor bill report with product image in odoo,
			Product image on invoice/vendor bill/Purchase/Sale line and invoice/vendor bill/Purchase/Sale report in odoo,
			Identify product via image in odoo,
			Identify priduct via image on invoice/vendor bill/Purchase/Sale report in odoo,

	""",
    'author': "Tinton Aji Sadewo",
    "website": "https://tintonajisadewo.github.io/",
    'depends': ['base', 'account', 'sale_management', 'purchase'],
    'data': [
        'report/invoice_report.xml',
        'report/purchase_report.xml',
        'report/sale_report.xml',
        'views/view_invoice.xml',
        'views/view_purchase.xml',
        'views/view_sale.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
    "images": ['static/description/Banner.gif'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
