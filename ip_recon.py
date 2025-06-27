# ip_recon.py

import requests
import socket
import dns.resolver

def get_ip_info(ip):
    print("\n[+] Getting IP info...")
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        for key in ['query', 'isp', 'org', 'city', 'regionName', 'country', 'timezone']:
            print(f"{key.capitalize()}: {data.get(key)}")
    except Exception as e:
        print("Error:", e)

def dns_lookup(domain):
    print("\n[+] Performing DNS Lookup...")
    try:
        print("A Records:", [r.address for r in dns.resolver.resolve(domain, 'A')])
        print("MX Records:", [r.exchange.to_text() for r in dns.resolver.resolve(domain, 'MX')])
        print("NS Records:", [r.to_text() for r in dns.resolver.resolve(domain, 'NS')])
    except Exception as e:
        print("DNS Lookup Error:", e)

def main():
    target = input("Enter domain or IP: ")
    try:
        ip = socket.gethostbyname(target)
    except:
        ip = target
    get_ip_info(ip)
    dns_lookup(target)

if __name__ == "__main__":
    main()
