from core.utils import quit, clearConsole
from core.config import SHODAN_API_KEY
import shodan

def shodan_tool():
    choix = 0
    try:
        while(choix != 3):
            clearConsole(False)
            print_shodan_logo()
            print("\n 1. Shodan search")
            print(" 2. Host search")
            print(" 3. Quit")

            try:
                choix = int(input("\n What do you want to do?:"))

                if(choix == 1):
                    shodan_search()

                elif(choix == 2):
                    host_search()

            except:
                clearConsole(False)
                print_shodan_logo()

    except KeyboardInterrupt:
        quit()

    return None

def print_shodan_logo():
    print(r" _______           _______  ______   _______  _       ")
    print(r"(  ____ \|\     /|(  ___  )(  __  \ (  ___  )( (    /|")
    print(r"| (    \/| )   ( || (   ) || (  \  )| (   ) ||  \  ( |")
    print(r"| (_____ | (___) || |   | || |   ) || (___) ||   \ | |")
    print(r"(_____  )|  ___  || |   | || |   | ||  ___  || (\ \) |")
    print(r"      ) || (   ) || |   | || |   ) || (   ) || | \   |")
    print(r"/\____) || )   ( || (___) || (__/  )| )   ( || )  \  |")
    print(r"\_______)|/     \|(_______)(______/ |/     \||/    )_)")

def print_host_results(info):

    print(f"\n IP: {info['ip_str']}")
    print(f" Organization: {info.get('org', 'n/a')}")
    print(f" ISP: {info.get('isp', 'n/a')}")
    print(f" ASN: {info.get('asn', 'n/a')}")
    print(f" OS: {info.get('os', 'n/a')}")
    print(f" Tags: {info.get('tags', [])}")

    print(f"\n Country: {info.get('country_name', 'n/a')} ({info.get('country_code', 'n/a')})")
    print(f" Region code: {info.get('region_code', 'n/a')}")
    print(f" Area code: {info.get('area_code', 'n/a')}")
    print(f" City: {info.get('city', 'n/a')}")
    print(f" Latitude: {info.get('latitude', 'n/a')}")
    print(f" Longitude: {info.get('longitude', 'n/a')}")

    print(f"\n Hostnames: {info.get('hostnames', [])}")
    print(f" Domains: {info.get('domains', [])}")
    print(f" Ports: {info.get('ports', [])}")
    print(f" Last update: {info.get('last_update', 'n/a')}")

    if 'vulns' in info:
        print("\n Vulnerabilities:")
        for vuln in info['vulns']:
            print(f" - {vuln}")

    for service in info.get('data', []):
        print("\n --- Service detected ---")
        print(f" Port: {service.get('port', 'n/a')}")
        print(f" Transport: {service.get('transport', 'n/a')}")
        print(f" Product: {service.get('product', 'n/a')}")
        print(f" Version: {service.get('version', 'n/a')}")
        print(f" CPE: {service.get('cpe', 'n/a')}")
        print(f" Banner:\n{service.get('data', '').strip()}")

    return None


def shodan_search():
    api = shodan.Shodan(SHODAN_API_KEY)

    try:
        print("\n WARNING: This framework considers you are using a free shodan account, it prevents you to see the results.")
        search = input(" Search(Press ENTER to leave):")
        if search == "" : return None

        # A premium shonan account is needed for more information
        results = api.count(search)
        print(f" Results found: {results['total']}")

    except shodan.APIError as e:
        print(f" Error: {e}")

    input("\n Leave?")
    return None

def host_search():
    api = shodan.Shodan(SHODAN_API_KEY)

    try:
        print("\n WARNING: Using a free shodan account can limit the searchable IPs.")
        ip = input(" IP to inspect(Press ENTER to leave):")
        if ip == "" : return None

        info = api.host(ip)
        print(f"\n === Results for {ip} ===")
        print_host_results(info)

    except shodan.APIError as e:
        print(f" Error: {e}")
    
    input("\n Leave?")
    return None