#!/usr/bin/env python3
"""
Generate EEC offers using the 6-step PGA framework.

Usage:
    python generate_offer.py --topic "Twitter growth" --audience "B2B SaaS founders" --outcome "Generate inbound leads"
"""

import json
import argparse
from typing import Dict, List, Optional


class OfferGenerator:
    """Generates high-converting EEC offers using the PGA 6-step framework."""
    
    GOLDEN_WORDS = [
        "Roadmap", "Blueprint", "System", "Guide", "Playbook", "Toolkit",
        "Checklist", "Accelerator", "Plan", "Map", "Framework", "Crash Course",
        "Kickstart Guide", "Field Guide", "Mini-Course"
    ]
    
    def __init__(self, topic: str, audience: str, outcome: str):
        self.topic = topic
        self.audience = audience
        self.outcome = outcome
        self.mistakes = []
        self.outcomes = []
        
    def step1_base_template(self) -> str:
        """Step 1: Create base template."""
        return f"Biggest Mistakes People Make {self.topic}"
    
    def step2_specify_who(self) -> str:
        """Step 2: Specify the WHO."""
        return f"Biggest Mistakes {self.audience} Make {self.topic}"
    
    def add_mistakes(self, mistakes: List[str]) -> None:
        """Step 3: Add the 5 mistakes."""
        if len(mistakes) != 5:
            raise ValueError("Must provide exactly 5 mistakes")
        self.mistakes = mistakes
    
    def map_outcomes(self, outcomes: List[Dict[str, str]]) -> None:
        """Step 4: Map mistakes to negative outcomes."""
        if len(outcomes) != 5:
            raise ValueError("Must provide exactly 5 outcomes mapped to mistakes")
        self.outcomes = outcomes
    
    def select_top_3_outcomes(self, indices: List[int]) -> List[str]:
        """Step 4B: Select 3 most painful outcomes."""
        if len(indices) != 3:
            raise ValueError("Must select exactly 3 outcome indices")
        return [self.outcomes[i]['outcome'] for i in indices]
    
    def step4c_bake_outcomes(self, top_3: List[str]) -> str:
        """Step 4C: Bake outcomes into offer."""
        outcomes_text = f"{top_3[0]}, {top_3[1]}, And {top_3[2]}"
        return f"Biggest Mistakes {self.audience} Make {self.topic} That Lead To {outcomes_text}"
    
    def step5_name_it(self, golden_word: Optional[str] = None) -> str:
        """Step 5: Give it a name with a golden word."""
        if not golden_word:
            golden_word = self.GOLDEN_WORDS[0]  # Default to "Roadmap"
        return f"The {self.audience}'s {golden_word}"
    
    def step6_whisper(self) -> str:
        """Step 6: Add the whisper."""
        return "(And How To Solve Them)"
    
    def remove_duplicates(self, name: str, subtitle: str) -> tuple[str, str]:
        """Bonus: Remove duplicate words between name and subtitle."""
        # Simple implementation - can be enhanced
        name_words = set(name.lower().split())
        subtitle_words = subtitle.lower().split()
        
        # Check for duplicates
        has_duplicates = bool(name_words.intersection(subtitle_words))
        
        if has_duplicates:
            # Return suggestion to reframe
            return name, subtitle + " [NOTE: Contains duplicate words - consider reframing]"
        
        return name, subtitle
    
    def make_tangible(self, outcome: str) -> str:
        """Bonus: Suggest making outcome more tangible."""
        # This is a helper - actual tangibility comes from the input
        intangible_words = ['struggle', 'difficult', 'hard', 'frustrated', 'overwhelmed']
        
        for word in intangible_words:
            if word in outcome.lower():
                return outcome + " [SUGGESTION: Make more tangible with numbers/specifics]"
        
        return outcome
    
    def add_final_whisper(self, objection: str) -> str:
        """Bonus: Add final objection whisper."""
        return f"(Even If {objection})"
    
    def generate_complete_offer(
        self,
        mistakes: List[str],
        outcomes: List[Dict[str, str]],
        top_3_indices: List[int],
        golden_word: Optional[str] = None,
        final_whisper: Optional[str] = None
    ) -> Dict:
        """Generate complete offer using all steps."""
        
        # Validate inputs
        self.add_mistakes(mistakes)
        self.map_outcomes(outcomes)
        
        # Step 1-2
        base = self.step1_base_template()
        specific = self.step2_specify_who()
        
        # Step 3 (mistakes stored)
        
        # Step 4
        top_3 = self.select_top_3_outcomes(top_3_indices)
        subtitle = self.step4c_bake_outcomes(top_3)
        
        # Step 5
        name = self.step5_name_it(golden_word)
        
        # Step 6
        main_whisper = self.step6_whisper()
        
        # Bonus steps
        name, subtitle = self.remove_duplicates(name, subtitle)
        
        # Check tangibility
        tangible_outcomes = [self.make_tangible(o) for o in top_3]
        
        # Build final offer
        final_subtitle = f"{subtitle} {main_whisper}"
        if final_whisper:
            final_subtitle += f" — {self.add_final_whisper(final_whisper)}"
        
        complete_offer = f"{name}: {final_subtitle}"
        
        return {
            'name': name,
            'subtitle': final_subtitle,
            'complete_offer': complete_offer,
            'mistakes': mistakes,
            'all_outcomes': outcomes,
            'top_3_outcomes': top_3,
            'top_3_tangibility_check': tangible_outcomes,
            'steps': {
                'step1_base': base,
                'step2_specific': specific,
                'step3_mistakes': mistakes,
                'step4_outcomes': outcomes,
                'step4b_top3': top_3,
                'step4c_subtitle': subtitle,
                'step5_name': name,
                'step6_whisper': main_whisper
            }
        }


def main():
    parser = argparse.ArgumentParser(description='Generate PGA EEC offers')
    parser.add_argument('--topic', required=True, help='The topic/activity')
    parser.add_argument('--audience', required=True, help='Specific target audience')
    parser.add_argument('--outcome', required=True, help='Desired outcome for readers')
    parser.add_argument('--mistakes', required=True, help='JSON array of 5 mistakes')
    parser.add_argument('--outcomes', required=True, help='JSON array of 5 outcome objects')
    parser.add_argument('--top3', required=True, help='JSON array of 3 indices for top outcomes')
    parser.add_argument('--golden-word', help='Golden word for naming (default: Roadmap)')
    parser.add_argument('--final-whisper', help='Final objection whisper')
    parser.add_argument('--output', help='Output file (JSON)')
    
    args = parser.parse_args()
    
    # Parse JSON inputs
    mistakes = json.loads(args.mistakes)
    outcomes = json.loads(args.outcomes)
    top_3_indices = json.loads(args.top3)
    
    # Generate offer
    generator = OfferGenerator(args.topic, args.audience, args.outcome)
    result = generator.generate_complete_offer(
        mistakes=mistakes,
        outcomes=outcomes,
        top_3_indices=top_3_indices,
        golden_word=args.golden_word,
        final_whisper=args.final_whisper
    )
    
    # Output
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(result, f, indent=2)
        print(f"✅ Offer generated and saved to {args.output}")
    else:
        print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
