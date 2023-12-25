import geoip2.database
import ipaddress
import os

def get_ip_info(ip_address, city_reader, country_reader, asn_reader):
    try:
        # Validate IP address
        ip_obj = ipaddress.IPv4Address(ip_address)
    except ipaddress.AddressValueError:
        return "Invalid IP Address", "Unknown", "Unknown", "Unknown"

    try:
        # Retrieve GeoIP information
        city_response = city_reader.city(ip_address)
        country_response = country_reader.country(ip_address)
        asn_response = asn_reader.asn(ip_address)

        ip_info = {
            "IP Address": ip_address,
            "Country": country_response.country.name,
            "City": city_response.city.name,
            "Provider": asn_response.autonomous_system_organization
        }

        return ip_info
    except geoip2.errors.AddressNotFoundError:
        return "Information not available", "Unknown", "Unknown", "Unknown"

def main():
    script_directory = os.path.dirname(os.path.realpath(__file__))

    asn_database_path = os.path.join(script_directory, 'GeoLite2-ASN_20231222/GeoLite2-ASN.mmdb')
    city_database_path = os.path.join(script_directory, 'GeoLite2-City_20231222/GeoLite2-City.mmdb')
    country_database_path = os.path.join(script_directory, 'GeoLite2-Country_20231222/GeoLite2-Country.mmdb')

    with geoip2.database.Reader(asn_database_path) as asn_reader, \
            geoip2.database.Reader(city_database_path) as city_reader, \
            geoip2.database.Reader(country_database_path) as country_reader:

        while True:
            ip_address = input("Enter an IP address (or 'exit' to quit): ")
            if ip_address.lower() == 'exit':
                break

            ip_info = get_ip_info(ip_address, city_reader, country_reader, asn_reader)

            print(f"\nInformation for IP Address {ip_address}:")
            for key, value in ip_info.items():
                print(f"{key}: {value}")

if __name__ == "__main__":
    main()
