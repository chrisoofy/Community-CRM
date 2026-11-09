#!/usr/bin/env python3
"""Local Community-CRM server.

Serves the existing static app and validates contact/household names before the
browser writes those records to its existing localStorage database. This keeps
the existing browser storage model and all unrelated CRM features intact.
"""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
HOST = "127.0.0.1"
PORT = 8765


class CRMHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def _json(self, status, payload):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        if self.path not in ("/api/contact-save", "/api/household-save"):
            self._json(404, {"ok": False, "error": "Unknown save route."})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length <= 0 or length > 1_000_000:
                self._json(400, {"ok": False, "error": "Invalid request size."})
                return
            record = json.loads(self.rfile.read(length).decode("utf-8"))
            if not isinstance(record, dict):
                raise ValueError("A record object is required.")

            if self.path == "/api/contact-save":
                first = str(record.get("firstName", "")).strip()
                last = str(record.get("lastName", "")).strip()
                if not first or not last:
                    self._json(422, {
                        "ok": False,
                        "error": "First and last name are required. Names cannot be blank or spaces only."
                    })
                    return
                record["firstName"] = first
                record["lastName"] = last
            else:
                name = str(record.get("name", "")).strip()
                if not name:
                    self._json(422, {
                        "ok": False,
                        "error": "Household name is required and cannot be blank or spaces only."
                    })
                    return
                record["name"] = name

            self._json(200, {"ok": True, "record": record})
        except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
            self._json(400, {"ok": False, "error": str(exc) or "Invalid JSON request."})


if __name__ == "__main__":
    print(f"Community-CRM server running at http://{HOST}:{PORT}")
    print("Press Ctrl+C to stop.")
    ThreadingHTTPServer((HOST, PORT), CRMHandler).serve_forever()
