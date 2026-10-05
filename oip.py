#!/usr/bin/env python3
import json
import struct
import sys
import webbrowser
import os
import subprocess
import re
from urllib.parse import urlparse

def read_message():
    # Read the message length (32-bit integer) from stdin
    length_bytes = sys.stdin.buffer.read(4)
    if len(length_bytes) != 4:
        raise ValueError("Invalid message length")

    # Unpack the message length from bytes to integer
    length = struct.unpack('i', length_bytes)[0]

    # Read the JSON message from stdin
    message_bytes = sys.stdin.buffer.read(length)
    if len(message_bytes) != length:
        raise ValueError("Invalid message length")

    # Decode the JSON message from bytes to string
    message = message_bytes.decode('utf-8')

    # Parse the JSON message
    data = json.loads(message)

    return data

def send_message(data):
    message = json.dumps(data)
    message_bytes = message.encode('utf-8')
    length = len(message_bytes)
    length_bytes = struct.pack('i', length)

    sys.stdout.buffer.write(length_bytes)
    sys.stdout.buffer.write(message_bytes)
    sys.stdout.buffer.flush()


PROFILE = "Default"
CHROME_APP = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
def build_argv(url, profile=PROFILE):
    if not re.fullmatch(r"[A-Za-z0-9 _.-]+", profile): raise ValueError("bad profile")
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https") or not parsed.netloc: raise ValueError("only http(s) URLs")
    return [CHROME_APP, f"--profile-directory={profile}", url]  # argv, never shell: url is data (305f291 quoting bypassable via embedded quote)
def open_url(url):
    subprocess.run(build_argv(url), check=True, capture_output=True, text=True)
def main():
    # stdout IS the native-messaging wire (length-prefixed): never print() there; diagnostics to stderr, always one framed response.
    try:
        data = read_message(); open_url(data["url"])
    except subprocess.CalledProcessError as e:
        print("chrome failed", file=sys.stderr); return send_message({"success": False, "msg": e.stderr or "chrome failed"})
    except Exception as e:
        print(f"bad request: {e}", file=sys.stderr); return send_message({"success": False, "msg": str(e)})
    return send_message({"success": True})

if __name__ == '__main__':
    main()
