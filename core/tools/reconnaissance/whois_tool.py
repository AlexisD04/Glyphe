from os import system
from core.utils import quit, define_cursor_color
from whois import whois

# A refaire avec la sortie brute de whois

def whois_tool():
    system('clear')
    print_whois_logo()

    try:
        domain = input("\n\n Enter a domain name or an IP address (Press ENTER to leave):")
    except KeyboardInterrupt:
        quit()

    if domain == "" : return None
    
    try:
        info = whois(domain)
        print(f"\n === Data WHOIS for {domain} ===")
        print_results(info)

    except Exception as e:
        print(f"\n Error fetching WHOIS information: {e}")

    input("\n Leave?")
    whois_tool()
    return None

def print_whois_logo():
    print(r"                   _______ _________ _______ ")
    print(r"|\     /||\     /|(  ___  )\__   __/(  ____ \ ")
    print(r"| )   ( || )   ( || (   ) |   ) (   | (    \/")
    print(r"| | _ | || (___) || |   | |   | |   | (_____ ")
    print(r"| |( )| ||  ___  || |   | |   | |   (_____  )")
    print(r"| || || || (   ) || |   | |   | |         ) |")
    print(r"| () () || )   ( || (___) |___) (___/\____) |")
    print(r"(_______)|/     \|(_______)\_______/\_______)")
    
    return None

# Affiche au bon format en fonction de si c'est une liste ou un string
def print_data(label,data,jump=False):
    if jump: print()

    if type(data) == list:
        print(f" {label}:")
        for elt in data:
            print(f" | {elt}")
    else:
        print(f" {label}: {data}")

    return None

def print_results(info):
    print_data("Domain name",info.domain_name,True)
    print_data("Registrar",info.registrar)
    print_data("URL registrar",info.registrar_url)

    print_data("Updated date",info.updated_date,True)
    print_data("Creation date",info.creation_date)
    print_data("Expiration date",info.expiration_date)

    print_data("Name servers",info.name_servers,True)

    print_data("Status",info.status,True)

    print_data("Organization",info.org,True)
    print_data("Email",info.emails)
    print_data("Phone",info.phone)
    print_data("Country",info.country)
    print_data("Address",info.address)

    print_data("DNSSE",info.dnssec,True)
    
    return None