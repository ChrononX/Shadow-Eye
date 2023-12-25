
# Shadow Eye

Shadow Eye is a Python-based offline IP and domain information scanner. It leverages GeoIP databases to provide detailed geographical information about IP addresses and domains.




## Features

- Retrieve IP address information, including country, city, and geographical coordinates (longitude and latitude).
- Identify the autonomous system organization (ISP) associated with an IP address.
- Support for both direct entry of IP addresses/domains and processing log files containing multiple entries.
- Prevents duplication of IP addresses in the output, displaying the count of occurrences in log files.
- Figlet-based ASCII art animation with a small trademark message.


## Installation

git clone https://github.com/ChrononX/Shadow-Eye.git

```Run the program using Python3.
  pip3 install -r requirements.txt
  python3 program.py
```
    
## Requirements

- Python 3.x
- GeoIP2 Python
- pyfiglet


## License

[MIT](https://choosealicense.com/licenses/mit/)

