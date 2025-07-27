import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import pandas as pd
import argparse

def crawl_url(url):
    try:
        
        response = requests.get(url)
        if response.status_code == 200:
            parsed_url = urlparse(url)
            params = parse_qs(parsed_url.query)
            return {
                "url": url,
                "parameters": params
            }
        else:
            print(f"Failed to access {url}")
            return None
    except Exception as e:
        print(f"Error accessing {url}: {e}")
        return None


def crawl_multiple_urls(urls, output_file):
    results = []
    
    for url in urls:
        print(f"Crawling URL: {url}")
        result = crawl_url(url)
        if result:
            results.append(result)
    
    if results:
       
        df = pd.DataFrame(results)
        
       
        df.to_csv(output_file, index=False)
        print(f"Results saved to {output_file}")
    else:
        print("No results to save.")


def main():
    parser = argparse.ArgumentParser(description="Web Crawler to extract URL parameters")
  
  
    parser.add_argument('-u', '--urls', nargs='+', required=True, help='List of URLs to crawl')
    parser.add_argument('-o', '--output', default="results.csv", help='Output CSV file')
    
    args = parser.parse_args()
    
   
    crawl_multiple_urls(args.urls, args.output)

if __name__ == "__main__":
    main()
