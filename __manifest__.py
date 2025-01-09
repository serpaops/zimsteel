# -*- coding: utf-8 -*-
{
    'name': "zimsteel",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "SERPA",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'sale', 'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'models/custom_fields.xml',
        # 'data/form_view.xml',
        # 'views/views.xml',
        'views/templates.xml',
        'data/ir_model.xml',
        'data/ir_model_fields.xml',
        'data/ir_ui_view.xml',
        'data/ir_actions_act_window.xml',
        'data/ir_ui_menu.xml',
        'data/ir_model_access.xml',
        'data/ir_default.xml',     
        'actions/server.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

