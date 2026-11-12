#!/usr/bin/env python3
"""
Content infrastructure auditor for company research

Detects blog, newsletter signup, lead magnets, CTAs, and educational gaps.

Usage:
    content_audit = audit_content(scraped_pages)
"""

import re
from typing import Dict, List


def detect_blog(pages: Dict[str, str]) -> bool:
    """
    Detect if website has a blog section.
    
    Args:
        pages: Dict mapping page types to text content
        
    Returns:
        True if blog detected
    """
    combined_text = ' '.join(pages.values()).lower()
    
    # Look for blog indicators
    blog_patterns = [
        r'\bblog\b',
        r'\barticles?\b',
        r'\bposts?\b',
        r'\bnews\b',
        r'\binsights\b',
        r'\bresources\b'
    ]
    
    for pattern in blog_patterns:
        if re.search(pattern, combined_text):
            return True
    
    return False


def detect_newsletter_signup(pages: Dict[str, str]) -> bool:
    """
    Detect if website has newsletter signup.
    
    Args:
        pages: Dict mapping page types to text content
        
    Returns:
        True if newsletter signup detected
    """
    combined_text = ' '.join(pages.values()).lower()
    
    # Look for newsletter indicators
    newsletter_patterns = [
        r'\bnewsletter\b',
        r'\bemail\s+list\b',
        r'\bsubscribe\b',
        r'\bget\s+updates\b',
        r'\bjoin\s+our\s+list\b',
        r'\bstay\s+informed\b'
    ]
    
    for pattern in newsletter_patterns:
        if re.search(pattern, combined_text):
            return True
    
    return False


def extract_lead_magnets(pages: Dict[str, str]) -> List[str]:
    """
    Extract lead magnet offerings from website.
    
    Args:
        pages: Dict mapping page types to text content
        
    Returns:
        List of detected lead magnets
    """
    combined_text = ' '.join(pages.values())
    lead_magnets = []
    
    # Look for common lead magnet patterns
    patterns = [
        (r'(?:free|download)\s+(?:our\s+)?([a-z\s]+(?:guide|ebook|template|checklist|workbook|toolkit|report|whitepaper))', 'guide/resource'),
        (r'(?:get|download)\s+(?:the|our|your)\s+([a-z\s]+(?:checklist|template|guide|ebook|workbook))', 'downloadable'),
        (r'(?:free|complimentary)\s+([a-z\s]+(?:consultation|audit|assessment|analysis|demo))', 'consultation/demo'),
        (r'(\d+[\-\s](?:day|week|step)\s+[a-z\s]+(?:course|challenge|bootcamp|training))', 'course/challenge'),
    ]
    
    for pattern, magnet_type in patterns:
        matches = re.findall(pattern, combined_text.lower())
        for match in matches:
            # Clean up the match
            cleaned = match.strip().title()
            if len(cleaned) > 5 and cleaned not in lead_magnets:
                lead_magnets.append(cleaned)
    
    return lead_magnets[:5]  # Limit to 5 most prominent


def identify_educational_gaps(pages: Dict[str, str], has_blog: bool, has_newsletter: bool, lead_magnets: List[str]) -> List[str]:
    """
    Identify missing educational content types.
    
    Args:
        pages: Dict mapping page types to text content
        has_blog: Whether blog was detected
        has_newsletter: Whether newsletter signup was detected
        lead_magnets: List of detected lead magnets
        
    Returns:
        List of missing content types
    """
    gaps = []
    
    # Check for missing content types
    if not has_blog:
        gaps.append("Blog/articles")
    
    if not has_newsletter:
        gaps.append("Newsletter")
    
    # Check for specific content types
    combined_text = ' '.join(pages.values()).lower()
    
    content_types = {
        "Email course": r'\b(?:email\s+)?(?:course|series)\b',
        "Video tutorials": r'\b(?:video|tutorial|webinar)\b',
        "Case studies": r'\b(?:case\s+stud|success\s+stor|customer\s+stor)\b',
        "Templates/tools": r'\b(?:template|tool|calculator|generator)\b',
        "Free trial": r'\b(?:free\s+trial|trial\s+version)\b',
        "Demo": r'\b(?:demo|demonstration|walkthrough)\b',
    }
    
    for content_type, pattern in content_types.items():
        if not re.search(pattern, combined_text):
            gaps.append(content_type)
    
    return gaps[:5]  # Return top 5 gaps


def extract_ctas(pages: Dict[str, str]) -> List[str]:
    """
    Extract call-to-action phrases from website.
    
    Args:
        pages: Dict mapping page types to text content
        
    Returns:
        List of unique CTAs found
    """
    combined_text = ' '.join(pages.values())
    ctas = []
    
    # Common CTA patterns
    cta_patterns = [
        r'\b(get\s+started|start\s+(?:now|today|free))\b',
        r'\b(book\s+(?:a\s+)?(?:demo|call|consultation))\b',
        r'\b(sign\s+up|join\s+(?:now|today|us))\b',
        r'\b(request\s+(?:a\s+)?(?:demo|quote|consultation))\b',
        r'\b(try\s+(?:it\s+)?free|free\s+trial)\b',
        r'\b(download\s+(?:now|today)?)\b',
        r'\b(schedule\s+(?:a\s+)?(?:call|demo|meeting))\b',
        r'\b(contact\s+us|reach\s+out)\b',
        r'\b(learn\s+more)\b',
        r'\b(subscribe(?:\s+now)?)\b',
    ]
    
    for pattern in cta_patterns:
        matches = re.finditer(pattern, combined_text.lower())
        for match in matches:
            cta = match.group(0).strip().title()
            if cta not in ctas:
                ctas.append(cta)
    
    return ctas


def assess_friction_level(pages: Dict[str, str], ctas: List[str]) -> str:
    """
    Assess friction level of conversion process.
    
    Args:
        pages: Dict mapping page types to text content
        ctas: List of detected CTAs
        
    Returns:
        "high", "medium", or "low" friction level
    """
    combined_text = ' '.join(pages.values()).lower()
    
    # Low friction indicators
    low_friction_count = 0
    low_friction_count += len(re.findall(r'\bfree\b', combined_text))
    low_friction_count += len(re.findall(r'\bno\s+(?:credit\s+card|payment)\b', combined_text))
    low_friction_count += len(re.findall(r'\binstant\s+access\b', combined_text))
    low_friction_count += 2 if 'free trial' in combined_text else 0
    
    # High friction indicators
    high_friction_count = 0
    high_friction_count += len(re.findall(r'\b(?:schedule|book)\s+(?:a\s+)?(?:call|demo|meeting)\b', combined_text))
    high_friction_count += len(re.findall(r'\b(?:contact|speak\s+with)\s+(?:us|sales)\b', combined_text))
    high_friction_count += 2 if re.search(r'\brequire[sd]?\b', combined_text) else 0
    
    # Calculate friction score
    if low_friction_count > high_friction_count * 2:
        return "low"
    elif high_friction_count > low_friction_count * 2:
        return "high"
    else:
        return "medium"


def identify_opt_in_mechanisms(pages: Dict[str, str], has_newsletter: bool, lead_magnets: List[str]) -> List[str]:
    """
    Identify opt-in mechanisms available on the site.
    
    Args:
        pages: Dict mapping page types to text content
        has_newsletter: Whether newsletter signup was detected
        lead_magnets: List of detected lead magnets
        
    Returns:
        List of opt-in mechanisms
    """
    mechanisms = []
    combined_text = ' '.join(pages.values()).lower()
    
    # Check for various opt-in types
    if has_newsletter:
        mechanisms.append("Newsletter signup")
    
    if lead_magnets:
        mechanisms.append("Lead magnet download")
    
    if re.search(r'\bfree\s+trial\b', combined_text):
        mechanisms.append("Free trial")
    
    if re.search(r'\b(?:demo|demonstration)\b', combined_text):
        mechanisms.append("Demo request")
    
    if re.search(r'\b(?:consultation|assessment)\b', combined_text):
        mechanisms.append("Free consultation")
    
    if re.search(r'\bwebinar\b', combined_text):
        mechanisms.append("Webinar registration")
    
    return mechanisms


def audit_content(scraped_pages: Dict[str, str]) -> Dict:
    """
    Audit content infrastructure and lead generation mechanisms.
    
    Args:
        scraped_pages: Dict mapping page types to extracted text
        
    Returns:
        Dict containing:
            - blog_present: bool
            - newsletter_signup: bool
            - lead_magnets: List[str]
            - educational_gaps: List[str]
            - ctas: List[str]
            - friction_level: str
            - opt_in_mechanisms: List[str]
    """
    if not scraped_pages:
        return {
            "blog_present": False,
            "newsletter_signup": False,
            "lead_magnets": [],
            "educational_gaps": ["Insufficient data to analyze"],
            "ctas": [],
            "friction_level": "medium",
            "opt_in_mechanisms": []
        }
    
    # Run all audits
    has_blog = detect_blog(scraped_pages)
    has_newsletter = detect_newsletter_signup(scraped_pages)
    lead_magnets = extract_lead_magnets(scraped_pages)
    educational_gaps = identify_educational_gaps(scraped_pages, has_blog, has_newsletter, lead_magnets)
    ctas = extract_ctas(scraped_pages)
    friction_level = assess_friction_level(scraped_pages, ctas)
    opt_in_mechanisms = identify_opt_in_mechanisms(scraped_pages, has_newsletter, lead_magnets)
    
    return {
        "blog_present": has_blog,
        "newsletter_signup": has_newsletter,
        "lead_magnets": lead_magnets,
        "educational_gaps": educational_gaps,
        "ctas": ctas,
        "friction_level": friction_level,
        "opt_in_mechanisms": opt_in_mechanisms
    }
