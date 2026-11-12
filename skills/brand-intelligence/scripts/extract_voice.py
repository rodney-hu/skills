#!/usr/bin/env python3
"""
Brand voice analyzer for company research

Analyzes text content across 5 voice dimensions and extracts representative samples.

Usage:
    voice_analysis = extract_voice(scraped_pages)
"""

import re
from typing import Dict, List, Tuple
from collections import Counter


def analyze_formality(text: str) -> str:
    """
    Analyze formality level based on language patterns.
    
    Args:
        text: Combined text from website
        
    Returns:
        "Casual", "Approachable", or "Professional"
    """
    text_lower = text.lower()
    
    # Casual indicators
    casual_count = 0
    casual_count += len(re.findall(r'\b(hey|hi|yo|cool|awesome|yeah|nope|gonna|wanna|kinda|sorta)\b', text_lower))
    casual_count += len(re.findall(r'\!', text))  # Exclamation marks
    casual_count += len(re.findall(r'[;)]', text))  # Emoticons
    
    # Professional indicators
    prof_count = 0
    prof_count += len(re.findall(r'\b(pursuant|heretofore|facilitate|leverage|synergy|optimize|strategic|enterprise|solution|robust|comprehensive)\b', text_lower))
    prof_count += len(re.findall(r'\b(we are pleased|we are committed|we believe|furthermore|additionally|consequently)\b', text_lower))
    
    # Calculate ratio
    total_words = len(text.split())
    casual_ratio = casual_count / max(total_words / 100, 1)
    prof_ratio = prof_count / max(total_words / 100, 1)
    
    if casual_ratio > 2.0:
        return "Casual"
    elif prof_ratio > 1.5:
        return "Professional"
    else:
        return "Approachable"


def analyze_complexity(text: str) -> str:
    """
    Analyze language complexity based on word length and jargon.
    
    Args:
        text: Combined text from website
        
    Returns:
        "Simple", "Moderate", or "Technical"
    """
    words = text.split()
    
    if not words:
        return "Moderate"
    
    # Calculate average word length
    avg_word_len = sum(len(word.strip('.,!?;:')) for word in words) / len(words)
    
    # Count technical/jargon terms
    text_lower = text.lower()
    jargon_count = 0
    jargon_count += len(re.findall(r'\b(api|sdk|saas|ai|ml|automation|integration|infrastructure|architecture|deployment|scalability)\b', text_lower))
    jargon_count += len(re.findall(r'\b(algorithm|analytics|optimization|ecosystem|framework|protocol|methodology)\b', text_lower))
    
    jargon_ratio = jargon_count / max(len(words) / 100, 1)
    
    if avg_word_len < 5.0 and jargon_ratio < 1.0:
        return "Simple"
    elif avg_word_len > 6.5 or jargon_ratio > 3.0:
        return "Technical"
    else:
        return "Moderate"


def analyze_energy(text: str) -> str:
    """
    Analyze energy level based on punctuation and word choice.
    
    Args:
        text: Combined text from website
        
    Returns:
        "Reserved", "Balanced", or "Energetic"
    """
    text_lower = text.lower()
    
    # Energy indicators
    exclamations = len(re.findall(r'!', text))
    action_words = len(re.findall(r'\b(start|launch|grow|transform|revolutionize|accelerate|boost|skyrocket|supercharge)\b', text_lower))
    intensifiers = len(re.findall(r'\b(amazing|incredible|powerful|extraordinary|outstanding|exceptional|remarkable)\b', text_lower))
    
    energy_score = exclamations + (action_words * 2) + (intensifiers * 2)
    words_count = len(text.split())
    energy_ratio = energy_score / max(words_count / 100, 1)
    
    if energy_ratio < 2.0:
        return "Reserved"
    elif energy_ratio > 8.0:
        return "Energetic"
    else:
        return "Balanced"


def analyze_pov(text: str) -> str:
    """
    Analyze point of view (focus on we vs. you).
    
    Args:
        text: Combined text from website
        
    Returns:
        "We-focused", "Balanced", or "You-focused"
    """
    text_lower = text.lower()
    
    # Count pronouns
    we_count = len(re.findall(r'\b(we|our|us)\b', text_lower))
    you_count = len(re.findall(r'\b(you|your|you\'re|you\'ll)\b', text_lower))
    
    if we_count == 0 and you_count == 0:
        return "Balanced"
    
    ratio = you_count / max(we_count, 1)
    
    if ratio < 0.5:
        return "We-focused"
    elif ratio > 2.0:
        return "You-focused"
    else:
        return "Balanced"


def analyze_sentence_length(text: str) -> str:
    """
    Analyze average sentence length.
    
    Args:
        text: Combined text from website
        
    Returns:
        "Short", "Medium", or "Long"
    """
    # Split into sentences (rough approximation)
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    if not sentences:
        return "Medium"
    
    avg_words_per_sentence = sum(len(s.split()) for s in sentences) / len(sentences)
    
    if avg_words_per_sentence < 12:
        return "Short"
    elif avg_words_per_sentence > 20:
        return "Long"
    else:
        return "Medium"


def extract_voice_samples(pages: Dict[str, str], count: int = 3) -> List[str]:
    """
    Extract representative sentence samples from website content.
    
    Args:
        pages: Dict mapping page types to text content
        count: Number of samples to extract
        
    Returns:
        List of representative sentences
    """
    # Combine all text
    all_text = ' '.join(pages.values())
    
    # Split into sentences
    sentences = re.split(r'[.!?]+', all_text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # Filter for quality sentences (8-25 words, not too generic)
    quality_sentences = []
    for sent in sentences:
        words = sent.split()
        if 8 <= len(words) <= 25:
            # Skip overly generic sentences
            sent_lower = sent.lower()
            if not any(generic in sent_lower for generic in ['click here', 'learn more', 'contact us', 'sign up', 'get started', 'copyright']):
                quality_sentences.append(sent)
    
    # Return diverse samples (first third, middle third, last third)
    if len(quality_sentences) < count:
        return quality_sentences[:count]
    
    samples = []
    step = len(quality_sentences) // count
    for i in range(count):
        idx = min(i * step, len(quality_sentences) - 1)
        samples.append(quality_sentences[idx])
    
    return samples


def extract_voice(scraped_pages: Dict[str, str]) -> Dict:
    """
    Analyze brand voice across 5 dimensions and extract representative samples.
    
    Args:
        scraped_pages: Dict mapping page types to extracted text
        
    Returns:
        Dict containing voice analysis:
            - formality: str
            - complexity: str
            - energy: str
            - pov: str
            - sentence_length: str
            - voice_samples: List[str]
    """
    if not scraped_pages:
        return {
            "formality": "Professional",
            "complexity": "Moderate",
            "energy": "Balanced",
            "pov": "Balanced",
            "sentence_length": "Medium",
            "voice_samples": []
        }
    
    # Combine all text for analysis
    combined_text = ' '.join(scraped_pages.values())
    
    return {
        "formality": analyze_formality(combined_text),
        "complexity": analyze_complexity(combined_text),
        "energy": analyze_energy(combined_text),
        "pov": analyze_pov(combined_text),
        "sentence_length": analyze_sentence_length(combined_text),
        "voice_samples": extract_voice_samples(scraped_pages, count=3)
    }
