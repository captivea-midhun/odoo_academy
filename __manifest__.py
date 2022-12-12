# -*- coding: utf-8 -*-
{
    'name': 'Odoo Academy',
    
    'summary': """Academy app to manage training""",
    
    'description': """
        Academy Module eto manage Training:
        - Courses
        - Sessions
        - Attendees
        """,
    
    'author': 'Odoo',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [       # Note that Odoo loads files in the order you specify
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml'
    ],
    
    'demo': [                       # How to link .xml files to the manifest
        'demo/academy_demo.xml'
    ],

}