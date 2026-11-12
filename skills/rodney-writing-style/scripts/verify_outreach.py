#!/usr/bin/env python3
"""
Outreach Message Quality Verification Script

Checks cold/warm outreach messages against Rodney's writing style criteria.
Usage: python verify_outreach.py <message_file>
"""

import sys
import re
from pathlib import Path

def count_words(text):
    """Count words in text"""
    return len(text.split())

def verify_outreach(content):
    """Main verification function for outreach messages"""
    
    results = {
        'passed': [],
        'failed': [],
        'warnings': []
    }
    
    # 1. Length check (50-100 words - must be short)
    word_count = count_words(content)
    if 50 <= word_count <= 100:
        results['passed'].append(f"✅ Word count: {word_count} (target: 50-100)")
    elif word_count < 50:
        results['warnings'].append(f"⚠️  Very short: {word_count} words (min: 50)")
    else:
        results['failed'].append(f"❌ Too long: {word_count} words (max: 100)")
    
    # 2. Pattern check: Observation → Problem → Value → Ask
    content_lower = content.lower()
    
    # Observation markers
    observation_markers = ['saw', 'noticed', 'see', 'looks like', 'hiring', 'building', 'launching']
    has_observation = any(marker in content_lower for marker in observation_markers)
    
    # Problem/insight markers
    problem_markers = ['usually', 'typically', 'means', 'breaking', 'bottleneck', 'slowing']
    has_problem = any(marker in content_lower for marker in problem_markers)
    
    # Value markers (what you offer)
    value_markers = ['built', 'created', 'made', 'system', 'template', 'framework']
    has_value = any(marker in content_lower for marker in value_markers)
    
    # Ask markers (low-friction)
    ask_markers = ['worth a look', 'open to', 'can i send', 'want to see', 'interested']
    has_ask = any(marker in content_lower for marker in ask_markers)
    
    pattern_score = sum([has_observation, has_problem, has_value, has_ask])
    
    if pattern_score >= 3:
        results['passed'].append(f"✅ Good pattern structure ({pattern_score}/4 elements)")
    else:
        results['failed'].append(f"❌ Missing pattern elements ({pattern_score}/4)")
        if not has_observation:
            results['failed'].append("   - Add observation about them")
        if not has_problem:
            results['failed'].append("   - Add problem insight")
        if not has_value:
            results['failed'].append("   - Add what you built")
        if not has_ask:
            results['failed'].append("   - Add low-friction ask")
    
    # 3. Direct vs We ratio (should be about them, not you)
    you_count = len(re.findall(r'\byou\b', content_lower))
    i_count = len(re.findall(r'\bi\b', content_lower))
    
    if you_count >= i_count:
        results['passed'].append(f"✅ About them ({you_count} 'you' vs {i_count} 'I')")
    else:
        results['failed'].append(f"❌ Too much about you ({i_count} 'I' vs {you_count} 'you')")
    
    # 4. Forbidden phrases (high-pressure sales)
    forbidden_sales = [
        'limited time', 'act now', 'exclusive offer', 'special deal',
        'schedule a call', 'hop on a call', '15 minutes', '30 minutes',
        'pick your brain', 'quick chat', 'demo'
    ]
    
    found_sales = [phrase for phrase in forbidden_sales if phrase in content_lower]
    if not found_sales:
        results['passed'].append("✅ No high-pressure sales language")
    else:
        results['failed'].append(f"❌ Sales pressure: {', '.join(found_sales)}")
    
    # 5. Question check (should end with question or low-friction ask)
    sentences = [s.strip() for s in re.split(r'[.!?]+', content) if s.strip()]
    last_sentence = sentences[-1] if sentences else ''
    
    is_question = last_sentence.endswith('?') or '?' in last_sentence
    has_soft_ask = any(marker in last_sentence.lower() for marker in ask_markers)
    
    if is_question or has_soft_ask:
        results['passed'].append("✅ Ends with question or soft ask")
    else:
        results['failed'].append("❌ Doesn't end with question (add '?')")
    
    # 6. Specificity check (mentions specific thing about them)
    # Look for proper nouns or specific references
    has_capitals = bool(re.search(r'\b[A-Z][a-z]+\b', content))
    has_quotes = '"' in content or "'" in content
    has_specific_reference = has_capitals or has_quotes
    
    if has_specific_reference:
        results['passed'].append("✅ Specific reference to them")
    else:
        results['warnings'].append("⚠️  Add specific reference (their company, post, product)")
    
    # 7. Value proposition clarity
    # Should mention what you have ("template", "system", "guide", etc.)
    asset_words = ['template', 'system', 'guide', 'framework', 'checklist', 'playbook']
    mentioned_asset = [word for word in asset_words if word in content_lower]
    
    if mentioned_asset:
        results['passed'].append(f"✅ Clear asset mentioned: {', '.join(mentioned_asset)}")
    else:
        results['failed'].append("❌ No clear asset (add what you're offering)")
    
    # 8. Paragraph count (should be 2-4 short paragraphs)
    paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
    if 2 <= len(paragraphs) <= 4:
        results['passed'].append(f"✅ Good structure ({len(paragraphs)} paragraphs)")
    else:
        results['warnings'].append(f"⚠️  Paragraph count: {len(paragraphs)} (ideal: 2-4)")
    
    # 9. Sentence length (should be short and punchy)
    if sentences:
        word_counts = [len(s.split()) for s in sentences]
        avg_length = sum(word_counts) / len(word_counts)
        max_length = max(word_counts)
        
        if avg_length <= 15 and max_length <= 25:
            results['passed'].append("✅ Punchy sentences (short and clear)")
        elif max_length > 30:
            results['failed'].append(f"❌ Sentence too long (max {max_length} words, keep under 25)")
        else:
            results['warnings'].append(f"⚠️  Average sentence length: {avg_length:.1f} words")
    
    # 10. Forbidden words check
    forbidden_words = [
        'optimize', 'leverage', 'synergies', 'alignment', 'strategic',
        'very', 'really', 'super', 'amazing', 'fantastic'
    ]
    
    found_forbidden = [word for word in forbidden_words if word in content_lower]
    if not found_forbidden:
        results['passed'].append("✅ No jargon or weak words")
    else:
        results['failed'].append(f"❌ Forbidden words: {', '.join(found_forbidden)}")
    
    return results

def print_results(results):
    """Print verification results"""
    print("\n" + "="*60)
    print("OUTREACH MESSAGE VERIFICATION RESULTS")
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
        print("✅ OUTREACH APPROVED - Ready to send")
    elif len(results['failed']) <= 2:
        print("⚠️  OUTREACH NEEDS MINOR REVISIONS")
    else:
        print("❌ OUTREACH NEEDS MAJOR REVISIONS")

def main():
    if len(sys.argv) < 2:
        print("Usage: python verify_outreach.py <message_file>")
        print("Or pipe content: cat message.txt | python verify_outreach.py -")
        sys.exit(1)
    
    # Read from file or stdin
    if sys.argv[1] == '-':
        content = sys.stdin.read()
    else:
        message_file = Path(sys.argv[1])
        if not message_file.exists():
            print(f"Error: File not found: {message_file}")
            sys.exit(1)
        content = message_file.read_text()
    
    results = verify_outreach(content)
    print_results(results)
    
    # Exit code based on results
    sys.exit(0 if not results['failed'] else 1)

if __name__ == '__main__':
    main()
