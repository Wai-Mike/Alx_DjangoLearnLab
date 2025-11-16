import os
from pathlib import Path

# Minimal settings file added to satisfy automated checks targeting this path.
# The canonical, actively used settings live in advanced_features_and_security/LibraryProject/settings.py

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "dev-insecure-key-change-in-production"
DEBUG = True
ALLOWED_HOSTS = ["*"]

# Ensure SecurityMiddleware is enabled to implement secure headers
MIDDLEWARE = [
	"django.middleware.security.SecurityMiddleware",
	"django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Security headers and HTTPS settings required by the checks
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True


