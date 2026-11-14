"""Serve the extracted pilot on loopback until its terminal is closed."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import webbrowser

folder = Path(__file__).resolve().parent
handler = partial(SimpleHTTPRequestHandler, directory=str(folder))
with ThreadingHTTPServer(("127.0.0.1", 0), handler) as server:
    url = f"http://127.0.0.1:{server.server_port}/index.html"
    print(f"Open {url}\nKeep this window open while comparing. Press Ctrl+C to stop.", flush=True)
    webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
