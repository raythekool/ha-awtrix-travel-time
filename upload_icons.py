#!/usr/bin/env python3
"""Download the travel-time icon from LaMetric and upload it to AWTRIX."""

import argparse
import ipaddress
import mimetypes
import re
import sys
import urllib.error
import urllib.request
import uuid

ICON_NAME = "travel-time"
ICON_ID = 42529
TIMEOUT_SECONDS = 10


def valid_address(value: str) -> str:
    try:
        ipaddress.ip_address(value)
    except ValueError:
        if not value or any(character.isspace() for character in value):
            raise argparse.ArgumentTypeError("Inserire un indirizzo IP o hostname valido.")
    return value


def valid_icon_name(value: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9_-]+", value):
        raise argparse.ArgumentTypeError(
            "Il nome icona puo contenere solo lettere, numeri, trattini e underscore."
        )
    return value


def download_icon() -> tuple[bytes, str]:
    for extension in ("gif", "png"):
        url = f"https://developer.lametric.com/content/apps/icon_thumbs/{ICON_ID}.{extension}"
        try:
            with urllib.request.urlopen(url, timeout=TIMEOUT_SECONDS) as response:
                return response.read(), extension
        except urllib.error.HTTPError:
            continue
    raise RuntimeError(f"Impossibile scaricare l'icona LaMetric {ICON_ID}.")


def upload_icon(address: str, icon_name: str, icon: bytes, extension: str) -> None:
    boundary = f"----AWTRIXUpload{uuid.uuid4().hex}"
    filename = f"/ICONS/{icon_name}.{extension}"
    content_type = mimetypes.types_map.get(f".{extension}", "application/octet-stream")
    body = b"\r\n".join(
        (
            f"--{boundary}".encode(),
            f'Content-Disposition: form-data; name="data"; filename="{filename}"'.encode(),
            f"Content-Type: {content_type}".encode(),
            b"",
            icon,
            f"--{boundary}--".encode(),
            b"",
        )
    )
    request = urllib.request.Request(
        f"http://{address}/edit",
        data=body,
        headers={
            "Content-Type": f"multipart/form-data; boundary={boundary}",
            "Content-Length": str(len(body)),
        },
    )
    with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
        if response.status not in (200, 201):
            raise RuntimeError(f"Upload non riuscito: HTTP {response.status}.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("address", nargs="?", type=valid_address, help="IP o hostname AWTRIX")
    parser.add_argument(
        "--name",
        default=ICON_NAME,
        type=valid_icon_name,
        help=f"Nome file dell'icona in /ICONS (predefinito: {ICON_NAME})",
    )
    args = parser.parse_args()
    address = args.address or input("IP o hostname AWTRIX: ").strip()
    try:
        address = valid_address(address)
        icon, extension = download_icon()
        upload_icon(address, args.name, icon, extension)
    except (RuntimeError, urllib.error.URLError, OSError) as error:
        print(f"Errore: {error}", file=sys.stderr)
        return 1
    print(f"Icona {args.name}.{extension} caricata su {address}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())