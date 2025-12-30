import logging
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Tuple

from insinoorilaskin.logger import ROOT_LOGGER_NAME, setup_logging
from insinoorilaskin.config import PACKAGE_NAME

logger = logging.getLogger(ROOT_LOGGER_NAME)


class Handler(BaseHTTPRequestHandler):
    server_version = f"{PACKAGE_NAME}/0.1"

    def _send_plain(self, code: int, body: str = "") -> None:
        payload = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        if payload:
            self.wfile.write(payload)

    def do_GET(self) -> None:
        if self.path in ("/", "/health", "/ping"):
            self._send_plain(200, "OK")
            return
        self._send_plain(404, "Not Found")


def _get_bind_address() -> Tuple[str, int]:
    from insinoorilaskin.config import os as _os

    host = _os.environ.get("insinoorilaskin_HOST", "0.0.0.0")
    port_str = _os.environ.get("insinoorilaskin_PORT", "8080")
    try:
        port = int(port_str)
    except ValueError:
        logger.warning("Invalid port '%s' in env; falling back to 8080", port_str)
        port = 8080
    return host, port


def main() -> None:
    setup_logging()
    host, port = _get_bind_address()
    server = ThreadingHTTPServer((host, port), Handler)
    logger.info("%s server listening on http://%s:%s", PACKAGE_NAME, host, port)
    try:
        server.serve_forever(poll_interval=0.5)
    except KeyboardInterrupt:
        logger.info("Shutdown requested (KeyboardInterrupt), stopping server…")
    finally:
        server.shutdown()
        server.server_close()
        logger.info("Server stopped")

if __name__ == "__main__":
    main()
