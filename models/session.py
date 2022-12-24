# -*- coding: utf-8 -*-

# Description: Holds the class representing the model

from odoo import fields, api, models
from datetime import timedelta

class Session(models.Model):
    _name = 'academy.session'
    _description = 'Session model'

    # Many sessions can be associated with a single course, so we will use a many2one field
    # *It is convention to add _id to the end of the variable name of the many2one field
    # *Setting ondelete to 'cascade' ensure that if course id of the Course model is deleted, this field will also be deleted
    # *Setting required to True ensures that every session that is created will have a course ID associated with it
    course_id = fields.Many2one(comodel_name='academy.course', string='Course', ondelete='cascade', required=True)

    # This will access the name of the associated course
    name = fields.Char(string='Title', related='course_id.name')

    # Many sessions can be taught by one instructor
    # Built into odoo, we have a model called res.partner.... ?
    instructor_id = fields.Many2one(comodel_name='res.partner', string='Instructor')

    # A student can attend many sessions and a session can have multiple students
    student_ids = fields.Many2many(comodel_name='res.partner', string='Students')

    start_date = fields.Date(string='Start Date', default=fields.Date.today)

    duration = fields.Integer(string='Session days', default=1)

    end_date = fields.Date(string='End date', compute='_compute_end_date', inverse='_inverse_end_date', stored=True)

    @api.depends('start_date', 'duration')
    def _compute_end_date(self):
        """Compute function to update end_date. This will run if either start_date or duration is updated."""
        for rec in self:
            if not rec.start_date and rec.duration:
                rec.end_date = rec.start_date
            else:
                duration = timedelta(days=rec.duration)
                rec.end_date = rec.start_date + duration
    
    def _inverse_end_date(self):
        """xxx"""
        for rec in self:
            if rec.start_date and rec.end_date:
                rec.duration = (rec.end_date - rec.start_date).days + 1      
            else:
                continue 