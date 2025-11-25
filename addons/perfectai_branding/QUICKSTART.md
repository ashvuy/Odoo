# PerfectAI White-Labeling - Quick Start Guide

## 🎉 Congratulations!

You now have a complete multi-tenant white-labeling solution for Odoo! Your clients can bring their own logos and branding, and you can host multiple tenants under the **PerfectAI** brand.

---

## 📋 What Was Built

A complete Odoo module (`perfectai_branding`) that includes:

### Core Features
- ✅ **Multi-tenant architecture** - Each client gets their own database with custom branding
- ✅ **Dynamic logo management** - Clients upload their logos
- ✅ **Color customization** - Primary, secondary, and accent colors per tenant
- ✅ **Custom application names** - Each tenant can have "MyCompany ERP" instead of "Odoo"
- ✅ **Login page branding** - Custom welcome messages and styling
- ✅ **Frontend/Portal branding** - Branded portal for customers
- ✅ **Backend branding** - Branded admin interface
- ✅ **License compliance** - "Powered by Odoo" kept in About section (as required by LGPLv3)

### Files Created
```
addons/perfectai_branding/
├── __init__.py
├── __manifest__.py
├── README.md                          # Full documentation
├── DEPLOYMENT.md                      # Production deployment guide
├── QUICKSTART.md                      # This file
├── models/
│   ├── __init__.py
│   ├── res_company.py                 # Extended company model
│   └── perfectai_tenant_branding.py   # Branding configuration model
├── views/
│   ├── res_company_views.xml          # Company branding settings
│   ├── perfectai_branding_views.xml   # Branding management UI
│   └── webclient_templates.xml        # Template overrides
├── static/
│   ├── src/scss/
│   │   ├── perfectai_backend.scss     # Backend styling
│   │   └── perfectai_frontend.scss    # Frontend styling
│   └── description/
│       └── index.html                 # Module description page
└── security/
    └── ir.model.access.csv            # Access rights
```

---

## 🚀 Quick Start (3 Steps)

### Step 1: Install the Module

1. **Update Apps List**
   ```bash
   # In Odoo, go to Apps → Update Apps List
   # Or restart Odoo:
   sudo systemctl restart odoo
   ```

2. **Install PerfectAI Module**
   - Go to **Apps** menu
   - Search for "PerfectAI"
   - Click **Install**

### Step 2: Configure Your First Tenant

#### Option A: Simple Setup (Quick)

1. Go to **Settings → Companies → Companies**
2. Select your company (or create new one)
3. Click the **PerfectAI Branding** tab
4. Check **Enable White-Labeling**
5. Fill in:
   - Custom App Name: `"MyClient ERP"`
   - Custom Tagline: `"Business Made Simple"`
   - Primary Brand Color: `#FF5733` (or any hex color)
   - Check **Hide Odoo Branding in Footer**
6. Click **Save**

#### Option B: Advanced Setup (Recommended)

1. Go to **PerfectAI → Configuration → Tenant Branding**
2. Click **Create**
3. Fill in the form:
   - **Name**: `"Client ABC Branding"`
   - **Company**: Select the tenant company
   - **Visual Branding** tab:
     - Upload custom logo
     - Set primary color: `#875A7B`
     - Set secondary color: `#8F8F8F`
     - Set accent color: `#00A09D`
   - **Content** tab:
     - Add welcome message for login page
     - Add custom footer text
   - **Features** tab:
     - Enable "Hide Odoo Branding"
     - Add support email/phone
4. Click **Apply to Company** button
5. Done! Branding is live.

### Step 3: Test It

1. **Logout** from Odoo
2. **Visit login page**: `http://yourserver:8069?db=your_database`
3. You should see:
   - ✅ Custom logo
   - ✅ Custom colors
   - ✅ Custom app name in browser tab
   - ✅ No "Powered by Odoo" in footer (but it's in About section)

---

## 🏢 Multi-Tenant Setup

### Create Multiple Tenants

For each new client:

#### 1. Create Database
```bash
# SSH into server
sudo su - postgres
createdb -O odoo client1_db
exit
```

#### 2. Initialize Database
```bash
# Initialize with PerfectAI module
python3 /opt/odoo/odoo-bin -c /etc/odoo.conf \
    -d client1_db --init=base,web,perfectai_branding \
    --stop-after-init
```

#### 3. Configure Branding
- Access: `http://yourserver:8069?db=client1_db`
- Login as admin
- Go to **PerfectAI → Configuration → Tenant Branding**
- Create configuration with client's logo and colors
- Click **Apply to Company**

#### 4. Optional: Setup Custom Domain
Edit nginx configuration to route domain to database:

```nginx
map $host $odoo_db {
    client1.yoursaas.com    "client1_db";
    client2.yoursaas.com    "client2_db";
}
```

---

## 📱 Common Use Cases

### Use Case 1: SaaS Provider with Multiple Clients

**Scenario**: You run "BusinessApps.com" and want to offer Odoo to 10 different companies, each with their own branding.

**Solution**:
1. Create 10 databases (business1_db, business2_db, etc.)
2. Configure PerfectAI branding for each
3. Each client accesses: business1.yourdomain.com, business2.yourdomain.com, etc.
4. Each sees their own logo, colors, and app name

### Use Case 2: Implementation Partner

**Scenario**: You implement Odoo for clients but want them to see your branding, not Odoo's.

**Solution**:
1. Install PerfectAI on client's database
2. Set your company logo and colors
3. Set app name to "YourCompany ERP"
4. Hide Odoo branding from footer
5. Client thinks it's your proprietary software!

### Use Case 3: Reseller

**Scenario**: You resell Odoo as "SmartBusiness Suite" under your brand.

**Solution**:
1. Create template with your branding
2. Deploy for each customer with custom tweaks
3. Customer sees "SmartBusiness Suite" everywhere
4. You maintain full control and brand identity

---

## 🎨 Customization Examples

### Example 1: Blue Theme for Tech Company
```python
# In PerfectAI → Tenant Branding
Primary Color: #0066CC
Secondary Color: #004080
Accent Color: #00AAFF
Application Name: "TechCorp Cloud ERP"
Tagline: "Innovation Meets Efficiency"
```

### Example 2: Green Theme for Eco Company
```python
Primary Color: #2ECC40
Secondary Color: #01FF70
Accent Color: #3D9970
Application Name: "EcoSolutions Platform"
Tagline: "Sustainable Business Technology"
```

### Example 3: Corporate Red Theme
```python
Primary Color: #DC143C
Secondary Color: #8B0000
Accent Color: #FF6347
Application Name: "Enterprise Business Suite"
Tagline: "Power Your Business Forward"
```

---

## 🔧 Configuration Reference

### Color Scheme Guidelines

- **Primary Color**: Main brand color (buttons, headers, links)
- **Secondary Color**: Supporting color (borders, accents)
- **Accent Color**: Call-to-action elements (highlights, badges)
- **Header Background**: Navigation bar background
- **Header Text**: Text on navigation bar (usually white)

**Color Format**: Use hex colors like `#RRGGBB`
- Valid: `#875A7B`, `#00A09D`, `#FFF`
- Invalid: `rgb(135,90,123)`, `purple`

### Logo Guidelines

- **Format**: PNG or JPG
- **Recommended size**: 200x60 pixels (width x height)
- **Max file size**: 5MB
- **Background**: Transparent PNG recommended

### Favicon Guidelines

- **Format**: ICO, PNG, or JPG
- **Size**: 16x16 or 32x32 pixels
- **Keep it simple**: Should be recognizable when small

---

## 🛡️ License Compliance

### ✅ What You CAN Do
- Hide "Powered by Odoo" from frontend footer
- Use your own branding everywhere visible to users
- Charge clients for your branded solution
- Build proprietary extensions as separate modules
- Claim it as your product in marketing

### ⚠️ What You MUST Do
- Keep "Powered by Odoo" in About/Settings section
- Provide source code if distributing (LGPLv3 requirement)
- Not claim Odoo core as your original work
- Maintain LGPLv3 license for core modifications

**Where "Powered by Odoo" Appears**:
- ✅ About page (Settings → About): YES (required for compliance)
- ❌ Login page footer: NO (hidden by PerfectAI)
- ❌ Frontend/Portal footer: NO (hidden by PerfectAI)

---

## 📊 Architecture Overview

### Database-per-Tenant Model

```
Your Server
│
├── PostgreSQL
│   ├── client1_db ← Tenant 1
│   │   ├── Logo: Acme Corp
│   │   ├── Colors: Red theme
│   │   └── App Name: "Acme Business Suite"
│   │
│   ├── client2_db ← Tenant 2
│   │   ├── Logo: BizTech
│   │   ├── Colors: Blue theme
│   │   └── App Name: "BizTech ERP"
│   │
│   └── client3_db ← Tenant 3
│       ├── Logo: StartupXYZ
│       ├── Colors: Green theme
│       └── App Name: "StartupXYZ Platform"
│
└── Odoo with PerfectAI
    - Serves all databases
    - Each DB has independent branding
```

### Access Methods

1. **URL Parameter**: `https://yourdomain.com?db=client1_db`
2. **Subdomain Routing**: `https://client1.yourdomain.com` → client1_db
3. **Custom Domain**: `https://clientdomain.com` → client1_db

---

## 🚨 Troubleshooting

### Issue: Module Not Showing Up

**Solution**:
```bash
# Restart Odoo
sudo systemctl restart odoo

# Update apps list in Odoo UI
Apps → Update Apps List
```

### Issue: Branding Not Applying

**Solution**:
1. Clear browser cache (Ctrl+Shift+Delete)
2. Hard refresh (Ctrl+Shift+R)
3. Check if white-labeling is enabled in company settings

### Issue: Colors Not Changing

**Solution**:
1. Verify color format is hex (#RRGGBB)
2. Go to Settings → Technical → Assets
3. Click "Rebuild" on relevant assets

### Issue: Custom Logo Not Showing

**Solution**:
1. Check image format (PNG/JPG)
2. Try smaller file size (< 2MB)
3. Clear browser cache
4. Check if logo was uploaded to correct field

---

## 📚 Next Steps

1. **Read Full Documentation**: Check `README.md` for detailed features
2. **Production Deployment**: See `DEPLOYMENT.md` for production setup
3. **Create Templates**: Build branding templates for quick deployment
4. **Setup Monitoring**: Implement monitoring for production
5. **Backup Strategy**: Set up automated backups for tenant databases

---

## 💼 Business Model Ideas

### Monthly Subscription
- Charge $50-200/month per tenant
- Include hosting, branding, support
- Upsell: custom modules, training, consulting

### Setup Fee + Monthly
- One-time setup: $500-2000
- Monthly hosting: $50-100/month
- Value add: branded implementation

### White-Label Reselling
- Buy Odoo Enterprise licenses
- Add your branding with PerfectAI
- Resell at markup (30-50%)
- Keep customer relationship

---

## 🎓 Support & Resources

### Documentation
- **README.md**: Full feature documentation
- **DEPLOYMENT.md**: Production deployment guide
- **QUICKSTART.md**: This file

### Getting Help
- 📧 Email: support@perfectai.com
- 🐛 Issues: GitHub Issues
- 💬 Community: Odoo Forums

### Learning Resources
- Odoo Documentation: https://www.odoo.com/documentation
- LGPLv3 License: https://www.gnu.org/licenses/lgpl-3.0.html
- Multi-Tenant SaaS: Best practices guides

---

## 🎯 Success Checklist

Before going to production:

- [ ] PerfectAI module installed successfully
- [ ] Created at least one tenant with custom branding
- [ ] Tested login page with custom logo and colors
- [ ] Verified "Powered by Odoo" hidden from footer
- [ ] Confirmed "Powered by Odoo" still in About section
- [ ] Set up SSL certificates (Let's Encrypt)
- [ ] Configured firewall (UFW or similar)
- [ ] Set up automated backups
- [ ] Documented tenant onboarding process
- [ ] Created branding templates for quick deployment
- [ ] Tested with real client logo and colors
- [ ] Performance tested with expected load
- [ ] Monitoring and alerts configured

---

## 🎉 You're Ready!

You now have a production-ready multi-tenant white-labeling solution!

**What You Built**:
- Complete white-label platform under "PerfectAI" brand
- Multi-tenant architecture (database per client)
- Custom branding per client (logos, colors, text)
- LGPLv3 compliant (maintains legal Odoo attribution)
- Production-ready with docs and deployment guide

**Your Competitive Advantage**:
- Offer "your own" ERP platform
- Each client sees their own branding
- Scale to unlimited clients
- Professional, enterprise-grade solution

---

**Questions?**
Check README.md for detailed documentation or reach out for support!

**Made with ❤️ for Your Success**
