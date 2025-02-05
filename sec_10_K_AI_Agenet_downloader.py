import requests
import time
import os
import re
from bs4 import BeautifulSoup

# List of companies to process
companies = [
    "PSO", "COUR", "CHGG", "TWOU", "STRA", "LRN", "ATGE", "LOPE", "PRDO",
    "MSFT", "GOOGL", "AMZN", "ADBE", "CRM", "ORCL", "IBM", "WDAY", "NOW",
    "TYL", "HPQ", "DELL", "VMW", "ADSK", "SPGI", "RHI", "VRSK", "MCO",
    "IQV", "PAYX", "AAPL", "META", "CSCO", "NVDA", "INTC", "ACN", "AVGO",
    "TXN", "MA", "V", "PYPL", "INTU", "AKAM", "FTNT", "PANW", "SPLK",
    "BLKB", "PWSC", "INST"
]

def extract_correct_10k(raw_text):
    """Finds the MAIN 10-K section and excludes exhibits and attachments."""
    documents = raw_text.split('<DOCUMENT>')

    ten_k_content = None
    mda_content = None

    print("🔍 Checking document types in SEC filing...")

    for doc in documents:
        doc_type_match = re.search(r'<TYPE>(.*?)\n', doc, re.IGNORECASE)
        doc_type = doc_type_match.group(1).strip() if doc_type_match else "UNKNOWN"
        print(f"🔹 Found document type: {doc_type}")

        # Ensure it's the main 10-K document, not an exhibit
        if doc_type == "10-K":
            print("✅ Identified the correct 10-K document!")
            ten_k_content = doc

            # Extract MD&A (Item 7)
            mda_match = re.search(r'(ITEM\s*7\.\s*MANAGEMENT\S*DISCUSSION\S*ANALYSIS.*?)ITEM\s*8', doc, re.DOTALL | re.IGNORECASE)
            if mda_match:
                mda_content = mda_match.group(1)

            break  # Stop once we find the correct 10-K document

    if not mda_content:
        mda_content = ten_k_content

    return ten_k_content, mda_content

def save_as_html(content, filename):
    """Converts extracted 10-K content to HTML and saves it."""
    soup = BeautifulSoup(content, "html.parser")

    # If the document is plain text, wrap it in <pre> tags
    if not soup.find():
        content = f"<html><body><pre>{content}</pre></body></html>"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

def download_10k(ticker):
    """Download the complete 10-K filing for a given ticker"""
    
    # Create downloads directory
    os.makedirs('sec_downloads', exist_ok=True)
    
    headers = {
        'User-Agent': 'Company Research Tool (your-email@example.com)',
        'Accept-Encoding': 'gzip, deflate'
    }

    try:
        print(f"\nProcessing {ticker}...")
        print("1. Getting company information...")
        
        # Step 1: Get the CIK number
        response = requests.get(
            'https://www.sec.gov/files/company_tickers.json',
            headers=headers
        )
        
        companies_data = response.json()
        cik = None
        
        for entry in companies_data.values():
            if entry['ticker'].upper() == ticker.upper():
                cik = str(entry['cik_str']).zfill(10)
                break
        
        if not cik:
            print(f"❌ Could not find CIK for {ticker}")
            return False
            
        print(f"✅ Found CIK: {cik}")
        time.sleep(1.5)  # SEC rate limit

        # Step 2: Get company's submissions
        company_url = f"https://data.sec.gov/submissions/CIK{cik}.json"
        headers['Host'] = 'data.sec.gov'
        response = requests.get(company_url, headers=headers)
        time.sleep(1.5)  # SEC rate limit
        
        if response.status_code != 200:
            print(f"❌ Error accessing SEC data: {response.status_code}")
            return False
            
        filings = response.json()
        print("2. Looking for most recent 10-K...")
        
        recent_filings = filings['filings']['recent']
        found = False
        
        for i, form in enumerate(recent_filings['form']):
            if form == '10-K':
                found = True
                filing_date = recent_filings['filingDate'][i]
                accession_number = recent_filings['accessionNumber'][i]
                
                print(f"✅ Found 10-K filed on {filing_date}")

                acc_no_stripped = accession_number.replace('-', '')
                url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc_no_stripped}/{accession_number}.txt"
                
                print(f"3. Downloading complete submission file...")
                response = requests.get(url, headers=headers)
                time.sleep(1.5)  # SEC rate limit
                
                if response.status_code == 200:
                    company_dir = f'sec_downloads/{ticker}'
                    os.makedirs(company_dir, exist_ok=True)

                    raw_filename = f'{company_dir}/10K_{filing_date}_full.txt'
                    html_filename = f'{company_dir}/10K_{filing_date}.html'

                    ten_k_content, _ = extract_correct_10k(response.text)

                    if ten_k_content:
                        with open(raw_filename, 'w', encoding='utf-8') as f:
                            f.write(ten_k_content)
                        save_as_html(ten_k_content, html_filename)
                        print(f"✅ Saved: {raw_filename} & {html_filename}")
                    else:
                        print("❌ No valid 10-K found!")

                    return True
                else:
                    print(f"❌ Failed to download document: {response.status_code}")
                    return False

        if not found:
            print("❌ No 10-K filings found")
            return False
            
    except Exception as e:
        print(f"❌ Error processing {ticker}: {str(e)}")
        return False

# Process all companies
for company in companies:
    download_10k(company)
    time.sleep(2)  # Respect SEC rate limits
