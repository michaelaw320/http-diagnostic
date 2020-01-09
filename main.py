import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import urlopen

IP4_ADDRESS = "http://whatismyip.akamai.com/"
IP6_ADDRESS = "http://ipv6.whatismyip.akamai.com/"


def get_self_inet_addr(url):
    try:
        return urlopen(url).read().decode("utf-8")
    except Exception as e:
        print(f"Exception {e}")
        return "Can't determine ip addr"


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        client_address = self.client_address[0]
        message = {
            "requester-address": client_address,
            "x-forwarded-for": self.headers.get("X-Forwarded-For", None),
            "self-ipv4": get_self_inet_addr(IP4_ADDRESS),
            "self-ipv6": get_self_inet_addr(IP6_ADDRESS),
            "request-headers": self.headers.as_string()
        }
        print(f"Response: {message}")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(message, indent=2).encode("utf-8"))


def main():
    server_address = ('', 80)
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
