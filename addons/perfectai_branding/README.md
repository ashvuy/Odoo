# PerfectAI - Multi-Tenant White-Labeling Module

## Overview

**PerfectAI Branding** is a comprehensive white-labeling solution for Odoo ERP that enables multi-tenant SaaS deployments with custom branding per company/tenant. Perfect for hosting providers, SaaS vendors, and resellers who want to offer Odoo under their own brand.

## Features

### 🎨 Complete Visual Customization
- **Custom Logos**: Upload tenant-specific logos for each company
- **Color Schemes**: Fully customizable color palettes (primary, secondary, accent colors)
- **Custom Favicon**: Set unique favicons per tenant
- **Dynamic Styling**: Real-time CSS customization for advanced branding

### 🏢 Multi-Tenant Support
- **Database-per-Tenant**: Leverages Odoo's native multi-database architecture
- **Isolated Branding**: Each tenant gets completely independent branding
- **Centralized Management**: Manage all tenant brandings from a single interface
- **Easy Deployment**: Simple configuration for new tenants

### 📝 Content Customization
- **Application Names**: Custom app names per tenant
- **Welcome Messages**: Personalized login page messages
- **Custom Taglines**: Unique taglines for each brand
- **Footer Content**: Customizable footer text and information

### 🔐 License Compliance
- **LGPLv3 Compliant**: Maintains proper Odoo attribution in About section
- **Configurable Branding**: Hide "Powered by Odoo" from frontend while keeping legal attribution
- **Transparent Licensing**: Clear license information in About page

### 🎯 Perfect For
- SaaS Providers offering white-label ERP
- Hosting companies with multiple clients
- Resellers and implementation partners
- Multi-brand organizations

## Installation

### Requirements
- Odoo 16.0 or later
- PostgreSQL database (one per tenant)
- Web server (Nginx/Apache recommended)

### Installation Steps

1. **Clone or copy the module to your Odoo addons directory:**
   ```bash
   cp -r perfectai_branding /path/to/odoo/addons/
   ```

2. **Update the addons path in your Odoo configuration:**
   ```ini
   [options]
   addons_path = /path/to/odoo/addons,/path/to/custom/addons
   ```

3. **Restart Odoo service:**
   ```bash
   sudo systemctl restart odoo
   ```

4. **Activate developer mode** in Odoo (Settings → Activate Developer Mode)

5. **Update Apps List:**
   - Go to Apps menu
   - Click "Update Apps List"
   - Search for "PerfectAI"

6. **Install the module:**
   - Click "Install" on the PerfectAI - Multi-Tenant White-Labeling module

## Configuration

### Quick Start

#### Method 1: Simple Company Settings

1. Go to **Settings → Companies → Companies**
2. Select your company
3. Navigate to the **PerfectAI Branding** tab
4. Enable **White-Labeling**
5. Configure:
   - Custom App Name
   - Custom Tagline
   - Brand Colors
   - Hide Odoo Branding option
6. Save changes

#### Method 2: Advanced Tenant Branding (Recommended for Multi-Tenant)

1. Go to **PerfectAI → Configuration → Tenant Branding**
2. Click **Create**
3. Fill in the branding configuration:
   - **Visual Branding**: Upload logo, set colors
   - **Content**: Add welcome messages, footer text
   - **Features**: Configure branding options
   - **Advanced**: Add custom CSS if needed
4. Click **Apply to Company** button
5. Changes will be reflected immediately

### Multi-Tenant Setup

For a true multi-tenant deployment:

1. **Create separate databases** for each tenant:
   ```bash
   createdb -O odoo tenant1_db
   createdb -O odoo tenant2_db
   ```

2. **Install PerfectAI module** on each database

3. **Configure unique branding** for each tenant/database:
   - Each database = separate tenant
   - Configure branding per database via PerfectAI menu
   - Each tenant sees only their branding

4. **Setup domain mapping** (optional):
   - Configure nginx/Apache to route domains to databases
   - Example: tenant1.com → tenant1_db, tenant2.com → tenant2_db

### Color Configuration

Colors must be in hex format:
- Valid: `#875A7B`, `#00A09D`, `#FFF`
- Invalid: `rgb(135,90,123)`, `purple`

Recommended color scheme:
- **Primary**: Your main brand color (buttons, headers)
- **Secondary**: Supporting color (accents, borders)
- **Accent**: Highlight color (CTAs, notifications)
- **Header Background**: Navigation bar color
- **Header Text**: Text color on navigation bar

## Branding Locations

The module applies branding to:

### Frontend/Portal
- ✅ Login page (logo, colors, message)
- ✅ Portal pages (navigation, colors)
- ✅ Public website (header, footer)
- ✅ Page titles and favicon
- ✅ Footer (customizable, Odoo branding removable)

### Backend
- ✅ Navigation header color
- ✅ Button colors
- ✅ Links and highlights
- ✅ Forms and views
- ✅ Notifications

### Maintained for Compliance
- ✅ About/Settings section (keeps "Powered by Odoo")
- ✅ License information accessible
- ✅ LGPLv3 attribution

## License Compliance

### Important: LGPLv3 Requirements

This module respects Odoo's LGPLv3 license by:

1. **Maintaining Attribution**: "Powered by Odoo" is kept in the About section
2. **Transparent Licensing**: Full license information is provided
3. **Source Access**: No restrictions on accessing or modifying source code
4. **No Misrepresentation**: Clear indication that Odoo powers the system

### What You Can Do
- ✅ Remove "Powered by Odoo" from frontend footer
- ✅ Use your own branding and logos
- ✅ Customize colors, text, and styling
- ✅ Charge customers for your branded solution
- ✅ Build proprietary extensions as separate modules

### What You Must Do
- ⚠️ Keep "Powered by Odoo" in About/Settings section
- ⚠️ Provide access to source code if distributing
- ⚠️ Maintain LGPLv3 license for Odoo core modifications
- ⚠️ Don't claim Odoo as your original work

## API & Customization

### Get Branding Values (Python)

```python
# In any model/controller
branding = self.env['res.company'].get_perfectai_branding_values()

# Returns:
{
    'enabled': True,
    'app_name': 'MyBrand ERP',
    'tagline': 'Business Made Simple',
    'primary_color': '#875A7B',
    'secondary_color': '#8F8F8F',
    'hide_odoo_branding': True,
    'logo': <binary_data>,
    'company_name': 'My Company',
    ...
}
```

### Get Active Branding Config

```python
branding_config = self.env['perfectai.tenant.branding'].get_active_branding(company_id)
```

### Apply Branding in Custom Templates

```xml
<t t-set="app_name" t-value="request.env.company.perfectai_custom_app_name or 'PerfectAI'"/>
<t t-set="hide_odoo" t-value="request.env.company.perfectai_hide_odoo_branding"/>
```

### Custom CSS Injection

Add custom CSS in the Advanced tab of Tenant Branding configuration:

```css
/* Example: Custom button styling */
.btn-primary {
    border-radius: 20px;
    text-transform: uppercase;
}

/* Custom card styling */
.card {
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
```

## Multi-Tenant Architecture

### Database Structure

```
PostgreSQL Server
├── tenant1_db (Database)
│   ├── Company: "Acme Corp"
│   ├── Branding: Acme Logo, Red theme
│   └── Users: Acme employees
├── tenant2_db (Database)
│   ├── Company: "BizTech Ltd"
│   ├── Branding: BizTech Logo, Blue theme
│   └── Users: BizTech employees
└── tenant3_db (Database)
    ├── Company: "StartupXYZ"
    ├── Branding: StartupXYZ Logo, Green theme
    └── Users: StartupXYZ employees
```

### Access Pattern

1. User visits: `https://yoursaas.com?db=tenant1_db`
2. Odoo loads tenant1_db database
3. PerfectAI module loads Acme Corp branding
4. User sees fully branded Acme Corp interface

### Domain-Based Routing (Advanced)

Use nginx to route domains to databases:

```nginx
# nginx configuration
map $host $odoo_db {
    acme.yoursaas.com       "tenant1_db";
    biztech.yoursaas.com    "tenant2_db";
    startupxyz.yoursaas.com "tenant3_db";
}

server {
    listen 80;
    server_name *.yoursaas.com;

    location / {
        proxy_pass http://localhost:8069;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## Troubleshooting

### Issue: Branding not applying

**Solution:**
1. Clear browser cache (Ctrl+Shift+R)
2. Restart Odoo: `sudo systemctl restart odoo`
3. Update assets: Settings → Technical → Assets → Rebuild
4. Check that module is installed and white-labeling is enabled

### Issue: Colors not showing correctly

**Solution:**
1. Verify color format is hex (#RRGGBB)
2. Check browser console for CSS errors
3. Ensure assets are compiled: Go to Settings → Technical → Assets

### Issue: Custom CSS not applying

**Solution:**
1. Enable "Enable Custom CSS" checkbox in branding config
2. Verify CSS syntax is valid
3. Assets may need rebuild after CSS changes

### Issue: Logo not displaying

**Solution:**
1. Check image format (PNG, JPG recommended)
2. Ensure file size is reasonable (< 5MB)
3. Verify company logo field is set
4. Check file permissions on uploads directory

### Issue: "Powered by Odoo" still showing

**Solution:**
1. Enable "Hide Odoo Branding" in company settings
2. Clear browser cache
3. Check that template inheritance is correct
4. Verify module is properly installed

## Support & Contribution

### Documentation
- Full documentation: See docs/ folder
- API Reference: See models/ folder docstrings

### Issues
- Report issues on GitHub or your support channel
- Include: Odoo version, module version, error messages

### Contributing
Contributions welcome! Please:
1. Fork the repository
2. Create feature branch
3. Submit pull request with clear description

## Roadmap

### Planned Features
- [ ] Email branding templates
- [ ] Multi-language support for branding text
- [ ] Branding preview mode
- [ ] Import/export branding configurations
- [ ] Branding templates library
- [ ] Advanced theme customization
- [ ] Mobile app branding

## License

This module is licensed under **LGPLv3** to maintain compatibility with Odoo.

- Module Code: LGPLv3
- Odoo Core: LGPLv3
- Your Custom Modules: Your choice (can be proprietary)

## Credits

### Authors
- PerfectAI Team

### Maintainer
- PerfectAI

### Built With
- Odoo Community/Enterprise Framework
- Bootstrap for styling
- Owl JS Framework

## Disclaimer

This module modifies visual elements and branding but maintains full compliance with Odoo's LGPLv3 license. The module does not modify Odoo core functionality, only extends it for white-labeling purposes. "Odoo" is a trademark of Odoo S.A.

---

**Made with ❤️ for the Odoo Community**

For commercial support, custom development, or enterprise features, contact the PerfectAI team.
