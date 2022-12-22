# -*- coding: utf-8 -*-

# Description: This file, __manifest__.py will hold the metadata for the module as well as link to other files in the module


{
    # Name of module
    'name': 'Odoo Academy',
    
    # Summary of module
    'summary': """Academy app to manage training""",
    
    # A Description of module
    'description': """
        Academy Module to manage Training:
        - Courses
        - Sessions
        - Attendees
        """,
    
    # Author of module
    'author': 'Odoo',
    
    # Website of your company
    'website': 'https://www.odoo.com',
    
    # Category of module
    'category': 'Training',
    
    # Version of module
    'version': '0.1',
    
    # Specify any other modules neccessary for this module to function
    'depends': ['base'],
    
    # Specifies .xml files. (How you link xml files to manifest. Note that Odoo loads files in the order you specify)
    'data': [       
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'demo/academy_demo.xml',   # Temporary placement
    ],
    
    # Specifies demo .xml files.
    'demo': [                       # How to link demo .xml files to the manifest
        # 'demo/academy_demo.xml',
    ],
}