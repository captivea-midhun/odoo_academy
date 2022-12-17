# -*- coding: utf-8 -*-

# Description: This file, __manifest__.py will hold the metadata for the module as well as link to other files in the module


{
    'name': 'Odoo Academy',
    
    'summary': """Academy app to manage training""",
    
    'description': """
        Academy Module to manage Training:
        - Courses
        - Sessions
        - Attendees
        """,
    
    'author': 'Odoo',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [       # How you link xml files to manifest. Note that Odoo loads files in the order you specify
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        # 'views/academy_menuitems.xml',
        # 'views/course_views.xml', These are individual form views that can work
    ],
    
    'demo': [                       # How to link demo .xml files to the manifest
        'demo/academy_demo.xml',
    ],
}