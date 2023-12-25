import geoip2.database
import ipaddress
import socket
import os

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
            return f"Invalid target: {target}", "Unknown", "Unknown", "Unknown"

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
            "Provider": asn_response.autonomous_system_organization
        }

        return ip_info
    except geoip2.errors.AddressNotFoundError:
        return "Information not available", "Unknown", "Unknown", "Unknown"

def process_log_file(log_file_path, city_reader, country_reader, asn_reader):
    try:
        with open(log_file_path, 'r') as log_file:
            for line in log_file:
                # Split each line into words and check for IP addresses or domains
                words = line.split()
                for word in words:
                    ip_info = get_ip_info(word, city_reader, country_reader, asn_reader)
                    print(f"\nInformation for {ip_info['Target']} ({ip_info['IP Address']}):")
                    for key, value in ip_info.items():
                        print(f"{key}: {value}")
    except FileNotFoundError:
        print(f"Error: Log file not found at {log_file_path}")

def main():
    script_directory = os.path.dirname(os.path.realpath(__file__))

    asn_database_path = os.path.join(script_directory, 'GeoLite2-ASN_20231222/GeoLite2-ASN.mmdb')
    city_database_path = os.path.join(script_directory, 'GeoLite2-City_20231222/GeoLite2-City.mmdb')
    country_database_path = os.path.join(script_directory, 'GeoLite2-Country_20231222/GeoLite2-Country.mmdb')

    with geoip2.database.Reader(asn_database_path) as asn_reader, \
            geoip2.database.Reader(city_database_path) as city_reader, \
            geoip2.database.Reader(country_database_path) as country_reader:

        while True:
            option = input("Enter '1' to enter IP address or domain directly, '2' to process a logfile, or 'exit' to quit: ")
            
            if option.lower() == 'exit':
                break

            if option == '1':
                target = input("Enter an IP address or domain name: ")
                ip_info = get_ip_info(target, city_reader, country_reader, asn_reader)
                print(f"\nInformation for {ip_info['Target']} ({ip_info['IP Address']}):")
                for key, value in ip_info.items():
                    print(f"{key}: {value}")

            elif option == '2':
                log_file_path = input("Enter the path to the logfile: ")
                process_log_file(log_file_path, city_reader, country_reader, asn_reader)

if __name__ == "__main__":
    main()
