# -*- coding: utf-8 -*-
{
    'name': "zimsteel",

    'summary': "Module for invoice and qoutation for the client Zimsteel",

    'description': """
    Module for Zimsteel
    ===================

    This module is specific to SERPA and its client Zimsteel. It provides customizations
    to the invoice and quotation reports.
    
    """,

    'author': "SERPA",
    'website': "https://github.com/serpaops/zimsteel",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'sale', 'product'],

    # always loaded
    'data': [
        'data/ir_model.xml',
        'data/ir_model_fields.xml',
        'data/ir_ui_view.xml',
        'data/ir_actions_act_window.xml',
        'data/ir_ui_menu.xml',
        'data/ir_model_access.xml',
        'data/ir_default.xml',     
        'actions/server.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

