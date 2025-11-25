# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import re


class PerfectAITenantBranding(models.Model):
    _name = 'perfectai.tenant.branding'
    _description = 'PerfectAI Tenant Branding Configuration'
    _order = 'company_id, id'

    name = fields.Char(
        string='Configuration Name',
        required=True,
        help='Name for this branding configuration'
    )

    company_id = fields.Many2one(
        'res.company',
        string='Company/Tenant',
        required=True,
        default=lambda self: self.env.company,
        help='Company/Tenant this branding applies to'
    )

    active = fields.Boolean(
        default=True,
        help='Set to false to disable this branding configuration'
    )

    # Visual Branding
    custom_logo = fields.Binary(
        string='Custom Logo',
        help='Upload custom logo for this tenant'
    )

    custom_logo_filename = fields.Char(string='Logo Filename')

    favicon = fields.Binary(
        string='Favicon',
        help='Custom favicon (16x16 or 32x32 pixels recommended)'
    )

    favicon_filename = fields.Char(string='Favicon Filename')

    # Colors
    primary_color = fields.Char(
        string='Primary Color',
        default='#875A7B',
        required=True,
        help='Primary brand color in hex format (#RRGGBB)'
    )

    secondary_color = fields.Char(
        string='Secondary Color',
        default='#8F8F8F',
        required=True,
        help='Secondary brand color in hex format (#RRGGBB)'
    )

    accent_color = fields.Char(
        string='Accent Color',
        default='#00A09D',
        help='Accent color for highlights and CTAs'
    )

    header_background_color = fields.Char(
        string='Header Background',
        default='#875A7B',
        help='Background color for navigation header'
    )

    header_text_color = fields.Char(
        string='Header Text Color',
        default='#FFFFFF',
        help='Text color for navigation header'
    )

    # Text Content
    application_name = fields.Char(
        string='Application Name',
        required=True,
        default='PerfectAI',
        help='Name displayed in browser title and headers'
    )

    welcome_message = fields.Html(
        string='Welcome Message',
        help='Welcome message displayed on login page'
    )

    tagline = fields.Char(
        string='Tagline',
        help='Short tagline for your application'
    )

    footer_text = fields.Html(
        string='Custom Footer Text',
        help='Custom text to display in footer'
    )

    # Features
    hide_odoo_branding = fields.Boolean(
        string='Hide Odoo Branding',
        default=True,
        help='Remove "Powered by Odoo" from footer (kept in About for compliance)'
    )

    show_custom_footer = fields.Boolean(
        string='Show Custom Footer',
        default=True,
        help='Display custom footer text'
    )

    enable_custom_css = fields.Boolean(
        string='Enable Custom CSS',
        default=False,
        help='Apply custom CSS styling'
    )

    custom_css = fields.Text(
        string='Custom CSS',
        help='Add custom CSS rules for advanced styling'
    )

    # Contact Information
    support_email = fields.Char(
        string='Support Email',
        help='Support email displayed to users'
    )

    support_phone = fields.Char(
        string='Support Phone',
        help='Support phone number'
    )

    support_url = fields.Char(
        string='Support URL',
        help='URL to support/help documentation'
    )

    # Computed Fields
    color_preview = fields.Html(
        string='Color Preview',
        compute='_compute_color_preview',
        help='Preview of selected colors'
    )

    @api.depends('primary_color', 'secondary_color', 'accent_color')
    def _compute_color_preview(self):
        """Generate color preview HTML"""
        for record in self:
            preview_html = f'''
                <div style="display: flex; gap: 10px; padding: 10px;">
                    <div style="width: 60px; height: 60px; background-color: {record.primary_color or '#875A7B'}; border: 1px solid #ccc; border-radius: 4px;" title="Primary"></div>
                    <div style="width: 60px; height: 60px; background-color: {record.secondary_color or '#8F8F8F'}; border: 1px solid #ccc; border-radius: 4px;" title="Secondary"></div>
                    <div style="width: 60px; height: 60px; background-color: {record.accent_color or '#00A09D'}; border: 1px solid #ccc; border-radius: 4px;" title="Accent"></div>
                </div>
            '''
            record.color_preview = preview_html

    @api.constrains('primary_color', 'secondary_color', 'accent_color', 'header_background_color', 'header_text_color')
    def _check_color_format(self):
        """Validate hex color format"""
        hex_pattern = re.compile(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')
        for record in self:
            colors = {
                'Primary Color': record.primary_color,
                'Secondary Color': record.secondary_color,
                'Accent Color': record.accent_color,
                'Header Background': record.header_background_color,
                'Header Text Color': record.header_text_color,
            }
            for color_name, color_value in colors.items():
                if color_value and not hex_pattern.match(color_value):
                    raise ValidationError(
                        _('%s must be in hex format (#RRGGBB or #RGB). Example: #875A7B') % color_name
                    )

    @api.model
    def get_active_branding(self, company_id=None):
        """
        Get active branding configuration for a company
        Returns the first active branding config or default values
        """
        if not company_id:
            company_id = self.env.company.id

        branding = self.search([
            ('company_id', '=', company_id),
            ('active', '=', True)
        ], limit=1)

        if branding:
            return {
                'application_name': branding.application_name,
                'primary_color': branding.primary_color,
                'secondary_color': branding.secondary_color,
                'accent_color': branding.accent_color,
                'header_background_color': branding.header_background_color,
                'header_text_color': branding.header_text_color,
                'tagline': branding.tagline,
                'welcome_message': branding.welcome_message,
                'hide_odoo_branding': branding.hide_odoo_branding,
                'support_email': branding.support_email,
                'support_phone': branding.support_phone,
                'support_url': branding.support_url,
                'custom_css': branding.custom_css if branding.enable_custom_css else '',
            }

        # Return defaults
        return {
            'application_name': 'PerfectAI',
            'primary_color': '#875A7B',
            'secondary_color': '#8F8F8F',
            'accent_color': '#00A09D',
            'header_background_color': '#875A7B',
            'header_text_color': '#FFFFFF',
            'tagline': '',
            'welcome_message': '',
            'hide_odoo_branding': True,
            'support_email': '',
            'support_phone': '',
            'support_url': '',
            'custom_css': '',
        }

    def action_apply_branding(self):
        """Apply this branding configuration to the company"""
        self.ensure_one()
        self.company_id.write({
            'perfectai_enable_white_label': True,
            'perfectai_custom_app_name': self.application_name,
            'perfectai_custom_tagline': self.tagline,
            'perfectai_primary_brand_color': self.primary_color,
            'perfectai_secondary_brand_color': self.secondary_color,
            'perfectai_hide_odoo_branding': self.hide_odoo_branding,
            'perfectai_backend_header_color': self.header_background_color,
        })
        if self.custom_logo:
            self.company_id.partner_id.image_1920 = self.custom_logo

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Success'),
                'message': _('Branding configuration applied successfully!'),
                'type': 'success',
                'sticky': False,
            }
        }
