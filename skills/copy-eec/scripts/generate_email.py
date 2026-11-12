#!/usr/bin/env python3
"""
Generate EEC emails following the 1/3/1 rhythm and 5-section structure.

Usage:
    python generate_email.py --day 1 --mistake "Trying to raise too much money" --config email_config.json
"""

import json
import argparse
from typing import Dict, List, Optional


class EmailGenerator:
    """Generates emails using PGA 1/3/1 rhythm and 5-section structure."""
    
    PROVEN_OPENERS = {
        'declarative': 'Strong declarative statement',
        'question': 'Thought-provoking question',
        'controversial': 'Controversial opinion',
        'moment': 'Moment in time',
        'vulnerable': 'Vulnerable statement',
        'insight': 'Weird, unique insight (MOST COMMON)'
    }
    
    def __init__(self, eec_name: str, day: int, author_name: str = "Claude"):
        self.eec_name = eec_name
        self.day = day
        self.author_name = author_name
    
    def section1_reminder(self, mistake: str, audience: str) -> str:
        """Generate Section 1: The Reminder."""
        return f"""Hey there!

Welcome to Day {self.day} of {self.eec_name}.

Today we're going to talk about Mistake #{self.day}: {mistake}.

Specifically:
- The reason {audience} make this mistake
- Why this mistake leads to [negative outcomes]
- And how to fix it

Let's dive in."""
    
    def section2_mistake(
        self,
        mistake: str,
        opener_type: str,
        opener_text: str,
        explanation_sentences: List[str],
        conclusion: str,
        outcomes: List[Dict[str, str]]
    ) -> str:
        """Generate Section 2: The Mistake using 1/3/1 rhythm."""
        
        # Validate inputs
        if len(explanation_sentences) != 3:
            raise ValueError("Must provide exactly 3 explanation sentences for 1/3/1 rhythm")
        
        if len(outcomes) < 3 or len(outcomes) > 5:
            raise ValueError("Must provide 3-5 negative outcomes")
        
        # Build 1/3/1 prose
        prose = f"{opener_text}\n\n"
        prose += " ".join(explanation_sentences) + "\n\n"
        prose += conclusion
        
        # Build outcome bullets
        bullets = "\n\n"
        for outcome in outcomes:
            bullets += f"- **{outcome['title']}:** {outcome['description']}\n\n"
        
        return f"""### The Mistake: {mistake}

{prose}

This mistake leads to the following negative outcomes (which is why you should avoid it):
{bullets}"""
    
    def section3_reason(
        self,
        opener_text: str,
        explanation_sentences: List[str],
        conclusion: str,
        reasons: List[Dict[str, str]]
    ) -> str:
        """Generate Section 3: The Reason This Happens using 1/3/1 rhythm."""
        
        if len(explanation_sentences) != 3:
            raise ValueError("Must provide exactly 3 explanation sentences")
        
        if len(reasons) < 3 or len(reasons) > 5:
            raise ValueError("Must provide 3-5 reasons")
        
        # Build 1/3/1 prose
        prose = f"{opener_text}\n\n"
        prose += " ".join(explanation_sentences) + "\n\n"
        prose += conclusion
        
        # Build reason bullets
        bullets = "\n\n"
        for reason in reasons:
            bullets += f"- **{reason['title']}:** {reason['description']}\n\n"
        
        return f"""### The Reason This Happens:

{prose}

Here are some even more specific reasons why this mistake happens:
{bullets}"""
    
    def section4_fix(
        self,
        opener_text: str,
        explanation_sentences: List[str],
        conclusion: str,
        action_steps: List[Dict[str, str]],
        mistake: str
    ) -> str:
        """Generate Section 4: How To Fix It using 1/3/1 rhythm."""
        
        if len(explanation_sentences) != 3:
            raise ValueError("Must provide exactly 3 explanation sentences")
        
        if len(action_steps) < 3 or len(action_steps) > 5:
            raise ValueError("Must provide 3-5 action steps")
        
        # Build 1/3/1 prose
        prose = f"{opener_text}\n\n"
        prose += " ".join(explanation_sentences) + "\n\n"
        prose += conclusion
        
        # Build action bullets
        bullets = "\n\n"
        for step in action_steps:
            bullets += f"- **{step['title']}:** {step['description']}\n\n"
        
        return f"""### How To Fix It

{prose}

Instead of {mistake.lower()}, here's what you should do instead:
{bullets}"""
    
    def section5_tomorrow(
        self,
        next_mistake: Optional[str],
        audience: str
    ) -> str:
        """Generate Section 5: Check Your Inbox Tomorrow."""
        
        if self.day == 5:
            # Final email
            return f"""### This Is The Last Email!

We've covered a lot over the past 5 days.

I hope you now have a clear picture of the 5 biggest mistakes {audience} make—and more importantly, how to avoid them.

Now go apply what you learned.

Best,
{self.author_name}"""
        else:
            # Regular preview
            next_day = self.day + 1
            return f"""### Don't Forget To Check Your Inbox Tomorrow!

Phew, we covered a lot today.

I hope this gives you some clarity around why this mistake happens—and some action steps to avoid it in the future.

And stay tuned for tomorrow, because we're going to dig into Mistake #{next_day}: {next_mistake}.

Specifically:
- The reason {audience} make this mistake
- Why this mistake leads to [negative outcomes]
- And how to fix it

Keep an eye on your inbox!

Best,
{self.author_name}"""
    
    def generate_complete_email(self, config: Dict) -> str:
        """Generate complete email from config."""
        
        # Section 1
        section1 = self.section1_reminder(
            config['mistake'],
            config['audience']
        )
        
        # Section 2
        section2 = self.section2_mistake(
            mistake=config['mistake'],
            opener_type=config['section2']['opener_type'],
            opener_text=config['section2']['opener'],
            explanation_sentences=config['section2']['explanation'],
            conclusion=config['section2']['conclusion'],
            outcomes=config['section2']['outcomes']
        )
        
        # Section 3
        section3 = self.section3_reason(
            opener_text=config['section3']['opener'],
            explanation_sentences=config['section3']['explanation'],
            conclusion=config['section3']['conclusion'],
            reasons=config['section3']['reasons']
        )
        
        # Section 4
        section4 = self.section4_fix(
            opener_text=config['section4']['opener'],
            explanation_sentences=config['section4']['explanation'],
            conclusion=config['section4']['conclusion'],
            action_steps=config['section4']['action_steps'],
            mistake=config['mistake']
        )
        
        # Section 5
        section5 = self.section5_tomorrow(
            config.get('next_mistake'),
            config['audience']
        )
        
        # Assemble email
        subject = f"{self.eec_name} - Day {self.day}: Mistake #{self.day}"
        
        email = f"Subject: {subject}\n\n"
        email += section1 + "\n\n---\n\n"
        email += section2 + "\n\n---\n\n"
        email += section3 + "\n\n---\n\n"
        email += section4 + "\n\n---\n\n"
        email += section5
        
        # Add PS if provided
        if config.get('ps_text'):
            email += f"\n\nP.S. — {config['ps_text']}"
        
        return email
    
    def validate_131_rhythm(self, section_config: Dict) -> bool:
        """Validate that a section follows 1/3/1 rhythm."""
        required = ['opener', 'explanation', 'conclusion']
        
        for field in required:
            if field not in section_config:
                return False
        
        if len(section_config['explanation']) != 3:
            return False
        
        return True


def main():
    parser = argparse.ArgumentParser(description='Generate PGA EEC emails')
    parser.add_argument('--day', type=int, required=True, help='Day number (1-5)')
    parser.add_argument('--config', required=True, help='Email config JSON file')
    parser.add_argument('--output', help='Output file for email')
    parser.add_argument('--validate-only', action='store_true', help='Only validate 1/3/1 rhythm')
    
    args = parser.parse_args()
    
    # Load config
    with open(args.config, 'r') as f:
        config = json.load(f)
    
    # Create generator
    generator = EmailGenerator(
        eec_name=config['eec_name'],
        day=args.day,
        author_name=config.get('author_name', 'Claude')
    )
    
    # Validate if requested
    if args.validate_only:
        valid = True
        for section_num in [2, 3, 4]:
            section_key = f'section{section_num}'
            if not generator.validate_131_rhythm(config[section_key]):
                print(f"❌ Section {section_num} does not follow 1/3/1 rhythm")
                valid = False
        
        if valid:
            print("✅ All sections follow 1/3/1 rhythm")
        return
    
    # Generate email
    email = generator.generate_complete_email(config)
    
    # Output
    if args.output:
        with open(args.output, 'w') as f:
            f.write(email)
        print(f"✅ Email generated and saved to {args.output}")
    else:
        print(email)


if __name__ == '__main__':
    main()
