#!/usr/bin/env python3
"""
Package EEC into deployment-ready formats.

Usage:
    python package_eec.py --emails email_dir/ --format convertkit --output eec_package/
"""

import json
import argparse
from pathlib import Path
from typing import Dict, List


class EECPackager:
    """Packages EEC into various deployment formats."""
    
    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        self.output_dir.mkdir(exist_ok=True, parents=True)
    
    def package_for_convertkit(self, emails: List[str], offer: Dict) -> str:
        """Package for ConvertKit (CSV format)."""
        csv_lines = ["Day,Subject,Content"]
        
        for i, email in enumerate(emails):
            lines = email.split('\n')
            subject = lines[0].replace('Subject: ', '').strip()
            content = '\n'.join(lines[2:]).replace('"', '""')
            csv_lines.append(f'{i},"{subject}","{content}"')
        
        output_file = self.output_dir / 'convertkit_import.csv'
        with open(output_file, 'w') as f:
            f.write('\n'.join(csv_lines))
        
        return str(output_file)
    
    def package_for_notion(self, emails: List[str], offer: Dict) -> str:
        """Package as Notion markdown page."""
        md_content = f"""# {offer['name']}

{offer['subtitle']}

---

## About This Course

{offer['name']} is a 5-day educational email course.

**Who It's For:** {offer.get('audience', 'People interested in this topic')}

**What You'll Learn:**
"""
        
        for i, mistake in enumerate(offer.get('mistakes', []), 1):
            md_content += f"\n- Day {i}: How to avoid {mistake.lower()}"
        
        md_content += "\n\n---\n\n## The Course\n\n"
        
        for i, email in enumerate(emails):
            day = i if i == 0 else i
            md_content += f"### Day {day}\n\n{email}\n\n---\n\n"
        
        output_file = self.output_dir / 'notion_page.md'
        with open(output_file, 'w') as f:
            f.write(md_content)
        
        return str(output_file)
    
    def package_as_json(self, emails: List[str], offer: Dict) -> str:
        """Package as structured JSON."""
        structured = {
            'offer': offer,
            'emails': []
        }
        
        for i, email in enumerate(emails):
            lines = email.split('\n')
            subject = lines[0].replace('Subject: ', '').strip()
            content = '\n'.join(lines[2:])
            
            structured['emails'].append({
                'day': i,
                'subject': subject,
                'content': content
            })
        
        output_file = self.output_dir / 'eec_structured.json'
        with open(output_file, 'w') as f:
            json.dump(structured, f, indent=2)
        
        return str(output_file)
    
    def create_landing_page(self, offer: Dict) -> str:
        """Create opt-in landing page HTML."""
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{offer['name']}</title>
    <style>
        body {{ font-family: -apple-system, sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; }}
        h1 {{ font-size: 32px; margin-bottom: 10px; }}
        .subtitle {{ font-size: 18px; color: #666; margin-bottom: 30px; }}
        .mistakes {{ margin: 30px 0; }}
        .mistake {{ margin: 10px 0; padding-left: 20px; }}
        .cta {{ background: #000; color: #fff; padding: 15px 30px; border: none; font-size: 18px; cursor: pointer; }}
    </style>
</head>
<body>
    <h1>{offer['name']}</h1>
    <p class="subtitle">{offer['subtitle']}</p>
    
    <div class="mistakes">
        <h2>Here's what you'll learn:</h2>
"""
        
        for i, mistake in enumerate(offer.get('mistakes', []), 1):
            html += f'        <div class="mistake">Day {i}: How to avoid {mistake.lower()}</div>\n'
        
        html += """    </div>
    
    <form action="/subscribe" method="post">
        <input type="email" name="email" placeholder="Enter your email" required style="padding: 15px; font-size: 16px; width: 100%; margin-bottom: 10px;">
        <button type="submit" class="cta">Get The Free Course</button>
    </form>
</body>
</html>"""
        
        output_file = self.output_dir / 'landing_page.html'
        with open(output_file, 'w') as f:
            f.write(html)
        
        return str(output_file)


def main():
    parser = argparse.ArgumentParser(description='Package PGA EEC for deployment')
    parser.add_argument('--emails', required=True, help='Directory with email files')
    parser.add_argument('--offer', required=True, help='Offer JSON file')
    parser.add_argument('--format', choices=['convertkit', 'notion', 'json', 'all'], 
                       default='all', help='Output format')
    parser.add_argument('--output', required=True, help='Output directory')
    parser.add_argument('--landing-page', action='store_true', help='Generate landing page')
    
    args = parser.parse_args()
    
    # Load emails
    email_dir = Path(args.emails)
    emails = []
    for email_file in sorted(email_dir.glob('*.txt')):
        with open(email_file, 'r') as f:
            emails.append(f.read())
    
    # Load offer
    with open(args.offer, 'r') as f:
        offer = json.load(f)
    
    # Create packager
    packager = EECPackager(Path(args.output))
    
    # Package in requested format(s)
    created_files = []
    
    if args.format in ['convertkit', 'all']:
        file = packager.package_for_convertkit(emails, offer)
        created_files.append(file)
        print(f"✅ ConvertKit import: {file}")
    
    if args.format in ['notion', 'all']:
        file = packager.package_for_notion(emails, offer)
        created_files.append(file)
        print(f"✅ Notion page: {file}")
    
    if args.format in ['json', 'all']:
        file = packager.package_as_json(emails, offer)
        created_files.append(file)
        print(f"✅ Structured JSON: {file}")
    
    if args.landing_page:
        file = packager.create_landing_page(offer)
        created_files.append(file)
        print(f"✅ Landing page: {file}")
    
    print(f"\n✅ Packaged {len(emails)} emails into {len(created_files)} files")


if __name__ == '__main__':
    main()
