Advanced Features and Security
==============================

Overview
--------
This project demonstrates:
- Custom Django user model (`bookshelf.User`) with `date_of_birth` and `profile_photo`
- Custom user manager for user/superuser creation
- Admin integration for the custom user
- Custom permissions on `bookshelf.Book`: `can_view`, `can_create`, `can_edit`, `can_delete`
- Views protected with permission checks
- Secure settings: CSRF, secure cookies, anti-XSS headers, CSP, HTTPS toggles

Custom User Model
-----------------
- Model: `bookshelf.models.User` (extends `AbstractUser`)
- Fields: `date_of_birth`, `profile_photo`
- Manager: `bookshelf.managers.UserManager`
- Settings: `AUTH_USER_MODEL = "bookshelf.User"`
- Admin: `bookshelf.admin.UserAdmin` adds custom fields to forms and lists

Permissions and Groups
----------------------
- `bookshelf.models.Book` defines Meta permissions: `can_view`, `can_create`, `can_edit`, `can_delete`
- Views use `@permission_required("bookshelf.<perm>", raise_exception=True)` to enforce access
- Create groups in admin:
  - Viewers: `can_view`
  - Editors: `can_view`, `can_create`, `can_edit`
  - Admins: all permissions or superuser

Security Best Practices
-----------------------
- CSRF tokens included in all forms (`{% csrf_token %}`)
- Headers: `SECURE_BROWSER_XSS_FILTER`, `SECURE_CONTENT_TYPE_NOSNIFF`, `X_FRAME_OPTIONS = "DENY"`
- Cookies: `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE` set True
- CSP: simple default via `bookshelf.middleware.ContentSecurityPolicyMiddleware`. Adjust CSP_* settings in `settings.py`
- HTTPS:
  - Enable in production: `DEBUG = False`, `SECURE_SSL_REDIRECT = True`, `SECURE_HSTS_SECONDS = 31536000`, `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`, `SECURE_HSTS_PRELOAD = True`

Deployment Notes
----------------
When serving behind HTTPS (e.g., Nginx):
- Obtain certificates (Let's Encrypt)
- Redirect HTTP->HTTPS at the proxy
- Set `SECURE_SSL_REDIRECT = True` and HSTS settings in `settings.py`
- Ensure `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE` remain True

Basic Nginx Snippet (example)
-----------------------------
server {
    listen 80;
    server_name example.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name example.com;
    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
    location / {
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto https;
        proxy_pass http://127.0.0.1:8000;
    }
}


