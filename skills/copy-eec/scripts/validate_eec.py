#!/usr/bin/env python3
"""
Validate EEC quality using PGA checklists.

Usage:
    python validate_eec.py --offer offer.json --emails email_dir/ --report validation_report.json
"""

import json
import argparse
import re
from pathlib import Path
from typing import Dict, List


class EECValidator:
    """Validates EEC quality against PGA standards."""
    
    VAGUE_WORDS = ['struggle', 'difficult', 'hard', 'frustrated', 'overwhelmed', 'challenging']
    BUSINESS_JARGON = ['leverage', 'optimize', 'synergies', 'utilize', 'implement', 'execute']
    WEAK_WORDS = ['might', 'could', 'maybe', 'probably', 'sort of', 'kinda']
    
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.passed = []
    
    def validate_offer(self, offer: Dict) -> Dict:
        """Validate offer against offer checklist."""
        checks = {}
        
        # Check specific audience
        if 'people' not in offer.get('subtitle', '').lower():
            self.passed.append("✅ Specific audience (not 'people')")
        else:
            self.errors.append("❌ Uses 'people' instead of specific audience")
        
        # Check 5 mistakes
        if len(offer.get('mistakes', [])) == 5:
            self.passed.append("✅ Has 5 mistakes")
        else:
            self.errors.append(f"❌ Has {len(offer.get('mistakes', []))} mistakes (need 5)")
        
        # Check 3 outcomes
        if len(offer.get('top_3_outcomes', [])) == 3:
            self.passed.append("✅ Has 3 top outcomes")
        else:
            self.errors.append(f"❌ Has {len(offer.get('top_3_outcomes', []))} outcomes (need 3)")
        
        # Check tangibility
        tangible_count = 0
        for outcome in offer.get('top_3_outcomes', []):
            if re.search(r'\d+', outcome) or any(word in outcome.lower() for word in ['$', 'hours', 'days', 'weeks']):
                tangible_count += 1
            else:
                for vague in self.VAGUE_WORDS:
                    if vague in outcome.lower():
                        self.warnings.append(f"⚠️  Outcome contains vague word '{vague}': {outcome[:50]}...")
        
        if tangible_count >= 2:
            self.passed.append(f"✅ Outcomes are tangible ({tangible_count}/3 have numbers/specifics)")
        else:
            self.errors.append(f"❌ Only {tangible_count}/3 outcomes are tangible")
        
        # Check golden word
        golden_words = ['roadmap', 'blueprint', 'system', 'guide', 'playbook', 'toolkit', 'plan', 'map']
        if any(word in offer.get('name', '').lower() for word in golden_words):
            self.passed.append("✅ Uses golden word in name")
        else:
            self.warnings.append("⚠️  No golden word in name")
        
        # Check main whisper
        if '(And How To Solve Them)' in offer.get('complete_offer', ''):
            self.passed.append("✅ Has main whisper")
        else:
            self.errors.append("❌ Missing '(And How To Solve Them)'")
        
        return checks
    
    def validate_email(self, email_text: str, day: int) -> Dict:
        """Validate email against copy checklist."""
        checks = {}
        
        # Check sections
        sections = ['### The Mistake:', '### The Reason This Happens:', '### How To Fix It']
        sections_found = sum(1 for s in sections if s in email_text)
        
        if sections_found == 3:
            self.passed.append(f"✅ Day {day}: Has all 5 sections")
        else:
            self.errors.append(f"❌ Day {day}: Missing sections ({sections_found}/3 headers found)")
        
        # Check 1/3/1 rhythm (basic check)
        if email_text.count('\n\n') >= 15:
            self.passed.append(f"✅ Day {day}: Appears to follow 1/3/1 rhythm")
        else:
            self.warnings.append(f"⚠️  Day {day}: May not follow 1/3/1 rhythm (check manually)")
        
        # Check bullet details
        bullet_pattern = r'- \*\*[^:]+:\*\* .{50,}'
        detailed_bullets = len(re.findall(bullet_pattern, email_text))
        
        if detailed_bullets >= 9:
            self.passed.append(f"✅ Day {day}: Has detailed bullets (1-3 sentences each)")
        else:
            self.warnings.append(f"⚠️  Day {day}: Only {detailed_bullets} detailed bullets (need 9+)")
        
        # Check "you" language
        you_count = email_text.lower().count(' you ')
        we_count = email_text.lower().count(' we ')
        
        if you_count > we_count * 2:
            self.passed.append(f"✅ Day {day}: Uses 'you' language")
        else:
            self.warnings.append(f"⚠️  Day {day}: Uses 'we' more than 'you' ({we_count} vs {you_count})")
        
        # Check business jargon
        jargon_found = [word for word in self.BUSINESS_JARGON if word in email_text.lower()]
        
        if jargon_found:
            self.warnings.append(f"⚠️  Day {day}: Contains jargon: {', '.join(jargon_found)}")
        else:
            self.passed.append(f"✅ Day {day}: No business jargon")
        
        # Check weak words
        weak_found = [word for word in self.WEAK_WORDS if word in email_text.lower()]
        
        if weak_found:
            self.warnings.append(f"⚠️  Day {day}: Contains weak words: {', '.join(weak_found)}")
        else:
            self.passed.append(f"✅ Day {day}: No weak language")
        
        # Check word count
        word_count = len(email_text.split())
        if word_count < 1000:
            self.passed.append(f"✅ Day {day}: Under 1000 words ({word_count})")
        else:
            self.warnings.append(f"⚠️  Day {day}: Over 1000 words ({word_count})")
        
        return checks
    
    def generate_report(self) -> Dict:
        """Generate validation report."""
        return {
            'passed': self.passed,
            'warnings': self.warnings,
            'errors': self.errors,
            'total_passed': len(self.passed),
            'total_warnings': len(self.warnings),
            'total_errors': len(self.errors),
            'is_valid': len(self.errors) == 0
        }


def main():
    parser = argparse.ArgumentParser(description='Validate PGA EEC quality')
    parser.add_argument('--offer', help='Offer JSON file')
    parser.add_argument('--emails', help='Directory with email files')
    parser.add_argument('--report', help='Output validation report JSON')
    
    args = parser.parse_args()
    
    validator = EECValidator()
    
    # Validate offer
    if args.offer:
        with open(args.offer, 'r') as f:
            offer = json.load(f)
        validator.validate_offer(offer)
    
    # Validate emails
    if args.emails:
        email_dir = Path(args.emails)
        for i, email_file in enumerate(sorted(email_dir.glob('day*.txt')), 1):
            with open(email_file, 'r') as f:
                email_text = f.read()
            validator.validate_email(email_text, i)
    
    # Generate report
    report = validator.generate_report()
    
    # Output
    if args.report:
        with open(args.report, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"✅ Validation report saved to {args.report}")
    
    # Print summary
    print("\n" + "="*60)
    print("VALIDATION SUMMARY")
    print("="*60)
    
    if report['is_valid']:
        print(f"\n✅ PASSED - {report['total_passed']} checks passed")
    else:
        print(f"\n❌ FAILED - {report['total_errors']} errors found")
    
    if report['total_warnings'] > 0:
        print(f"⚠️  {report['total_warnings']} warnings")
    
    print(f"\nPassed: {report['total_passed']}")
    print(f"Warnings: {report['total_warnings']}")
    print(f"Errors: {report['total_errors']}")
    
    # Print details
    if report['errors']:
        print("\n❌ ERRORS:")
        for error in report['errors']:
            print(f"  {error}")
    
    if report['warnings']:
        print("\n⚠️  WARNINGS:")
        for warning in report['warnings']:
            print(f"  {warning}")


if __name__ == '__main__':
    main()
