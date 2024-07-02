"""
This script allows you to screenshot a given URL. It requires the installation
of chromium and chromium-driver and was written for docker python:3.9-bookworm
"""
import argparse
import sys
from datetime import datetime
from urllib.parse import urlparse
import socket
import ipaddress

try:
    from selenium import webdriver
except ImportError:
    print("Unable to import selenium.")

def get_ipaddress(domain:str, port: int) -> bool:
    """
    Determine if the domain is resolvable
    """
    try:
        if port:
            data = socket.getaddrinfo(domain, port= port)
        else:
            data = socket.getaddrinfo(domain, port= 80)
            
        if len(data):
            return True
        else:
            return False
    except Exception:
        return False

def main():
    """
    Main method, it makes the screenshot for the given url and outputs it.
    The name of the file is the ISO-timestamp followed by the domain, this
    allows for multiple screenshots of the same website.
    """
    url_parse_result = urlparse(args.url)
    host_ipaddress = get_ipaddress(url_parse_result.netloc, url_parse_result.port)
    if all([url_parse_result.scheme, url_parse_result.netloc, host_ipaddress]):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--incognito")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--test-type")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--start-maximized")
        options.add_argument("--window-size=1920,1080")
        options.binary_location = "/usr/bin/chromium"
        driver = webdriver.Chrome(options=options)
        driver.get(args.url)
        isotime = datetime.utcnow().isoformat()
        filename = f"{isotime}_{url_parse_result.netloc}.png"
        driver.save_screenshot(f"/output/{filename}")
        driver.close()
    else:
        sys.exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="The url to screenshot")
    args = parser.parse_args()
    main()
