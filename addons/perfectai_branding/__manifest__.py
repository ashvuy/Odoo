# -*- coding: utf-8 -*-
{
    'name': 'PerfectAI - Multi-Tenant White-Labeling',
    'version': '1.0.0',
    'category': 'Administration',
    'summary': 'Multi-tenant white-labeling solution for PerfectAI ERP',
    'description': """
PerfectAI Multi-Tenant White-Labeling
======================================

This module enables multi-tenant white-labeling capabilities for PerfectAI ERP.

Features:
---------
* Custom branding per company/tenant
* Dynamic logo management
* Customizable color schemes
* White-label login pages
* Tenant-specific styling
* Removes "Powered by Odoo" from frontend (kept only in About section for compliance)

Perfect for:
-----------
* SaaS providers
* Multi-tenant deployments
* Hosting providers
* Resellers

License Compliance:
------------------
This module maintains LGPLv3 compliance by keeping "Powered by Odoo"
attribution in the About/Settings section as required by the license.
    """,
    'author': 'PerfectAI',
    'website': 'https://www.perfectai.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'web',
        'base_setup',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/res_company_views.xml',
        'views/perfectai_branding_views.xml',
        'views/webclient_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'perfectai_branding/static/src/scss/perfectai_backend.scss',
        ],
        'web.assets_frontend': [
            'perfectai_branding/static/src/scss/perfectai_frontend.scss',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
