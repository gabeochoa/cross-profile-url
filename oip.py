#!/usr/bin/env python3
import json
import struct
import sys
import webbrowser
import os
import subprocess

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


def main():
    # Read a message from stdin
    data = read_message()

    # Get the URL from the message
    url = data['url']

    # https://chromium.googlesource.com/chromium/src/+/HEAD/docs/user_data_dir.md#Mac-OS-X
    profile = "Default"

    chrome_app = "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"
    cmd = (f"{chrome_app} --profile-directory=\"{profile}\" \"{url}\" ")

    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
        send_message({'success': True, 'cmd': cmd})
        print(f"Success ran command {cmd}")
    except subprocess.CalledProcessError as e:
        error_message = e.output.decode('utf-8')
        send_message({'success': False, 'msg': error_message})
        print(f"Error: {error_message}")

    print(f"Success ran command {cmd}")

if __name__ == '__main__':
    main()
