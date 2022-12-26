# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    """xxx"""

    # Specify the model that you are inheriting from (In this case, it is the sales app)
    _inherit= 'sale.order'

    # Access the session ID that is associated with this order
    # Each sales order can have a related session
    session_id = fields.Many2one(comodel_name='academy.session', string='Related Session', ondelete='set null')

    instructor_id = fields.Many2one(string='Session Instructor', related='session_id.instructor_id')
    