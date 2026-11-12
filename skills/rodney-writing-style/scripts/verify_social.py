#!/usr/bin/env python3
"""
Social Post Quality Verification Script

Checks social media posts against Rodney's writing style criteria.
Usage: python verify_social.py <post_file>
"""

import sys
import re
from pathlib import Path

def count_words(text):
    """Count words in text"""
    return len(text.split())

def check_reading_level(text):
    """
    Estimate reading level based on sentence length and word complexity.
    Target: 5th grade (avg 10-12 words/sentence, simple vocabulary)
    """
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    if not sentences:
        return False, "No sentences found"
    
    avg_words = sum(len(s.split()) for s in sentences) / len(sentences)
    
    # Check for complex words (3+ syllables, rough heuristic)
    complex_words = []
    forbidden = ['optimize', 'leverage', 'strategic', 'synergies', 'alignment',
                 'best-in-class', 'world-class', 'utilize', 'implement', 'execute']
    
    for word in text.lower().split():
        clean_word = re.sub(r'[^\w]', '', word)
        if clean_word in forbidden:
            complex_words.append(word)
    
    issues = []
    if avg_words > 15:
        issues.append(f"Sentences too long (avg {avg_words:.1f} words, target <15)")
    if complex_words:
        issues.append(f"Business jargon found: {', '.join(set(complex_words))}")
    
    return len(issues) == 0, issues

def verify_social_post(content):
    """Main verification function for social posts"""
    
    results = {
        'passed': [],
        'failed': [],
        'warnings': []
    }
    
    # 1. Length check (75-150 words)
    word_count = count_words(content)
    if 75 <= word_count <= 150:
        results['passed'].append(f"✅ Word count: {word_count} (target: 75-150)")
    elif word_count < 75:
        results['failed'].append(f"❌ Too short: {word_count} words (min: 75)")
    else:
        results['warnings'].append(f"⚠️  Long: {word_count} words (max: 150)")
    
    # 2. Hook check (first line)
    lines = [l.strip() for l in content.split('\n') if l.strip()]
    if lines:
        first_line = lines[0]
        first_word_count = count_words(first_line)
        
        # Check for contrarian markers, questions, or bold statements
        hook_markers = ['why', 'how', 'if you', 'mistake', 'wrong', 'stop', "you're", "don't"]
        has_marker = any(marker in first_line.lower() for marker in hook_markers)
        
        # Check for numbers in hook
        has_number = bool(re.search(r'\d+', first_line))
        
        if first_word_count <= 15 and (has_marker or has_number):
            results['passed'].append("✅ Strong hook (short + marker/number)")
        elif first_word_count > 15:
            results['failed'].append(f"❌ Hook too long: {first_word_count} words (max: 15)")
        else:
            results['warnings'].append("⚠️  Hook could be stronger (add contrarian/number)")
    
    # 3. White space check (line breaks for readability)
    line_count = len(lines)
    avg_words_per_line = word_count / line_count if line_count else 0
    
    if avg_words_per_line <= 20:
        results['passed'].append("✅ Good white space (short lines)")
    else:
        results['failed'].append(f"❌ Walls of text (avg {avg_words_per_line:.1f} words/line, target <20)")
    
    # 4. CTA check (last 1-2 lines)
    if len(lines) >= 2:
        last_lines = ' '.join(lines[-2:]).lower()
        cta_markers = ['reply', 'dm', 'comment', 'book', 'get', 'download', 'click']
        has_cta = any(marker in last_lines for marker in cta_markers)
        
        if has_cta:
            results['passed'].append("✅ Clear CTA present")
        else:
            results['failed'].append("❌ No clear CTA (add Reply/DM/Book directive)")
    
    # 5. Forbidden words check
    forbidden_patterns = [
        (r'\b(optimize|leverage|strategic|synergies|alignment)\b', "business jargon"),
        (r'\b(might|could|probably|sort of|kinda|maybe)\b', "weak words"),
        (r'\b(very|really|super|extremely)\b', "empty intensifiers"),
        (r'!!!+', "excessive exclamation marks")
    ]
    
    found_forbidden = []
    for pattern, category in forbidden_patterns:
        matches = re.findall(pattern, content.lower())
        if matches:
            found_forbidden.append(f"{category}: {', '.join(set(matches))}")
    
    if not found_forbidden:
        results['passed'].append("✅ No forbidden words")
    else:
        for issue in found_forbidden:
            results['failed'].append(f"❌ {issue}")
    
    # 6. Direct address check ("you")
    you_count = len(re.findall(r'\byou\b', content.lower()))
    we_count = len(re.findall(r'\bwe\b', content.lower()))
    
    if you_count > we_count:
        results['passed'].append(f"✅ Direct 'you' address ({you_count} vs {we_count} 'we')")
    else:
        results['failed'].append(f"❌ Too much 'we' ({we_count} vs {you_count} 'you')")
    
    # 7. Reading level check
    readable, reading_issues = check_reading_level(content)
    if readable:
        results['passed'].append("✅ Reading level appropriate (5th grade)")
    else:
        for issue in reading_issues:
            results['failed'].append(f"❌ {issue}")
    
    # 8. Action words check
    action_words = ['cut', 'build', 'ship', 'automate', 'start', 'stop', 'get', 'make']
    action_count = sum(1 for word in action_words if word in content.lower())
    
    if action_count >= 2:
        results['passed'].append(f"✅ Action words present ({action_count})")
    else:
        results['warnings'].append("⚠️  Add more action words (cut, build, ship, start)")
    
    return results

def print_results(results):
    """Print verification results"""
    print("\n" + "="*60)
    print("SOCIAL POST VERIFICATION RESULTS")
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
        print("✅ POST APPROVED - Ready to publish")
    elif len(results['failed']) <= 2:
        print("⚠️  POST NEEDS MINOR REVISIONS")
    else:
        print("❌ POST NEEDS MAJOR REVISIONS")

def main():
    if len(sys.argv) < 2:
        print("Usage: python verify_social.py <post_file>")
        print("Or pipe content: echo 'Your post...' | python verify_social.py -")
        sys.exit(1)
    
    # Read from file or stdin
    if sys.argv[1] == '-':
        content = sys.stdin.read()
    else:
        post_file = Path(sys.argv[1])
        if not post_file.exists():
            print(f"Error: File not found: {post_file}")
            sys.exit(1)
        content = post_file.read_text()
    
    results = verify_social_post(content)
    print_results(results)
    
    # Exit code based on results
    sys.exit(0 if not results['failed'] else 1)

if __name__ == '__main__':
    main()
