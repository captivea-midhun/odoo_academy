# -*- coding: utf-8 -*-

# Description: Holds the class representing our model

from odoo import models, fields, api   # Import python modules for Odoo (These 3 are the most common odoo imports)
from odoo.exceptions import UserError, ValidationError     # For errors

class Course(models.Model):     # Must inherit abstract model: models.Model
    """Represents a model in Odoo."""
    
    # --- Define model attributes ---
    _name = 'academy.course'           # Name of model (Technical name of model)
    _description = 'Course model'       # Model Description
    
    # --- Initialize fields (referenced by view) ---
    # *'string' attribute  is what is seen by end user. If not set, odoo uses the field name (aka variable name)
    # * 'required' attribute specifes whether the field must/not be filled in
    name = fields.Char(string='Title', required=True)

    description = fields.Text(string='Description')

    test1 = fields.Text(string='Stuff')

    # The Selection field ...?
    # * 'selection' attribute hold a list containing an array of tuples. Each tuple has the format: ...?
    level = fields.Selection(string='Level',
                             selection= [('beginner', 'Beginner'),
                                         ('intermediate', 'Intermediate'),
                                         ('advanced', 'Advanced')],
                            copy=False)  

    active = fields.Boolean(string='Active', default=True)

    base_price = fields.Float(string='Base Price', default=0.00)

    additional_fee = fields.Float(string='Additional Fee', default=10.00)

    total_price = fields.Float(string='Total Fee', readonly=True)

    # Each course will be associated with multiple sessions, so we use a one2many field
    # *Note the conventinal use of _ids at the end of the variable names
    # *Note that the inverse_name is the name of the corresponding many2one field in the session model
    session_ids = fields.One2many(comodel_name='academy.session', inverse_name='course_id', string='Sessions')



    # Onchange decorator (This will immediately (real time) update the price of total_price if base_price or additinal_fee is updated)
    @api.onchange('base_price', 'additional_fee')
    def _onchange_total_price(self):
        """Dynamically changes the total_price value when base_price or additional_fee is changed."""
        # Raise UserError
        if self.base_price < 0.00:
            raise UserError('Base Price cannot be set as Negative.')          
        self.total_price = self.base_price + self.additional_fee


    # Constraints decorator (This will trigger the specified action when when the user submits a from)
    @api.constrains('additional_fee')
    def _check_additional_fee(self):
        """xxx""" 

        raise UserError(str(len(self)))
        for record in self:  # Loops through each record
            # Raise validation error
            if record.additional_fee < 10.00:
                raise ValidationError('Additional Fees cannot be less than 10.00: %s' % record.additional_fee)
