"""
New Era Consultants — Contact Form API
Vercel Serverless Python Function
"""
from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime


class handler(BaseHTTPRequestHandler):
    """Handles contact form submissions."""

    def do_POST(self):
        """Process contact form data."""
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            data = json.loads(body.decode('utf-8'))

            # Validate required fields
            name = data.get('name', '').strip()
            email = data.get('email', '').strip()
            service = data.get('service', '').strip()
            phone = data.get('phone', '').strip()
            message = data.get('message', '').strip()

            if not name or not email:
                self._send_response(400, {
                    'error': 'Name and email are required.'
                })
                return

            # Basic email validation
            if '@' not in email or '.' not in email:
                self._send_response(400, {
                    'error': 'Please provide a valid email address.'
                })
                return

            # Log the inquiry (in production, you'd save to a database
            # or send via email service like SendGrid, Mailgun, etc.)
            inquiry = {
                'name': name,
                'email': email,
                'phone': phone,
                'service': service,
                'message': message,
                'timestamp': datetime.utcnow().isoformat(),
            }

            print(f"[NEW INQUIRY] {json.dumps(inquiry)}")

            self._send_response(200, {
                'success': True,
                'message': f'Thank you, {name}! We will contact you shortly.'
            })

        except json.JSONDecodeError:
            self._send_response(400, {
                'error': 'Invalid request format.'
            })
        except Exception as e:
            print(f"[ERROR] {str(e)}")
            self._send_response(500, {
                'error': 'Internal server error. Please try again later.'
            })

    def do_OPTIONS(self):
        """Handle CORS preflight requests."""
        self.send_response(200)
        self._set_cors_headers()
        self.end_headers()

    def _send_response(self, status_code, data):
        """Send JSON response with CORS headers."""
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self._set_cors_headers()
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def _set_cors_headers(self):
        """Set CORS headers for cross-origin requests."""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
