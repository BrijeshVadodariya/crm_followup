# -*- coding: utf-8 -*-
from odoo import models, fields, api


class MailActivity(models.Model):
    _inherit = 'mail.activity'

    lead_id = fields.Many2one(
        'crm.lead', string='Lead / Opportunity',
        compute='_compute_lead_id',
        store=True, readonly=True
    )
    partner_id = fields.Many2one(
        'res.partner', string='Customer',
        related='lead_id.partner_id', store=True, readonly=True
    )
    email_from = fields.Char(
        string='Email',
        related='lead_id.email_from', store=True, readonly=True
    )
    phone = fields.Char(
        string='Phone',
        related='lead_id.phone', store=True, readonly=True
    )
    stage_id = fields.Many2one(
        'crm.stage', string='Stage',
        related='lead_id.stage_id', store=True, readonly=True
    )
    expected_revenue = fields.Monetary(
        string='Expected Revenue',
        related='lead_id.expected_revenue', currency_field='company_currency', store=True, readonly=True
    )
    company_currency = fields.Many2one(
        'res.currency', string='Currency',
        related='lead_id.company_currency', store=True, readonly=True
    )
    lead_user_id = fields.Many2one(
        'res.users', string='Salesperson',
        related='lead_id.user_id', store=True, readonly=True
    )
    tag_ids = fields.Many2many(
        'crm.tag', string='Tags',
        related='lead_id.tag_ids', readonly=True
    )

    @api.depends('res_model', 'res_id')
    def _compute_lead_id(self):
        for activity in self:
            if activity.res_model == 'crm.lead' and activity.res_id:
                activity.lead_id = activity.res_id
            else:
                activity.lead_id = False
