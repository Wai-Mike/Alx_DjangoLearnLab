from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class ContentSecurityPolicyMiddleware(MiddlewareMixin):
	def process_response(self, request, response):
		directives = {
			"default-src": getattr(settings, "CSP_DEFAULT_SRC", "'self'"),
			"script-src": getattr(settings, "CSP_SCRIPT_SRC", "'self'"),
			"style-src": getattr(settings, "CSP_STYLE_SRC", "'self'"),
			"img-src": getattr(settings, "CSP_IMG_SRC", "'self'"),
			"font-src": getattr(settings, "CSP_FONT_SRC", "'self'"),
			"connect-src": getattr(settings, "CSP_CONNECT_SRC", "'self'"),
		}
		header_value = "; ".join(f"{k} {v}" for k, v in directives.items() if v)
		response["Content-Security-Policy"] = header_value
		return response


