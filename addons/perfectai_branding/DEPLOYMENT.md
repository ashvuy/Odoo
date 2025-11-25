# PerfectAI Multi-Tenant White-Labeling - Deployment Guide

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Architecture Overview](#architecture-overview)
3. [Installation Steps](#installation-steps)
4. [Multi-Tenant Configuration](#multi-tenant-configuration)
5. [Domain Routing Setup](#domain-routing-setup)
6. [Security Considerations](#security-considerations)
7. [Performance Optimization](#performance-optimization)
8. [Monitoring & Maintenance](#monitoring--maintenance)

---

## Prerequisites

### System Requirements
- **Operating System**: Ubuntu 20.04/22.04 LTS or Debian 11 (recommended)
- **RAM**: Minimum 4GB (8GB+ recommended for production)
- **Storage**: SSD recommended, 50GB+ for multi-tenant setup
- **CPU**: 2+ cores recommended

### Software Requirements
- **Odoo**: Version 16.0 or later
- **PostgreSQL**: Version 12 or later
- **Python**: 3.8 or later
- **Web Server**: Nginx or Apache
- **SSL Certificate**: Let's Encrypt or commercial SSL

### Network Requirements
- Open ports: 80 (HTTP), 443 (HTTPS), 8069 (Odoo)
- Domain names for each tenant (optional but recommended)
- DNS configured to point to your server

---

## Architecture Overview

### Single Server Multi-Tenant Architecture

```
┌─────────────────────────────────────────────┐
│           Nginx Reverse Proxy                │
│  (Domain Routing & SSL Termination)         │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│            Odoo Application                  │
│         (Port 8069, Longpolling 8072)       │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│          PostgreSQL Database                 │
│  ├── tenant1_db (Client 1)                  │
│  ├── tenant2_db (Client 2)                  │
│  ├── tenant3_db (Client 3)                  │
│  └── ...                                     │
└─────────────────────────────────────────────┘
```

### Benefits
- **Isolation**: Each tenant has separate database
- **Security**: Data completely isolated per tenant
- **Scalability**: Easy to add new tenants
- **Customization**: Per-tenant branding and configuration
- **Backup**: Individual database backups per tenant

---

## Installation Steps

### Step 1: Install Odoo

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install PostgreSQL
sudo apt install postgresql -y

# Install Python dependencies
sudo apt install python3-pip python3-dev libxml2-dev libxslt1-dev \
    libldap2-dev libsasl2-dev libtiff5-dev libjpeg8-dev libopenjp2-7-dev \
    zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev libharfbuzz-dev \
    libfribidi-dev libxcb1-dev -y

# Install wkhtmltopdf (for PDF reports)
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.jammy_amd64.deb
sudo dpkg -i wkhtmltox_0.12.6.1-2.jammy_amd64.deb
sudo apt-get install -f

# Install Node.js (for SCSS compilation)
curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt-get install -y nodejs

# Create Odoo user
sudo useradd -m -d /opt/odoo -U -r -s /bin/bash odoo

# Clone Odoo (or use package installation)
sudo su - odoo
git clone https://github.com/odoo/odoo.git --depth 1 --branch 16.0 /opt/odoo/odoo16

# Install Python requirements
pip3 install -r /opt/odoo/odoo16/requirements.txt
```

### Step 2: Install PerfectAI Module

```bash
# Switch to odoo user
sudo su - odoo

# Create custom addons directory
mkdir -p /opt/odoo/custom-addons

# Copy PerfectAI module
cp -r /path/to/perfectai_branding /opt/odoo/custom-addons/

# Set permissions
chmod -R 755 /opt/odoo/custom-addons/perfectai_branding
```

### Step 3: Configure Odoo

Create `/etc/odoo.conf`:

```ini
[options]
# Admin credentials
admin_passwd = CHANGE_THIS_STRONG_PASSWORD
db_host = localhost
db_port = 5432
db_user = odoo
db_password = odoo_db_password

# Paths
addons_path = /opt/odoo/odoo16/addons,/opt/odoo/custom-addons
data_dir = /opt/odoo/.local/share/Odoo

# Performance
workers = 4
max_cron_threads = 2
limit_memory_hard = 2684354560
limit_memory_soft = 2147483648
limit_request = 8192
limit_time_cpu = 600
limit_time_real = 1200

# Database filtering (for multi-tenancy)
dbfilter = ^%h$

# Logging
logfile = /var/log/odoo/odoo.log
log_level = info

# Server
http_port = 8069
longpolling_port = 8072
proxy_mode = True

# Security
list_db = False
```

**Important Settings Explained:**
- `dbfilter = ^%h$`: Automatically selects database based on hostname
- `list_db = False`: Hides database selector for security
- `proxy_mode = True`: Required when behind Nginx/Apache
- `workers = 4`: Adjust based on CPU cores (2 × cores + 1)

### Step 4: Create Systemd Service

Create `/etc/systemd/system/odoo.service`:

```ini
[Unit]
Description=Odoo Open Source ERP and CRM
After=network.target postgresql.service

[Service]
Type=simple
User=odoo
Group=odoo
ExecStart=/usr/bin/python3 /opt/odoo/odoo16/odoo-bin -c /etc/odoo.conf
StandardOutput=journal+console

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl daemon-reload
sudo systemctl enable odoo
sudo systemctl start odoo
sudo systemctl status odoo
```

---

## Multi-Tenant Configuration

### Step 1: Create Databases for Each Tenant

```bash
# Switch to postgres user
sudo su - postgres

# Create database for tenant 1
createdb -O odoo tenant1_db

# Create database for tenant 2
createdb -O odoo tenant2_db

# Create database for tenant 3
createdb -O odoo tenant3_db

# Exit postgres user
exit
```

### Step 2: Initialize Databases

For each database, initialize Odoo:

```bash
# Initialize tenant1_db
python3 /opt/odoo/odoo16/odoo-bin -c /etc/odoo.conf -d tenant1_db \
    --init=base,web,perfectai_branding --stop-after-init

# Initialize tenant2_db
python3 /opt/odoo/odoo16/odoo-bin -c /etc/odoo.conf -d tenant2_db \
    --init=base,web,perfectai_branding --stop-after-init

# Repeat for other tenants...
```

### Step 3: Configure Branding for Each Tenant

1. Access tenant database: `http://yourserver:8069?db=tenant1_db`
2. Login with admin credentials
3. Go to **Settings → Companies → Companies**
4. Configure PerfectAI branding settings
5. Or use **PerfectAI → Configuration → Tenant Branding** for advanced setup

### Step 4: Create Admin Users for Each Tenant

```python
# Python script to create admin for tenant
# Run: python3 create_tenant_admin.py

import xmlrpc.client

# Configuration
url = 'http://localhost:8069'
db = 'tenant1_db'
username = 'admin'
password = 'admin'  # Change after creation

# Connect
common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})

# Create new admin user for tenant
models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
user_id = models.execute_kw(db, uid, password, 'res.users', 'create', [{
    'name': 'Tenant Admin',
    'login': 'admin@tenant1.com',
    'email': 'admin@tenant1.com',
    'groups_id': [(6, 0, [1])],  # Admin group
}])

print(f"Created user ID: {user_id}")
```

---

## Domain Routing Setup

### Option 1: Nginx Configuration (Recommended)

Create `/etc/nginx/sites-available/odoo`:

```nginx
# Upstream Odoo
upstream odoo {
    server 127.0.0.1:8069;
}

upstream odoo_longpolling {
    server 127.0.0.1:8072;
}

# Map hostnames to databases
map $host $odoo_db {
    default                     "";
    tenant1.perfectai.com       "tenant1_db";
    tenant2.perfectai.com       "tenant2_db";
    tenant3.perfectai.com       "tenant3_db";
}

# HTTP Redirect to HTTPS
server {
    listen 80;
    server_name *.perfectai.com;
    return 301 https://$host$request_uri;
}

# HTTPS Server Configuration
server {
    listen 443 ssl http2;
    server_name *.perfectai.com;

    # SSL Configuration (Let's Encrypt)
    ssl_certificate /etc/letsencrypt/live/perfectai.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/perfectai.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;

    # Security Headers
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-XSS-Protection "1; mode=block" always;

    # Logging
    access_log /var/log/nginx/odoo_access.log;
    error_log /var/log/nginx/odoo_error.log;

    # Proxy Settings
    proxy_read_timeout 720s;
    proxy_connect_timeout 720s;
    proxy_send_timeout 720s;
    proxy_set_header X-Forwarded-Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Real-IP $remote_addr;

    # Increase buffer size
    proxy_buffers 16 64k;
    proxy_buffer_size 128k;

    # Force timeouts if the backend dies
    proxy_next_upstream error timeout invalid_header http_500 http_502 http_503;

    # Odoo log files
    location /web/database {
        proxy_pass http://odoo;
        return 403;  # Disable database manager
    }

    # Longpolling
    location /longpolling {
        proxy_pass http://odoo_longpolling;
    }

    # Main Location
    location / {
        proxy_pass http://odoo;
        proxy_redirect off;
    }

    # Cache static files
    location ~* /web/static/ {
        proxy_cache_valid 200 90m;
        proxy_buffering on;
        expires 864000;
        proxy_pass http://odoo;
    }

    # Gzip compression
    gzip on;
    gzip_types text/css text/scss text/plain text/xml application/xml application/json application/javascript;
}
```

Enable and restart Nginx:

```bash
sudo ln -s /etc/nginx/sites-available/odoo /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### Option 2: Apache Configuration

Create `/etc/apache2/sites-available/odoo.conf`:

```apache
<VirtualHost *:80>
    ServerName tenant1.perfectai.com
    Redirect permanent / https://tenant1.perfectai.com/
</VirtualHost>

<VirtualHost *:443>
    ServerName tenant1.perfectai.com

    SSLEngine on
    SSLCertificateFile /etc/letsencrypt/live/perfectai.com/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/perfectai.com/privkey.pem

    ProxyRequests Off
    ProxyPreserveHost On

    <Proxy *>
        Order deny,allow
        Allow from all
    </Proxy>

    ProxyPass / http://localhost:8069/
    ProxyPassReverse / http://localhost:8069/

    RequestHeader set X-Forwarded-Proto "https"
    RequestHeader set X-Forwarded-For %{REMOTE_ADDR}s
</VirtualHost>

# Repeat for other tenants...
```

### SSL Certificate Setup (Let's Encrypt)

```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx -y

# Get wildcard certificate
sudo certbot certonly --manual --preferred-challenges=dns \
    -d *.perfectai.com -d perfectai.com

# Add DNS TXT record as instructed, then press Enter

# Auto-renewal (already set up by certbot)
sudo systemctl status certbot.timer
```

---

## Security Considerations

### 1. Database Access Control

```bash
# PostgreSQL: Restrict connections
sudo nano /etc/postgresql/14/main/pg_hba.conf

# Add:
local   all             odoo                                    md5
host    all             odoo            127.0.0.1/32            md5
```

### 2. Firewall Configuration

```bash
# UFW Firewall
sudo ufw allow 22/tcp   # SSH
sudo ufw allow 80/tcp   # HTTP
sudo ufw allow 443/tcp  # HTTPS
sudo ufw deny 8069/tcp  # Block direct Odoo access
sudo ufw enable
```

### 3. Fail2Ban for Brute Force Protection

```bash
# Install Fail2Ban
sudo apt install fail2ban -y

# Create Odoo jail
sudo nano /etc/fail2ban/jail.d/odoo.conf

[odoo]
enabled = true
port = http,https
logpath = /var/log/odoo/odoo.log
maxretry = 5
findtime = 600
bantime = 3600
```

### 4. Regular Security Updates

```bash
# Auto-updates
sudo apt install unattended-upgrades -y
sudo dpkg-reconfigure -plow unattended-upgrades
```

---

## Performance Optimization

### 1. PostgreSQL Tuning

Edit `/etc/postgresql/14/main/postgresql.conf`:

```ini
# Memory Settings (adjust for your RAM)
shared_buffers = 2GB
effective_cache_size = 6GB
maintenance_work_mem = 512MB
work_mem = 10MB

# Checkpoint Settings
checkpoint_completion_target = 0.9
wal_buffers = 16MB

# Query Planning
random_page_cost = 1.1
effective_io_concurrency = 200

# Parallel Query
max_parallel_workers_per_gather = 2
max_parallel_workers = 4
```

Restart PostgreSQL:

```bash
sudo systemctl restart postgresql
```

### 2. Odoo Workers Configuration

For a 4-core server with 8GB RAM:

```ini
[options]
workers = 9  # (4 cores × 2) + 1
max_cron_threads = 2
limit_memory_hard = 2684354560  # 2.5GB
limit_memory_soft = 2147483648  # 2GB
```

### 3. Asset Compilation

```bash
# Precompile assets for all databases
for db in tenant1_db tenant2_db tenant3_db; do
    python3 /opt/odoo/odoo16/odoo-bin -c /etc/odoo.conf -d $db \
        --stop-after-init --no-http
done
```

---

## Monitoring & Maintenance

### 1. Monitoring with Prometheus + Grafana

```bash
# Install Prometheus
sudo apt install prometheus -y

# Install Grafana
sudo apt-get install -y software-properties-common
sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
sudo apt update
sudo apt install grafana -y

# Start services
sudo systemctl start prometheus grafana-server
sudo systemctl enable prometheus grafana-server
```

### 2. Database Backups

Create `/opt/odoo/backup.sh`:

```bash
#!/bin/bash

BACKUP_DIR="/opt/odoo/backups"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Create backup directory
mkdir -p $BACKUP_DIR

# Backup each tenant database
for DB in tenant1_db tenant2_db tenant3_db; do
    echo "Backing up $DB..."
    pg_dump -U odoo -F c $DB > $BACKUP_DIR/${DB}_${TIMESTAMP}.dump

    # Compress
    gzip $BACKUP_DIR/${DB}_${TIMESTAMP}.dump

    # Delete backups older than 30 days
    find $BACKUP_DIR -name "${DB}_*.dump.gz" -mtime +30 -delete
done

echo "Backup completed: $(date)"
```

Schedule with cron:

```bash
sudo crontab -e

# Add: Daily backup at 2 AM
0 2 * * * /opt/odoo/backup.sh >> /var/log/odoo/backup.log 2>&1
```

### 3. Log Rotation

Create `/etc/logrotate.d/odoo`:

```
/var/log/odoo/*.log {
    daily
    rotate 30
    compress
    delaycompress
    missingok
    notifempty
    create 0640 odoo odoo
}
```

### 4. Health Check Script

```bash
#!/bin/bash

# Check Odoo service
if systemctl is-active --quiet odoo; then
    echo "Odoo: OK"
else
    echo "Odoo: FAIL - Restarting..."
    systemctl restart odoo
fi

# Check PostgreSQL
if systemctl is-active --quiet postgresql; then
    echo "PostgreSQL: OK"
else
    echo "PostgreSQL: FAIL"
fi

# Check Nginx
if systemctl is-active --quiet nginx; then
    echo "Nginx: OK"
else
    echo "Nginx: FAIL"
fi

# Check disk space
DISK_USAGE=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')
if [ $DISK_USAGE -gt 80 ]; then
    echo "WARNING: Disk usage at ${DISK_USAGE}%"
fi
```

---

## Tenant Onboarding Checklist

### New Tenant Setup

- [ ] Create PostgreSQL database
- [ ] Initialize Odoo with base modules
- [ ] Install PerfectAI branding module
- [ ] Configure company settings (name, address, etc.)
- [ ] Upload tenant logo
- [ ] Configure color scheme
- [ ] Set custom app name and tagline
- [ ] Create admin user for tenant
- [ ] Configure domain/subdomain (if applicable)
- [ ] SSL certificate for domain
- [ ] Test login and branding
- [ ] Configure email server (optional)
- [ ] Import initial data (if any)
- [ ] Train tenant admin
- [ ] Backup database

---

## Troubleshooting

### Common Issues

**Issue: Database connection errors**
```bash
# Check PostgreSQL is running
sudo systemctl status postgresql

# Check Odoo can connect
sudo -u odoo psql -l
```

**Issue: Odoo won't start**
```bash
# Check logs
sudo tail -f /var/log/odoo/odoo.log

# Check systemd service
sudo journalctl -u odoo -n 50
```

**Issue: Nginx 502 Bad Gateway**
```bash
# Check Odoo is running
sudo systemctl status odoo

# Check Nginx error log
sudo tail -f /var/log/nginx/error.log
```

---

## Support

For deployment assistance or issues:
- Email: support@perfectai.com
- Documentation: https://docs.perfectai.com
- GitHub Issues: https://github.com/perfectai/odoo-branding/issues

---

**Deployment Guide Version 1.0**
*Last Updated: November 2025*
