# -*- coding: utf-8 -*-

from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError


class ExampleModule(models.Model):
    _name = "example.module"
    _description = "example module"



    name = fields.Char(string='Name', required=True)
    gender_group = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string="Internal Group",
        required=True)
    is_active = fields.Boolean(string='Active', default=True)
    sign_date = fields.Datetime(string="Sign Date", default=fields.Datetime.now)
    note = fields.Text(string='Description')

