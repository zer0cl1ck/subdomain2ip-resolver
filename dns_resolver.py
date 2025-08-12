#!/usr/bin/env python3

import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# Set a global DNS timeout
socket.setdefaulttimeout(3)  # seconds

# Resolve function with timeout protection
def resolve_subdomain(subdomain):
    try:
        ip_address = socket.gethostbyname(subdomain)
        return f"{subdomain}:{ip_address}"
    except Exception:
        return f"{subdomain}:Could not resolve"

def process_subdomains(input_file, output_file):
    # Read input subdomains
    with open(input_file, 'r') as f:
        subdomains = f.read().splitlines()

    results = [None] * len(subdomains)

    with ThreadPoolExecutor(max_workers=50) as executor:
        # Map futures to original index to preserve order
        future_to_index = {
            executor.submit(resolve_subdomain, subdomain): i
            for i, subdomain in enumerate(subdomains)
        }

        with tqdm(total=len(subdomains), desc="Resolving", unit="subdomain") as pbar:
            for future in as_completed(future_to_index):
                index = future_to_index[future]
                try:
                    result = future.result()
                except Exception:
                    result = f"{subdomains[index]}:Error"
                results[index] = result
                pbar.update(1)

    # Write to output file in order
    with open(output_file, 'w') as f:
        f.write('\n'.join(results))

    print(f"\n✅ Done! Results saved to: {output_file}")

if __name__ == "__main__":
    input_file = 'subdomains.txt'
    output_file = 'result.txt'
    process_subdomains(input_file, output_file)
