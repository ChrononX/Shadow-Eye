**IP Offline Scanner**

The IP Offline Scanner is a Python script designed to provide offline information about given IP addresses using MaxMind's GeoIP2 databases. This program allows users to input an IPv4 address, and it retrieves detailed information such as the country, city, and internet service provider (ISP) associated with that IP address.

**Features:**

Utilizes MaxMind's GeoIP2 databases (GeoLite2-ASN, GeoLite2-City, GeoLite2-Country) for accurate geolocation and ISP data.
Validates user-input IP addresses to ensure proper formatting.
Retrieves information about the country, city, and ISP associated with the provided IP address.
User-friendly interface: Users can interactively input IP addresses and receive detailed information.
Usage:

Run the script and provide the path to the GeoIP2 databases (GeoLite2-ASN, GeoLite2-City, GeoLite2-Country).
Enter an IPv4 address when prompted or type 'exit' to end the program.
Receive detailed information about the provided IP address, including country, city, and ISP.
Prerequisites:

MaxMind GeoIP2 databases (GeoLite2-ASN, GeoLite2-City, GeoLite2-Country) must be available in the specified paths.
Python 3 installed.
Required Python packages installed (listed in the requirements.txt file).
Usage Example:



-> python3 ip_offline_scanner.py
-> Enter an IP address (or 'exit' to quit): 8.8.8.8

This program is useful for scenarios where real-time internet access is limited, and users need offline access to geolocation information for specific IP addresses.

