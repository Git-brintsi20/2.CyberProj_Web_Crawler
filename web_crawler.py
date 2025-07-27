import requests
from urllib.parse import urlparse, parse_qs
import pandas as pd
import argparse

def crawl_url(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            parsed_url = urlparse(url)
            params = parse_qs(parsed_url.query)
            return {"url": url, "parameters": params}
        else:
            print(f"Failed to access {url} (Status code: {response.status_code})")
            return None
    except Exception as e:
        print(f"Error accessing {url}: {e}")
        return None

def crawl_multiple_urls(urls, output_file):
    results = []
    for url in urls:
        # Strip whitespace/newlines from URLs read from a file
        url = url.strip()
        if not url:
            continue
        print(f"Crawling URL: {url}")
        result = crawl_url(url)
        if result:
            results.append(result)

    if results:
        all_param_keys = set()
        for result in results:
            all_param_keys.update(result['parameters'].keys())
        
        processed_data = []
        for result in results:
            row = {'URL': result['url']}
            for key in all_param_keys:
                param_value_list = result['parameters'].get(key)
                row[key] = param_value_list[0] if param_value_list else ''
            processed_data.append(row)

        df = pd.DataFrame(processed_data)
        sorted_params = sorted(list(all_param_keys))
        df = df[['URL'] + sorted_params]
        
        df.to_csv(output_file, index=False)
        print(f"\nResults saved to {output_file}")
    else:
        print("No results to save.")

def main():
    parser = argparse.ArgumentParser(description="Web Crawler to extract URL parameters from a list of URLs or a file.")
    # Create a mutually exclusive group: you can use --urls OR --file, but not both.
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-u', '--urls', nargs='+', help='List of URLs to crawl')
    group.add_argument('-f', '--file', help='Path to a file containing URLs, one per line')
    
    parser.add_argument('-o', '--output', default="output.csv", help='Output CSV file name')
    
    args = parser.parse_args()
    
    urls_to_crawl = []
    if args.urls:
        urls_to_crawl = args.urls
    elif args.file:
        try:
            with open(args.file, 'r') as f:
                urls_to_crawl = f.readlines()
        except FileNotFoundError:
            print(f"Error: The file '{args.file}' was not found.")
            return

    crawl_multiple_urls(urls_to_crawl, args.output)

if __name__ == "__main__":
    main()