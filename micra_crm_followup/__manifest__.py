# -*- coding: utf-8 -*-
{
    'name': "CRM Followup",

    'summary': "Followup scheduled activities in CRM",

    'description': """
        CRM Followup Module to manage scheduled activities for CRM Leads and Opportunities.
        Adds a Followup menu in between Sales and Reporting in CRM to display scheduled,
        today's, and overdue activities assigned to users.
    """,

    'author': "Micra Digital",
    'website': "https://www.micra.digital/",
    'images': ['static/description/banner.png'],
    'category': 'CRM',
    'version': '19.0.1.0.0',
    'support': 'hello@micra.digital',
    'depends': ['base', 'crm', 'mail'],
    'license': 'OPL-1',

    'data': [
        'views/views.xml',
    ],
    'installable': True,
    'application': False,
}

