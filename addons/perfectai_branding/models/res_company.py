# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    # PerfectAI White-Label Settings
    perfectai_enable_white_label = fields.Boolean(
        string='Enable White-Labeling',
        default=False,
        help='Enable tenant-specific white-labeling for this company'
    )

    perfectai_custom_app_name = fields.Char(
        string='Custom App Name',
        default='PerfectAI',
        help='Custom application name displayed to users'
    )

    perfectai_custom_tagline = fields.Char(
        string='Custom Tagline',
        help='Custom tagline for your branded application'
    )

    perfectai_primary_brand_color = fields.Char(
        string='Primary Brand Color',
        default='#875A7B',
        help='Primary color for branding (hex format: #RRGGBB)'
    )

    perfectai_secondary_brand_color = fields.Char(
        string='Secondary Brand Color',
        default='#8F8F8F',
        help='Secondary color for branding (hex format: #RRGGBB)'
    )

    perfectai_login_message = fields.Html(
        string='Custom Login Message',
        help='Custom message displayed on the login page'
    )

    perfectai_hide_odoo_branding = fields.Boolean(
        string='Hide Odoo Branding in Footer',
        default=True,
        help='Remove "Powered by Odoo" from frontend footer (kept in About section for license compliance)'
    )

    perfectai_custom_favicon = fields.Binary(
        string='Custom Favicon',
        help='Custom favicon for browser tabs'
    )

    perfectai_backend_header_color = fields.Char(
        string='Backend Header Color',
        default='#875A7B',
        help='Color for backend navigation header'
    )

    @api.model
    def get_perfectai_branding_values(self):
        """
        Get branding values for the current company/tenant
        Returns a dictionary with all branding settings
        """
        company = self.env.company
        return {
            'enabled': company.perfectai_enable_white_label,
            'app_name': company.perfectai_custom_app_name or 'PerfectAI',
            'tagline': company.perfectai_custom_tagline or '',
            'primary_color': company.perfectai_primary_brand_color or '#875A7B',
            'secondary_color': company.perfectai_secondary_brand_color or '#8F8F8F',
            'login_message': company.perfectai_login_message or '',
            'hide_odoo_branding': company.perfectai_hide_odoo_branding,
            'logo': company.logo_web,
            'company_name': company.name,
            'backend_header_color': company.perfectai_backend_header_color or '#875A7B',
        }
