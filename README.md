# Scraping-SEC-filings
Web-scraped 10-K filings of all public companies on SEC website. 

Python packages used:
- pandas
- BeautifulSoup
- urllib2
- os
# --------- This is an Updated AI Agent ------

  # 📊 SEC 10-K AI Agent for undersatning the 

This AI Agent helps the process of downloading the latest 10-K financial filings and Management Discussion & Analysis (MD&A) reports from the U.S. Securities and Exchange Commission (SEC) website. It's designed to be a valuable tool for investors, analysts, and researchers who need quick and easy access to this information.

## Key Features

* **Batch Downloading:** Downloads the latest 10-K report for multiple companies (up to 40 at a time), saving significant time compared to manual downloads.  You provide a list of company tickers, and the script handles the rest.
* **Automated 10-K Retrieval:**  Specifically targets and retrieves the most recent 10-K filing for each company.
* **MD&A Extraction:**  Extracts the crucial Management Discussion & Analysis (MD&A) section from the 10-K report, allowing for focused analysis of management's perspective on the company's performance.
* **Flexible Output Formats:** Saves the complete 10-K report in both `.txt` (plain text) and `.html` (formatted webpage) formats.  The `.txt` format is ideal for text analysis and NLP tasks, while the `.html` format preserves the document's structure for easy reading.
* **Easy to Use:**  The script is designed to be user-friendly, requiring minimal setup and configuration.  Simply provide a list of company tickers, and the script takes care of the downloading and processing.
* **Efficient and Reliable:**  Leverages robust libraries for web scraping and data processing, ensuring reliable and efficient retrieval of financial data.


---

## **How to Install & Run This Tool**

### **1️⃣ Install Python (if you don’t have it already)**

If Python is not installed, download it here:
🔗 https://www.python.org/downloads/

2️⃣ Clone This Repository
To use this script, you need to download it to your computer.

git clone https://github.com/vishwanathakuthota/scraper-10K-filling-AI-Agent.git
cd sec-10k-downloader

3️⃣ Install Required Python Packages
Before running the script, install the required libraries:

pip install -r requirements.txt

4️⃣ Update the Script with Your Email **(IMPORTANT)**
**SEC requires an email in the request headers.**

Open sec_10_K_AI_Agenet_downloader.py

Find this line:

headers = {
    'User-Agent': 'Company Research Tool (your-email@example.com)',
    'Accept-Encoding': 'gzip, deflate'
}

**Replace your-email@example.com with your own email.**
🚨 If you don’t update this, the SEC may block your requests.

5️⃣ Run the Script
Once everything is set up, run the script:

python sec_10_K_AI_Agenet_downloader.py

📂 Where Do the Files Go?

All downloaded reports are saved in a folder called sec_downloads/

Each company gets its own subfolder
Files are saved in both .txt and .html formats

⚠️ Troubleshooting & FAQs

Why is a company missing?
Some companies may not have filed a recent 10-K report.
Check manually on SEC EDGAR.

What if I get an error?
Make sure Python is installed and you have run pip install -r requirements.txt.
Check your internet connection.

**Ensure you replaced your email in sec_10_K_AI_Agenet_downloader.py.**

**Disclaimer:**
This script is for informational purposes only and does not constitute financial advice.  The accuracy of the downloaded data is not guaranteed, and users should verify the information independently before making any investment decisions.  Use of this script is at your own risk.

## Contributing

Contributions are welcome!  Whether you find a bug, have a suggestion for a new feature, or want to contribute code, there are several ways you can get involved:

**1. Bug Reports:**

* **Check for Existing Issues:** Before submitting a bug report, please check the [Issues](https://github.com/YOUR_USERNAME/YOUR_REPO/issues) page to see if the bug has already been reported.  If it has, you can add your comments or upvotes to the existing issue.
* **Create a New Issue:** If the bug is new, create a new issue on the [Issues](https://github.com/YOUR_USERNAME/YOUR_REPO/issues) page.  Please provide as much detail as possible, including:
    * A clear and descriptive title for the issue.
    * Steps to reproduce the bug.
    * The expected behavior and the actual behavior.
    * Your operating system and Python version.
    * Any relevant error messages or screenshots.

**2. Feature Requests:**

* **Check for Existing Requests:**  Similar to bug reports, check the [Issues](https://github.com/vishwanathakuthota/scraper-10K-filling-AI-Agent) page for existing feature requests.  If there's a similar request, you can add your comments or vote for it.
* **Create a New Request:** If your feature request is new, create a new issue on the [Issues](https://github.com/vishwanathakuthota/scraper-10K-filling-AI-Agent) page.  Describe the feature you'd like to see and explain why it would be beneficial.

**3. Code Contributions:**

* **Fork the Repository:** Fork the repository to your own GitHub account.
* **Create a Branch:** Create a new branch for your changes.  Use a descriptive branch name (e.g., `fix-bug-123`, `add-new-feature`).
* **Make Your Changes:** Make your code changes, ensuring that they follow the project's coding style (if any).  Add unit tests if necessary.
* **Commit Your Changes:** Commit your changes with clear and concise commit messages.
* **Submit a Pull Request:** Create a pull request (PR) from your branch to the main branch of the original repository.  In the PR description, explain the changes you've made and why they are necessary.

**Code Style (Optional):**

*(If you have specific code style guidelines, mention them here. For example:)*

* We follow the PEP 8 style guide for Python code.  You can use tools like `flake8` or `pylint` to check your code.

**Testing (Optional):**

*(If you have a testing framework, mention it here. For example:)*

* Please ensure that your changes pass all existing unit tests.  You can run the tests using `pytest`.

**Guidelines:**

* Be respectful and considerate in your communication.
* Follow the project's code of conduct (if any).

We appreciate your contributions!
