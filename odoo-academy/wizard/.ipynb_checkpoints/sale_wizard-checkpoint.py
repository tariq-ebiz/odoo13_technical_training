# -*- coding: utf-8 -*-

from odoo import models, fields, api 

class SaleWizard(models.TransientModel):
    _name ='academy.sale.wizard'
    _description = 'Wizard: Quick Sale Orders for Session Students'
    
    def _default_session(self):
        return self.env['academy.session'].browse(self._context.get('active_id'))
    
    session_id = fields.Many2one(comodel_name='academy.session',
                                 string='Session',
                                 required=True,
                                 default=_default_session)
    
    session_student_ids = fields.Many2many(comodel_name='res.partner',
                                           string='Student in Current Session',
                                           related ='session_id.students_ids',
                                           help='These are the students currently in the Session')
    students_ids = fields.Many2many(comodel_name='res.partner',
                                    string='Students for Sales Order')
                                          
    )