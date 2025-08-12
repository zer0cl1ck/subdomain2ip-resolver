# subdomain2ip-resolver
dns_resolver is a multithreaded Python tool that takes a list of subdomains from a file, resolves them to their IP addresses, and saves the results in order to an output file. It uses a configurable DNS timeout and processes subdomains in parallel for faster results.

Steps to Set Up & Run the Script

# 1. Install Python
Ensure Python 3 is installed:
python3 --version

# 2. Create a Working Directory
mkdir dns_resolver && cd dns_resolver

# 3. Save the Script
Save the code as dns_resolver.py
nano dns_resolver.py

# 4. Install Dependencies
pip install tqdm

# 5. Prepare Input File
Create subdomains.txt with one subdomain per line:
Example:
www.example.com
mail.example.com
api.example.com

# 6. Run the Script
python3 dns_resolver.py

# Note: "The script by default reads from subdomains.txt and writes to result.txt in the same directory"
