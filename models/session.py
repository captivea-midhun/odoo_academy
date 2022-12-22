# -*- coding: utf-8 -*-

# Description: Holds the class representing the model

from odoo import fields, api, models

class Session(models.Model):
    _name = 'academy.session'
    _description = 'Session info'

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