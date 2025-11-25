# 🚀 HOW TO RUN PERFECTAI - Step-by-Step Guide

This guide will walk you through running the PerfectAI white-labeling application from start to finish.

---

## ✅ Prerequisites Check

Before running, verify you have:

```bash
# Check if Odoo is installed
which odoo-bin
# OR check if Python is available
python3 --version  # Should be 3.8+

# Check if PostgreSQL is running
sudo systemctl status postgresql
# OR
pg_isready

# Check if you're in the Odoo directory
pwd  # Should show /home/user/Odoo or your Odoo path
```

---

## 🎯 Quick Start (5 Minutes)

### Step 1: Verify Module Installation

```bash
# Navigate to Odoo directory
cd /home/user/Odoo

# Check if module exists
ls -la addons/perfectai_branding/

# You should see:
# - __init__.py
# - __manifest__.py
# - models/
# - views/
# - static/
# - security/
# - README.md, DEPLOYMENT.md, QUICKSTART.md
```

**✅ Module is ready!** The code is already in place and committed to git.

---

### Step 2: Start Odoo (Choose Your Method)

#### Option A: If Odoo is Already Installed as Service

```bash
# Check if Odoo service exists
sudo systemctl status odoo

# If it exists, restart it
sudo systemctl restart odoo

# Check it started successfully
sudo systemctl status odoo

# View logs
sudo tail -f /var/log/odoo/odoo.log
```

#### Option B: If Running Odoo Directly (Development)

```bash
# From the Odoo directory (/home/user/Odoo)
python3 odoo-bin --addons-path=addons --db-filter=^.*$ -d your_database_name

# OR with configuration file
python3 odoo-bin -c /etc/odoo.conf

# You should see output like:
# INFO ? odoo: Odoo version 16.0
# INFO ? odoo.service.server: HTTP service (werkzeug) running on 0.0.0.0:8069
```

#### Option C: If Odoo Isn't Installed Yet

```bash
# Quick Odoo setup (Ubuntu/Debian)
sudo apt update
sudo apt install postgresql python3-pip python3-dev libxml2-dev libxslt1-dev \
    libldap2-dev libsasl2-dev libtiff5-dev libjpeg8-dev libopenjp2-7-dev \
    zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev -y

# Install Python dependencies
pip3 install -r requirements.txt

# Create PostgreSQL user
sudo su - postgres
createuser -s odoo
exit

# Run Odoo
python3 odoo-bin --addons-path=addons -d mydatabase --db-filter=^mydatabase$
```

---

### Step 3: Access Odoo Web Interface

1. **Open your browser** and go to:
   ```
   http://localhost:8069
   ```

2. **First Time Setup:**
   - If you see the database manager:
     - Master Password: `admin` (or set your own)
     - Database Name: `perfectai_demo`
     - Email: `admin@example.com`
     - Password: `admin`
     - Language: English
     - Country: Your country
     - Check "Load demonstration data" (optional)
     - Click **Create Database**

   - Wait 2-5 minutes for database creation

3. **Login:**
   - Email: `admin@example.com` (or what you set)
   - Password: `admin` (or what you set)
   - Click **Log in**

---

### Step 4: Install PerfectAI Module

1. **Enable Developer Mode:**
   - Click your **username** (top right)
   - Go to **Settings**
   - Scroll to bottom
   - Click **Activate the developer mode**

2. **Update Apps List:**
   - Go to **Apps** menu (top)
   - Click **Update Apps List** button
   - Click **Update** in the popup
   - Wait a few seconds

3. **Find PerfectAI:**
   - In Apps menu, search for: `perfectai`
   - You should see: **PerfectAI - Multi-Tenant White-Labeling**

4. **Install:**
   - Click **Install** button
   - Wait 10-30 seconds
   - Module will install automatically

**✅ Success!** You should see a new menu item **PerfectAI** in the top menu bar.

---

## 🎨 Step 5: Configure Your First Branding

### Method A: Quick Setup (2 Minutes)

1. **Go to Company Settings:**
   - Click **Settings** in top menu
   - Scroll to **Companies** section
   - Click **Companies**
   - Click on your company name (e.g., "My Company")

2. **Configure PerfectAI Branding:**
   - Click the **PerfectAI Branding** tab
   - Check ✅ **Enable White-Labeling**
   - Fill in:
     - **Custom App Name**: `MyBusiness ERP`
     - **Custom Tagline**: `Your Business, Simplified`
     - **Primary Brand Color**: `#FF5733` (or click to choose)
     - **Secondary Brand Color**: `#C70039`
     - **Backend Header Color**: `#900C3F`
   - Check ✅ **Hide Odoo Branding in Footer**
   - Click **Save**

3. **See Results:**
   - **Logout** (top right → Log out)
   - You'll see the **login page** with your branding
   - **Login** again
   - Notice the custom app name in browser tab!

### Method B: Advanced Setup (5 Minutes)

1. **Go to PerfectAI Menu:**
   - Click **PerfectAI** in top menu
   - Click **Configuration** → **Tenant Branding**

2. **Create Branding Configuration:**
   - Click **Create** button
   - Fill in:
     - **Name**: `Demo Company Branding`
     - **Company**: Select your company
     - **Application Name**: `Demo Business Suite`

3. **Visual Branding Tab:**
   - **Custom Logo**: Click to upload your logo (PNG/JPG, ~200x60px)
   - **Primary Color**: `#875A7B` (or choose your color)
   - **Secondary Color**: `#8F8F8F`
   - **Accent Color**: `#00A09D`
   - **Header Background Color**: `#875A7B`
   - **Header Text Color**: `#FFFFFF`

4. **Content Tab:**
   - **Welcome Message**: Add custom HTML message for login
   ```html
   <h3>Welcome to Our Platform!</h3>
   <p>The most powerful business management system</p>
   ```
   - **Show Custom Footer**: Check ✅
   - **Footer Text**: Add your footer content

5. **Features Tab:**
   - **Hide Odoo Branding**: Check ✅
   - **Support Email**: `support@yourdomain.com`
   - **Support Phone**: `+1-555-123-4567`

6. **Apply Configuration:**
   - Click **Apply to Company** button (top)
   - You'll see success notification
   - Click **Save**

7. **Test Your Branding:**
   - **Logout**
   - See your custom login page with logo and colors!
   - **Login**
   - Browse around - notice your colors everywhere

---

## 🏢 Step 6: Create a Second Tenant (Multi-Tenant Demo)

### Create New Database for Second Tenant

```bash
# Open a terminal
# Switch to postgres user
sudo su - postgres

# Create new database for tenant
createdb -O odoo tenant2_demo

# Exit postgres user
exit
```

### Initialize Second Tenant

```bash
# Initialize database with PerfectAI module
python3 /home/user/Odoo/odoo-bin -c /etc/odoo.conf \
    -d tenant2_demo \
    --init=base,web,perfectai_branding \
    --stop-after-init

# This will:
# - Create database structure
# - Install base Odoo modules
# - Install PerfectAI module
# - Stop after initialization
```

### Access Second Tenant

1. **Open browser:**
   ```
   http://localhost:8069?db=tenant2_demo
   ```

2. **Login:**
   - Email: `admin` (default for new database)
   - Password: `admin`

3. **Configure Different Branding:**
   - Go to **PerfectAI → Configuration → Tenant Branding**
   - Create new configuration with **different colors**:
     - Primary: `#0066CC` (Blue theme)
     - Secondary: `#004080`
     - App Name: `Tenant 2 Business Suite`
   - Click **Apply to Company**

4. **Compare Tenants:**
   - Tenant 1: `http://localhost:8069?db=perfectai_demo`
   - Tenant 2: `http://localhost:8069?db=tenant2_demo`
   - Each has completely different branding! 🎉

---

## 📊 Step 7: Verify Everything Works

### Checklist

- [ ] Odoo is running (`http://localhost:8069` works)
- [ ] PerfectAI module is installed (visible in Apps)
- [ ] PerfectAI menu appears in top menu bar
- [ ] Company branding settings are accessible
- [ ] Tenant branding configuration works
- [ ] Custom colors are applied
- [ ] Login page shows custom branding
- [ ] "Powered by Odoo" is hidden from footer
- [ ] Browser tab shows custom app name
- [ ] Can create and apply branding configurations

### Test Different Pages

1. **Login Page**: Logout and check branding
2. **Dashboard**: Check header colors
3. **Settings → About**: Verify "Powered by Odoo" is here (for compliance)
4. **Any Portal Page**: Check frontend branding
5. **Forms**: Check button colors match your branding

---

## 🎯 Common Use Cases

### Use Case 1: Single Tenant (Your Own Business)

```bash
# Use the main database
http://localhost:8069

# Configure PerfectAI branding for your company
# Upload your logo, set your colors
# All users see your branding
```

### Use Case 2: Multiple Clients (SaaS Provider)

```bash
# Create database per client
createdb -O odoo client_acme
createdb -O odoo client_biztech
createdb -O odoo client_startup

# Access each client's database
http://localhost:8069?db=client_acme      # Acme Corp branding
http://localhost:8069?db=client_biztech   # BizTech branding
http://localhost:8069?db=client_startup   # Startup branding

# Each client sees only their branding
```

### Use Case 3: Development & Testing

```bash
# Create test database
createdb -O odoo test_branding

# Test different branding configs
# Experiment with colors, logos, text
# Delete and recreate as needed:
dropdb test_branding
createdb -O odoo test_branding
```

---

## 🔧 Troubleshooting

### Issue: "Module not found"

**Solution:**
```bash
# Restart Odoo
sudo systemctl restart odoo
# OR if running directly:
# Ctrl+C to stop, then restart with:
python3 odoo-bin --addons-path=addons -d your_database

# In Odoo UI: Apps → Update Apps List
```

### Issue: "PerfectAI menu not showing"

**Solution:**
1. Hard refresh browser: `Ctrl + Shift + R`
2. Clear browser cache
3. Check module is installed: Apps → search "perfectai" → should show "Installed"
4. Logout and login again

### Issue: "Colors not applying"

**Solution:**
1. Go to Settings → Technical → Assets
2. Find `web.assets_backend` and `web.assets_frontend`
3. Click "Rebuild" on each
4. Hard refresh browser: `Ctrl + Shift + R`

### Issue: "Can't access database"

**Solution:**
```bash
# Check PostgreSQL is running
sudo systemctl status postgresql

# Check database exists
sudo su - postgres
psql -l | grep your_database_name
exit

# Check Odoo is running
sudo systemctl status odoo
# OR
ps aux | grep odoo
```

### Issue: "Permission denied"

**Solution:**
```bash
# Fix file permissions
cd /home/user/Odoo
sudo chown -R $USER:$USER addons/perfectai_branding/
chmod -R 755 addons/perfectai_branding/

# Restart Odoo
sudo systemctl restart odoo
```

---

## 📱 Mobile Access

Access from mobile device on same network:

1. **Find your server IP:**
   ```bash
   hostname -I
   # Example output: 192.168.1.100
   ```

2. **Access from mobile:**
   ```
   http://192.168.1.100:8069
   ```

3. **Mobile browsers supported:**
   - Chrome (Android)
   - Safari (iOS)
   - Firefox (Android/iOS)

---

## 🌐 Production Access (Optional)

### Setup Domain (Basic)

1. **Point domain to server:**
   - In your DNS provider (GoDaddy, Namecheap, etc.)
   - Create A record: `yourdomain.com` → `your_server_ip`

2. **Configure Nginx** (see DEPLOYMENT.md for full guide):
   ```nginx
   server {
       listen 80;
       server_name yourdomain.com;

       location / {
           proxy_pass http://127.0.0.1:8069;
           proxy_set_header Host $host;
       }
   }
   ```

3. **Access:**
   ```
   http://yourdomain.com
   ```

---

## 📈 Next Steps

### Once Everything Works:

1. **Customize Further:**
   - Experiment with different color schemes
   - Upload better logos
   - Add custom CSS (Advanced tab)
   - Add custom login messages

2. **Add More Tenants:**
   - Create more databases
   - Configure unique branding for each
   - Test multi-tenant functionality

3. **Go to Production:**
   - Follow DEPLOYMENT.md guide
   - Setup SSL certificates
   - Configure firewall
   - Setup backups
   - Enable monitoring

4. **Onboard Real Clients:**
   - Create client databases
   - Get client logos and colors
   - Configure branding
   - Provide access credentials

---

## ✅ Success Indicators

You'll know everything is working when:

1. ✅ You can access Odoo at `http://localhost:8069`
2. ✅ PerfectAI module appears in Apps (installed)
3. ✅ PerfectAI menu is visible in top menu
4. ✅ You can create branding configurations
5. ✅ Login page shows your custom logo/colors
6. ✅ Browser tab shows your custom app name
7. ✅ "Powered by Odoo" is hidden from footer
8. ✅ "Powered by Odoo" appears in Settings → About
9. ✅ You can create multiple databases with different branding
10. ✅ All functionality works normally

---

## 🎓 Learning Resources

- **Odoo Documentation**: https://www.odoo.com/documentation/16.0
- **PerfectAI README**: See `addons/perfectai_branding/README.md`
- **Deployment Guide**: See `addons/perfectai_branding/DEPLOYMENT.md`
- **Quick Start**: See `addons/perfectai_branding/QUICKSTART.md`

---

## 🆘 Getting Help

If you're stuck:

1. **Check the logs:**
   ```bash
   # Odoo logs
   sudo tail -f /var/log/odoo/odoo.log

   # Or if running directly, check terminal output
   ```

2. **Check documentation:**
   - README.md for features
   - DEPLOYMENT.md for production setup
   - QUICKSTART.md for quick reference

3. **Common fixes:**
   - Restart Odoo
   - Update Apps List
   - Clear browser cache
   - Check file permissions
   - Verify database exists

---

## 🎉 You're Ready!

**If you can see the PerfectAI menu and configure branding, you're all set!**

The application is:
- ✅ Installed
- ✅ Running
- ✅ Ready to use
- ✅ Ready for multi-tenant deployment

**Start adding your clients and grow your white-label SaaS business!**

---

**Quick Reference:**

```bash
# Start Odoo
sudo systemctl start odoo

# Stop Odoo
sudo systemctl stop odoo

# Restart Odoo
sudo systemctl restart odoo

# View logs
sudo tail -f /var/log/odoo/odoo.log

# Create new tenant database
sudo su - postgres
createdb -O odoo new_tenant_db
exit

# Access Odoo
http://localhost:8069
```

**Need help?** Check the documentation files or open an issue!
