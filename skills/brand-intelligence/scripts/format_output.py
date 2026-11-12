#!/usr/bin/env python3
"""
Output formatter for company research

Structures all extracted data into CompanyData JSON format with validation.

Usage:
    company_data = format_output(company_name, company_url, positioning, voice, content, quality_flag)
"""

import json
import re
from typing import Dict, List, Optional


def extract_company_name(pages: Dict[str, str], url: str) -> str:
    """
    Extract company name from website content or URL.
    
    Args:
        pages: Dict mapping page types to text content
        url: Company URL
        
    Returns:
        Company name (best guess)
    """
    # Try to find company name in homepage title/heading patterns
    homepage = pages.get('homepage', '')
    
    # Look for common patterns
    patterns = [
        r'^([A-Z][a-zA-Z0-9]+)\s*[–\-|]',  # "CompanyName - Tagline"
        r'(?:Welcome to|About)\s+([A-Z][a-zA-Z0-9]+)',  # "Welcome to CompanyName"
    ]
    
    for pattern in patterns:
        match = re.search(pattern, homepage)
        if match:
            return match.group(1)
    
    # Fallback: extract from URL
    from urllib.parse import urlparse
    parsed = urlparse(url)
    domain_parts = parsed.netloc.split('.')
    # Get the main domain (skip 'www' if present)
    name_part = domain_parts[-2] if domain_parts[0] == 'www' else domain_parts[0]
    return name_part.capitalize()


def extract_offer(pages: Dict[str, str]) -> str:
    """
    Extract primary offer description (1-2 sentences).
    
    Args:
        pages: Dict mapping page types to text content
        
    Returns:
        Offer description
    """
    # Prioritize homepage and about page
    text = pages.get('homepage', '') + ' ' + pages.get('about', '')
    
    # Split into sentences
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # Look for sentences that describe what they do (verb indicators)
    offer_sentences = []
    for sent in sentences[:20]:  # Check first 20 sentences
        sent_lower = sent.lower()
        if any(verb in sent_lower for verb in ['we help', 'we provide', 'we offer', 'we build', 'we create', 'we deliver', 'we enable', 'we power']):
            if 10 < len(sent.split()) < 40:
                offer_sentences.append(sent)
    
    if offer_sentences:
        return offer_sentences[0]
    
    # Fallback: return first substantial sentence
    for sent in sentences[:10]:
        if 10 < len(sent.split()) < 40:
            return sent
    
    return "Unable to determine primary offer"


def infer_industry(pages: Dict[str, str]) -> str:
    """
    Infer industry from website content.
    
    Args:
        pages: Dict mapping page types to text content
        
    Returns:
        Industry classification
    """
    combined_text = ' '.join(pages.values()).lower()
    
    # Industry keywords mapping
    industries = {
        "B2B SaaS": ['saas', 'software', 'platform', 'api', 'automation', 'integration'],
        "Marketing/Sales": ['marketing', 'sales', 'crm', 'lead generation', 'outreach', 'email marketing'],
        "E-commerce": ['ecommerce', 'e-commerce', 'online store', 'shopify', 'retail', 'products'],
        "Healthcare": ['health', 'medical', 'patient', 'clinic', 'therapy', 'wellness', 'healthcare'],
        "Fintech": ['fintech', 'financial', 'payments', 'banking', 'crypto', 'blockchain'],
        "Education": ['education', 'learning', 'training', 'course', 'student', 'school'],
        "Agency/Services": ['agency', 'consulting', 'services', 'strategy', 'design', 'creative'],
        "Beauty/Wellness": ['beauty', 'spa', 'salon', 'esthetician', 'medspa', 'skin care'],
    }
    
    scores = {}
    for industry, keywords in industries.items():
        score = sum(combined_text.count(keyword) for keyword in keywords)
        scores[industry] = score
    
    # Return industry with highest score
    if scores:
        best_match = max(scores.items(), key=lambda x: x[1])
        if best_match[1] > 0:
            return best_match[0]
    
    return "General Business"


def extract_messaging_themes(pages: Dict[str, str]) -> List[str]:
    """
    Extract 3-5 key messaging themes.
    
    Args:
        pages: Dict mapping page types to text content
        
    Returns:
        List of messaging themes
    """
    combined_text = ' '.join(pages.values()).lower()
    themes = []
    
    # Common messaging theme patterns
    theme_patterns = {
        "Speed/velocity": r'\b(?:fast|quick|rapid|instant|immediate|speed|velocity)\b',
        "Simplicity": r'\b(?:simple|easy|straightforward|intuitive|effortless)\b',
        "Automation": r'\b(?:automat[e|ion]|streamline|optimize|efficient)\b',
        "Quality/premium": r'\b(?:quality|premium|professional|expert|excellence)\b',
        "Results-driven": r'\b(?:result|outcome|roi|growth|increase|revenue)\b',
        "Customer-focused": r'\b(?:customer|client|personalized|custom|tailored)\b',
        "Innovation": r'\b(?:innovate|cutting-edge|advanced|modern|future)\b',
        "Trust/reliability": r'\b(?:trust|reliable|secure|proven|established)\b',
        "Transparency": r'\b(?:transparent|clear|honest|straightforward)\b',
        "Scalability": r'\b(?:scale|grow|expand|flexible|adaptable)\b',
    }
    
    theme_scores = {}
    for theme, pattern in theme_patterns.items():
        count = len(re.findall(pattern, combined_text))
        if count > 0:
            theme_scores[theme] = count
    
    # Return top 5 themes
    sorted_themes = sorted(theme_scores.items(), key=lambda x: x[1], reverse=True)
    return [theme for theme, _ in sorted_themes[:5]]


def extract_positioning_data(pages: Dict[str, str]) -> Dict:
    """
    Extract positioning, differentiators, and authority signals.
    
    Args:
        pages: Dict mapping page types to text content
        
    Returns:
        Dict with differentiators and authority_signals
    """
    combined_text = ' '.join(pages.values()).lower()
    
    # Extract differentiators (what makes them unique)
    differentiators = []
    diff_patterns = [
        r'(?:only|first|leading|#1)\s+([a-z\s]+(?:platform|solution|provider|service))',
        r'(?:unique|exclusive|proprietary)\s+([a-z\s]+)',
        r'(?:unlike|different from)\s+[a-z\s]+,\s+we\s+([a-z\s]+)',
    ]
    
    for pattern in diff_patterns:
        matches = re.findall(pattern, combined_text)
        for match in matches:
            cleaned = match.strip().title()
            if 5 < len(cleaned) < 50 and cleaned not in differentiators:
                differentiators.append(cleaned)
    
    # Extract authority signals
    authority_signals = []
    
    if re.search(r'\b(?:case\s+stud|success\s+stor)\b', combined_text):
        authority_signals.append("Case studies")
    
    if re.search(r'\btestimonia', combined_text):
        authority_signals.append("Customer testimonials")
    
    if re.search(r'\b(?:award|recognized|certified)\b', combined_text):
        authority_signals.append("Awards/certifications")
    
    if re.search(r'\b\d+[+]?\s+(?:years?|customers?|clients?|users?)\b', combined_text):
        authority_signals.append("Quantified results")
    
    if re.search(r'\b(?:featured|mentioned)\s+(?:in|on)\b', combined_text):
        authority_signals.append("Media mentions")
    
    return {
        "differentiators": differentiators[:3] if differentiators else ["Not clearly differentiated"],
        "authority_signals": authority_signals if authority_signals else ["None identified"]
    }


def determine_quality_flag(pages: Dict[str, str], voice_samples: List[str], offer: str) -> str:
    """
    Determine quality flag for the data.
    
    Args:
        pages: Dict mapping page types to text content
        voice_samples: List of voice samples extracted
        offer: Extracted offer description
        
    Returns:
        "PASS", "GENERIC_VOICE", or "INSUFFICIENT_DATA"
    """
    # Check for insufficient data
    if not pages:
        return "INSUFFICIENT_DATA"
    
    total_words = sum(len(text.split()) for text in pages.values())
    if total_words < 500:
        return "INSUFFICIENT_DATA"
    
    if offer == "Unable to determine primary offer":
        return "INSUFFICIENT_DATA"
    
    # Check for generic voice
    if len(voice_samples) < 2:
        return "GENERIC_VOICE"
    
    combined_samples = ' '.join(voice_samples).lower()
    generic_phrases = [
        'we provide solutions',
        'industry-leading',
        'best-in-class',
        'world-class',
        'cutting-edge solutions',
        'leverage our expertise'
    ]
    
    generic_count = sum(1 for phrase in generic_phrases if phrase in combined_samples)
    if generic_count >= 2:
        return "GENERIC_VOICE"
    
    return "PASS"


def format_output(
    company_name: str,
    company_url: str,
    scraped_pages: Dict[str, str],
    voice_analysis: Dict,
    content_audit: Dict
) -> str:
    """
    Format all extracted data into CompanyData JSON.
    
    Args:
        company_name: Name of the company (or empty to extract)
        company_url: Company website URL
        scraped_pages: Dict mapping page types to text content
        voice_analysis: Voice analysis results
        content_audit: Content audit results
        
    Returns:
        JSON string matching CompanyData contract
    """
    # Extract or use provided company name
    if not company_name:
        company_name = extract_company_name(scraped_pages, company_url)
    
    # Extract positioning data
    offer = extract_offer(scraped_pages)
    industry = infer_industry(scraped_pages)
    messaging_themes = extract_messaging_themes(scraped_pages)
    positioning = extract_positioning_data(scraped_pages)
    
    # Determine quality flag
    quality_flag = determine_quality_flag(
        scraped_pages,
        voice_analysis.get('voice_samples', []),
        offer
    )
    
    # Build CompanyData structure
    company_data = {
        "company": {
            "name": company_name,
            "industry": industry,
            "offer": offer,
            "value_prop": offer,  # Use offer as value prop initially
            "target_customer": "General business owners",  # Placeholder
            "messaging_themes": messaging_themes if messaging_themes else ["Unable to determine"]
        },
        "brand_voice": {
            "formality": voice_analysis.get("formality", "Professional"),
            "complexity": voice_analysis.get("complexity", "Moderate"),
            "energy": voice_analysis.get("energy", "Balanced"),
            "pov": voice_analysis.get("pov", "Balanced"),
            "sentence_length": voice_analysis.get("sentence_length", "Medium"),
            "voice_samples": voice_analysis.get("voice_samples", [])
        },
        "content_audit": {
            "blog_present": content_audit.get("blog_present", False),
            "newsletter_signup": content_audit.get("newsletter_signup", False),
            "lead_magnets": content_audit.get("lead_magnets", []),
            "educational_gaps": content_audit.get("educational_gaps", [])
        },
        "lead_gen": {
            "ctas": content_audit.get("ctas", []),
            "friction_level": content_audit.get("friction_level", "medium"),
            "opt_in_mechanisms": content_audit.get("opt_in_mechanisms", [])
        },
        "positioning": positioning,
        "quality_flag": quality_flag
    }
    
    return json.dumps(company_data, indent=2)
