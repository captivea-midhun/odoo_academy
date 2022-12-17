# -*- coding: utf-8 -*-

# Description: Holds the class representing our model


# Import existing python modules created by Odoo (These 3 are the most common odoo imports)
from odoo import models, fields, api

class Course(models.Model):     # Must inherit abstract model: models.Model
    """Represents a model in Odoo."""
    
    # --- Define model attributes ---
    _name = 'academy.course'           # Name of model (Technical name of model)
    _description = 'Course Info'       # Model Description
    
    # --- Initialize fields (referenced by view) ---
    # *'string' arg is what is seen by end user. If not set, odoo used field name 
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')

    level = fields.Selection(string='Level',
                             selection= [('beginner', 'Beginner'),
                                         ('intermediate', 'Intermediate'),
                                         ('advanced', 'Advanced')],
                            copy=False)  

    active = fields.Boolean(string='Active', default=True)
