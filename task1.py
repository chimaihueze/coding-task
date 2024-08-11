import re
import logging
from bs4 import BeautifulSoup

# LOGGING SETUP
logging.basicConfig(
    filename='task1.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

try:
    with open('task_1.html') as file:
        html_data = file.read()
        logging.debug('HTML file read successfully.')
except Exception as e:
    logging.error(f'Error reading HTML file: {e}')
    raise


def unique_domain_names(data):
    """
    FUNCTION TO EXTRACT UNIQUE DOMAIN NAMES FROM RAW DATA
    """
    domain_pattern = re.compile(r'https?://(?:www\.)?([^/\s:]+)')

    domain_names = re.findall(domain_pattern, data)

    domains = {domain.strip() for domain in domain_names}

    unique_domains = sorted(domains)

    logging.debug(f"Unique domain names extracted from raw data: {unique_domains}")
    return unique_domains


def unique_domain_names2(html_content):
    """
    FUNCTION TO IDENTIFY DISTINCT DOMAIN NAMES FROM RAW DATA.
    THIS IS AN ALTERNATIVE APPROACH TO ACHIEVING THE SAME RESULT USING BEAUTIFUL SOUP.
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    domain_pattern = re.compile(r'https?://(?:www\.)?([^/\s:]+)')

    text_content = soup.get_text()

    domain_names = re.findall(domain_pattern, text_content)

    domains = {domain.strip() for domain in domain_names}

    unique_domains = sorted(domains)

    logging.debug(f"Unique domain names extracted from HTML content: {unique_domains}")
    return unique_domains


unique_domain_names = unique_domain_names(html_data)
unique_domains_html = unique_domain_names2(html_data)

print(unique_domain_names)
print()
print(unique_domains_html)
