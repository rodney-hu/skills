#!/usr/bin/env python3
"""
Email Quality Verification Script

Checks emails against Rodney's writing style criteria.
Usage: python verify_email.py <email_file>
"""

import sys
import re
from pathlib import Path

def count_words(text):
    """Count words in text"""
    return len(text.split())

def extract_subject(content):
    """Extract subject line from email"""
    subject_match = re.search(r'Subject:\s*(.+)', content, re.IGNORECASE)
    return subject_match.group(1).strip() if subject_match else None

def verify_email(content):
    """Main verification function for emails"""
    
    results = {
        'passed': [],
        'failed': [],
        'warnings': []
    }
    
    # 1. Subject line check
    subject = extract_subject(content)
    if subject:
        subject_words = count_words(subject)
        
        # Check subject length
        if 3 <= subject_words <= 10:
            results['passed'].append(f"✅ Subject length good: {subject_words} words (3-10)")
        else:
            results['failed'].append(f"❌ Subject too {'short' if subject_words < 3 else 'long'}: {subject_words} words")
        
        # Check for curiosity markers in subject
        curiosity_markers = ['why', 'how', 'what', 'when', 'mistake', 'wrong', 'secret', 'fast']
        has_curiosity = any(marker in subject.lower() for marker in curiosity_markers)
        
        # Check for numbers in subject
        has_number = bool(re.search(r'\d+', subject))
        
        if has_curiosity or has_number:
            results['passed'].append("✅ Subject has hook (curiosity/number)")
        else:
            results['warnings'].append("⚠️  Subject could be stronger (add hook/number)")
    else:
        results['failed'].append("❌ No subject line found (format: 'Subject: ...')")
    
    # Remove subject line for body analysis
    body = re.sub(r'Subject:.+\n', '', content, flags=re.IGNORECASE).strip()
    
    # 2. Length check (150-250 words)
    word_count = count_words(body)
    if 150 <= word_count <= 250:
        results['passed'].append(f"✅ Word count: {word_count} (target: 150-250)")
    elif word_count < 150:
        results['failed'].append(f"❌ Too short: {word_count} words (min: 150)")
    else:
        results['warnings'].append(f"⚠️  Long: {word_count} words (max: 250)")
    
    # 3. Opening check (first paragraph)
    paragraphs = [p.strip() for p in body.split('\n\n') if p.strip()]
    if paragraphs:
        opening = paragraphs[0]
        opening_words = count_words(opening)
        
        # Opening should be punchy (under 40 words)
        if opening_words <= 40:
            results['passed'].append("✅ Strong opening (concise)")
        else:
            results['failed'].append(f"❌ Opening too long: {opening_words} words (max: 40)")
        
        # Check for direct address in opening
        if 'you' in opening.lower():
            results['passed'].append("✅ Direct 'you' in opening")
        else:
            results['warnings'].append("⚠️  Opening lacks direct 'you' address")
    
    # 4. Structure check (paragraphs)
    if len(paragraphs) >= 3:
        results['passed'].append(f"✅ Good structure ({len(paragraphs)} paragraphs)")
    else:
        results['failed'].append(f"❌ Too few paragraphs ({len(paragraphs)}, need 3+)")
    
    # 5. CTA check (should have clear call-to-action)
    cta_patterns = [
        r'\*\*.*?\*\*',  # Bold text (markdown)
        r'(reply|book|click|download|get|grab|claim)',  # Action verbs
        r'\[.*?\]\(.*?\)'  # Links
    ]
    
    last_para = paragraphs[-1] if paragraphs else ''
    has_cta = any(re.search(pattern, last_para, re.IGNORECASE) for pattern in cta_patterns)
    
    if has_cta:
        results['passed'].append("✅ Clear CTA present")
    else:
        results['failed'].append("❌ No clear CTA (add bold action + link)")
    
    # 6. Forbidden words check
    forbidden_patterns = [
        (r'\b(optimize|leverage|strategic|synergies|alignment)\b', "business jargon"),
        (r'\b(might|could|probably|sort of|kinda|maybe)\b', "weak words"),
        (r'\b(very|really|super|extremely)\b', "empty intensifiers")
    ]
    
    found_forbidden = []
    for pattern, category in forbidden_patterns:
        matches = re.findall(pattern, body.lower())
        if matches:
            found_forbidden.append(f"{category}: {', '.join(set(matches))}")
    
    if not found_forbidden:
        results['passed'].append("✅ No forbidden words")
    else:
        for issue in found_forbidden:
            results['failed'].append(f"❌ {issue}")
    
    # 7. Direct vs We ratio
    you_count = len(re.findall(r'\byou\b', body.lower()))
    we_count = len(re.findall(r'\bwe\b', body.lower()))
    
    if you_count >= we_count:
        results['passed'].append(f"✅ Direct address ({you_count} 'you' vs {we_count} 'we')")
    else:
        results['failed'].append(f"❌ Too much 'we' ({we_count} vs {you_count} 'you')")
    
    # 8. Concrete numbers check
    numbers = re.findall(r'\d+', body)
    if len(numbers) >= 2:
        results['passed'].append(f"✅ Concrete numbers present ({len(numbers)})")
    else:
        results['warnings'].append("⚠️  Add more specific numbers (time, cost, results)")
    
    # 9. P.S. check (powerful for emails)
    has_ps = bool(re.search(r'P\.S\.', body, re.IGNORECASE))
    if has_ps:
        results['passed'].append("✅ P.S. included (good engagement)")
    else:
        results['warnings'].append("⚠️  Consider adding P.S. with key insight")
    
    # 10. Reading flow check (sentence variety)
    sentences = re.split(r'[.!?]+', body)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    if sentences:
        word_counts = [len(s.split()) for s in sentences]
        avg_length = sum(word_counts) / len(word_counts)
        
        # Check for variety (some short, some longer)
        has_short = any(count <= 8 for count in word_counts)
        has_medium = any(9 <= count <= 15 for count in word_counts)
        
        if has_short and has_medium:
            results['passed'].append("✅ Good sentence variety")
        elif avg_length > 20:
            results['failed'].append(f"❌ Sentences too long (avg {avg_length:.1f} words)")
        else:
            results['warnings'].append("⚠️  Add more sentence variety")
    
    return results

def print_results(results):
    """Print verification results"""
    print("\n" + "="*60)
    print("EMAIL VERIFICATION RESULTS")
    print("="*60)
    
    if results['passed']:
        print("\n✅ PASSED CHECKS:")
        for item in results['passed']:
            print(f"  {item}")
    
    if results['warnings']:
        print("\n⚠️  WARNINGS:")
        for item in results['warnings']:
            print(f"  {item}")
    
    if results['failed']:
        print("\n❌ FAILED CHECKS:")
        for item in results['failed']:
            print(f"  {item}")
    
    print("\n" + "="*60)
    
    total_checks = len(results['passed']) + len(results['failed'])
    passed_checks = len(results['passed'])
    pass_rate = (passed_checks / total_checks * 100) if total_checks else 0
    
    print(f"PASS RATE: {passed_checks}/{total_checks} ({pass_rate:.0f}%)")
    print("="*60 + "\n")
    
    # Overall verdict
    if not results['failed']:
        print("✅ EMAIL APPROVED - Ready to send")
    elif len(results['failed']) <= 2:
        print("⚠️  EMAIL NEEDS MINOR REVISIONS")
    else:
        print("❌ EMAIL NEEDS MAJOR REVISIONS")

def main():
    if len(sys.argv) < 2:
        print("Usage: python verify_email.py <email_file>")
        print("Or pipe content: cat email.txt | python verify_email.py -")
        sys.exit(1)
    
    # Read from file or stdin
    if sys.argv[1] == '-':
        content = sys.stdin.read()
    else:
        email_file = Path(sys.argv[1])
        if not email_file.exists():
            print(f"Error: File not found: {email_file}")
            sys.exit(1)
        content = email_file.read_text()
    
    results = verify_email(content)
    print_results(results)
    
    # Exit code based on results
    sys.exit(0 if not results['failed'] else 1)

if __name__ == '__main__':
    main()
