# -*- coding: utf-8 -*-

# Import existing python modules created by Odoo
from odoo import models, fields, api      # You usually want to import these three

class Course(models.Model):     # Inherit abstract model: models.Model
    
    # Define model attributes
    _name = 'academy.course'           # Name of model
    _description = 'Course Info'       # Model Description
    
    # Initialize fields
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    level = fields.Selection(string='Level',
                             selection= [('beginner', 'Beginner'),
                                         ('intermediate', 'Inermediate'),
                                         ('advanced', 'Advanced')],
                            copy=False)  
    test = fields.Char(string='Test', required=False)
