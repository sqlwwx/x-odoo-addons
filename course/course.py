# -*- coding: utf-8 -*-

import pytz
from datetime import timedelta
from openerp import models, fields, api, _, exceptions
from openerp.exceptions import Warning

class course(models.Model):
    _name = 'course.course'
    _description = "Course Course"
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _order = "date_start,name"

    name = fields.Char(string='name', required=True,size=64,select=True)
    color = fields.Char(string = 'color', size=10)
    date_start = fields.Date(string = 'start date', default=fields.Date.today)
    date_end = fields.Date(string = 'end date', default=fields.Date.today)
    teacher_id = fields.Many2one('res.users', string='teacher',
        default=lambda self: self.env.user,
        readonly=False)
    student_ids = fields.Many2many('res.partner')
    price = fields.Float('price',digits=(16,2))
    description = fields.Text()
    provider_latitude = fields.Char(string='provider_latitude',size=64)
    provider_longitude = fields.Char(string='provider_longitude',size=64)
    count_students =fields.Integer(string='count_students',compute='_count_students')
    
    @api.one
    @api.depends('student_ids')
    def _count_students(self):
        self.count_students=len(self.student_ids)
