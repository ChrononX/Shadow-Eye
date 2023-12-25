import geoip2.database
import ipaddress
import socket
import os
from pyfiglet import Figlet

def print_shadow_eye():
    figlet = Figlet(font='slant')
    print(figlet.renderText('Shadow Eye'))
    print("Made by chrononx")
    print("--------------------")
    print("https://github.com/ChrononX")
    print("https://www.linkedin.com/in/davitmm22/")

def get_ip_info(target, city_reader, country_reader, asn_reader):
    try:
        # Try to interpret the target as an IP address
        ip_obj = ipaddress.ip_address(target)
        ip_address = str(ip_obj)
    except ValueError:
        try:
            # Try to resolve the target as a domain name using local DNS resolver
            ip_address = socket.gethostbyname(target)
        except socket.gaierror:
            return {
                "Target": target,
                "IP Address": "Invalid target",
                "Country": "Unknown",
                "City": "Unknown",
                "Provider": "Unknown",
                "Longitude": "Unknown",
                "Latitude": "Unknown"
            }

    try:
        # Retrieve GeoIP information
        city_response = city_reader.city(ip_address)
        country_response = country_reader.country(ip_address)
        asn_response = asn_reader.asn(ip_address)

        ip_info = {
            "Target": target,
            "IP Address": ip_address,
            "Country": country_response.country.name,
            "City": city_response.city.name,
            "Provider": asn_response.autonomous_system_organization,
            "Longitude": city_response.location.longitude,
            "Latitude": city_response.location.latitude
        }

        return ip_info
    except geoip2.errors.AddressNotFoundError:
        return {
            "Target": target,
            "IP Address": "Information not available",
            "Country": "Unknown",
            "City": "Unknown",
            "Provider": "Unknown",
            "Longitude": "Unknown",
            "Latitude": "Unknown"
        }

def process_log_file(log_file_path, city_reader, country_reader, asn_reader):
    ip_occurrences = {}

    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            target = line.strip()
            ip_info = get_ip_info(target, city_reader, country_reader, asn_reader)
            ip_address = ip_info["IP Address"]

            if ip_address not in ip_occurrences:
                ip_occurrences[ip_address] = 1
                print(f"\nInformation for {ip_info['Target']} ({ip_info['IP Address']}):")
                for key, value in ip_info.items():
                    print(f"{key}: {value}")
            else:
                ip_occurrences[ip_address] += 1

    for ip, count in ip_occurrences.items():
        print(f"\n{ip}: IP Detected {count} times")

def main():
    print_shadow_eye()
    
    script_directory = os.path.dirname(os.path.realpath(__file__))

    asn_database_path = os.path.join(script_directory, 'GeoLite2-ASN_20231222/GeoLite2-ASN.mmdb')
    city_database_path = os.path.join(script_directory, 'GeoLite2-City_20231222/GeoLite2-City.mmdb')
    country_database_path = os.path.join(script_directory, 'GeoLite2-Country_20231222/GeoLite2-Country.mmdb')

    with geoip2.database.Reader(asn_database_path) as asn_reader, \
            geoip2.database.Reader(city_database_path) as city_reader, \
            geoip2.database.Reader(country_database_path) as country_reader:

        while True:
            choice = input("Do you want to enter an IP address/domain or provide a log file path? "
                           "(Type 'ip' or 'log' or 'exit' to quit): ").lower()

            if choice == 'exit':
                break
            elif choice == 'ip':
                target = input("Enter an IP address or domain name: ")
                ip_info = get_ip_info(target, city_reader, country_reader, asn_reader)
                print(f"\nInformation for {ip_info['Target']} ({ip_info['IP Address']}):")
                for key, value in ip_info.items():
                    print(f"{key}: {value}")
            elif choice == 'log':
                log_file_path = input("Enter the path to the log file: ")
                process_log_file(log_file_path, city_reader, country_reader, asn_reader)

if __name__ == "__main__":
    main()
