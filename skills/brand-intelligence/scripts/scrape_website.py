#!/usr/bin/env python3
"""
Website scraper for company research

Fetches homepage, about, services pages and extracts clean text content.
Uses web_fetch tool (must be called by Claude, not directly).

Usage:
    This script is imported by Claude and called with:
    scrape_result = scrape_website(company_url)
"""

import re
from typing import Dict, List, Optional
from urllib.parse import urljoin, urlparse


def extract_text_from_html(html: str) -> str:
    """
    Extract clean text from HTML, removing scripts, styles, and excessive whitespace.
    
    Args:
        html: Raw HTML string
        
    Returns:
        Cleaned text content
    """
    # Remove script and style tags
    html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', html)
    
    # Decode HTML entities
    text = text.replace('&nbsp;', ' ')
    text = text.replace('&amp;', '&')
    text = text.replace('&lt;', '<')
    text = text.replace('&gt;', '>')
    text = text.replace('&quot;', '"')
    text = text.replace('&#39;', "'")
    
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    
    return text


def extract_common_paths(base_url: str) -> List[str]:
    """
    Generate common page paths to scrape.
    
    Args:
        base_url: Base URL of the website
        
    Returns:
        List of URLs to attempt scraping
    """
    parsed = urlparse(base_url)
    base = f"{parsed.scheme}://{parsed.netloc}"
    
    # Common paths to check
    paths = [
        "",  # Homepage
        "/about",
        "/about-us",
        "/services",
        "/solutions",
        "/products",
        "/how-it-works",
        "/pricing",
    ]
    
    return [urljoin(base, path) if path else base for path in paths]


def validate_url(url: str) -> bool:
    """
    Validate URL format.
    
    Args:
        url: URL to validate
        
    Returns:
        True if valid HTTP/HTTPS URL
    """
    parsed = urlparse(url)
    return parsed.scheme in ('http', 'https') and bool(parsed.netloc)


def scrape_website(company_url: str, fetched_pages: Dict[str, str]) -> Dict:
    """
    Process fetched website content and extract relevant information.
    
    NOTE: This function expects fetched_pages to be provided by Claude
    after calling web_fetch on the URLs from extract_common_paths().
    
    Args:
        company_url: Base URL of the company website
        fetched_pages: Dict mapping URLs to their HTML content
        
    Returns:
        Dict containing:
            - success: bool
            - pages: Dict[str, str] mapping page type to extracted text
            - word_count: int
            - error: Optional[str]
    """
    if not validate_url(company_url):
        return {
            "success": False,
            "pages": {},
            "word_count": 0,
            "error": "Invalid URL format. Must be HTTP or HTTPS."
        }
    
    if not fetched_pages:
        return {
            "success": False,
            "pages": {},
            "word_count": 0,
            "error": "No pages were successfully fetched."
        }
    
    # Process fetched pages
    processed_pages = {}
    total_words = 0
    
    for url, html in fetched_pages.items():
        if not html:
            continue
            
        # Extract clean text
        text = extract_text_from_html(html)
        
        if len(text) < 100:  # Skip pages with minimal content
            continue
        
        # Determine page type from URL
        url_lower = url.lower()
        if '/about' in url_lower:
            page_type = 'about'
        elif '/service' in url_lower or '/solution' in url_lower:
            page_type = 'services'
        elif '/product' in url_lower:
            page_type = 'products'
        elif '/how-it-works' in url_lower or '/how' in url_lower:
            page_type = 'how_it_works'
        elif '/pricing' in url_lower:
            page_type = 'pricing'
        elif url == company_url or url.rstrip('/') == company_url.rstrip('/'):
            page_type = 'homepage'
        else:
            page_type = 'other'
        
        processed_pages[page_type] = text
        total_words += len(text.split())
    
    if total_words < 500:
        return {
            "success": False,
            "pages": processed_pages,
            "word_count": total_words,
            "error": f"Insufficient content. Only {total_words} words found (minimum 500 required)."
        }
    
    return {
        "success": True,
        "pages": processed_pages,
        "word_count": total_words,
        "error": None
    }


def get_urls_to_fetch(company_url: str) -> List[str]:
    """
    Get list of URLs that Claude should fetch using web_fetch.
    
    Args:
        company_url: Base URL of the company website
        
    Returns:
        List of URLs to fetch
    """
    return extract_common_paths(company_url)
