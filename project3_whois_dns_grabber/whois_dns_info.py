# whois_dns_info.py

import whois
import dns.resolver

def get_whois(domain):
    print("\n[+] Getting WHOIS Info...")
    try:
        info = whois.whois(domain)
        print("Domain Name:", info.domain_name)
        print("Registrar:", info.registrar)
        print("Creation Date:", info.creation_date)
        print("Expiration Date:", info.expiration_date)
        print("Name Servers:", info.name_servers)
        print("Emails:", info.emails)
    except Exception as e:
        print("WHOIS Error:", e)

def get_dns_records(domain):
    print("\n[+] Getting DNS Records...")
    try:
        print("A Records:", [r.address for r in dns.resolver.resolve(domain, 'A')])
        print("MX Records:", [r.exchange.to_text() for r in dns.resolver.resolve(domain, 'MX')])
        print("NS Records:", [r.to_text() for r in dns.resolver.resolve(domain, 'NS')])
    except Exception as e:
        print("DNS Error:", e)

def main():
    domain = input("Enter domain: ")
    get_whois(domain)
    get_dns_records(domain)

if __name__ == "__main__":
    main()
