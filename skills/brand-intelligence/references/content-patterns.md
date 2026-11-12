# Content Infrastructure Patterns

Reference guide for identifying lead generation infrastructure and educational content.

## Blog Detection Patterns

### Indicators of Blog Presence
- URL paths: `/blog`, `/articles`, `/posts`, `/news`, `/insights`, `/resources`
- Text patterns: "read our blog", "latest articles", "recent posts"
- Date patterns: "Posted on", "Published", timestamps
- Author bylines: "By [Name]", "Written by"
- Category/tag systems
- Archive links: "View all posts", "Older posts"

### False Positives to Avoid
- Single "News" page with company announcements
- Press releases section
- One-off articles on homepage
- Product documentation labeled as "resources"

## Newsletter Signup Patterns

### Clear Indicators
- Forms with email input
- Text: "Subscribe", "Join our newsletter", "Get updates", "Stay informed"
- CTA buttons: "Subscribe", "Sign up", "Join our list"
- Privacy notice near email field
- Frequency mentioned: "Weekly", "Monthly", "Bi-weekly"

### Weak Signals
- Generic "Contact us" forms
- Email mentioned but no subscribe CTA
- Social media follow buttons (not newsletter)

## Lead Magnet Patterns

### Types of Lead Magnets

**1. Downloadable Resources**
- Guides, ebooks, whitepapers, reports
- Templates, checklists, worksheets, toolkits
- Case studies, research papers
- Pattern: "Download [type]", "Get your [type]"

**2. Interactive Tools**
- Calculators, assessments, quizzes
- ROI calculators, cost estimators
- Pattern: "Try our [tool]", "Calculate your [metric]"

**3. Time-Based Content**
- Email courses, challenges, bootcamps
- Webinar recordings, video series
- Pattern: "[Number]-day [content type]", "Free [duration] course"

**4. Consultations/Demos**
- Free consultation, audit, assessment
- Product demo, trial version
- Pattern: "Free [service]", "Book your [session]"

### Extraction Patterns

Match these regex patterns:
- `(?:free|download)\s+(?:our\s+)?([a-z\s]+(?:guide|ebook|template|checklist))`
- `(?:get|download)\s+(?:the|our|your)\s+([a-z\s]+(?:checklist|template))`
- `(?:free|complimentary)\s+([a-z\s]+(?:consultation|audit|assessment))`
- `(\d+[\-\s](?:day|week|step)\s+[a-z\s]+(?:course|challenge|training))`

## Educational Content Gaps

### Missing Content Types to Flag

**Core Educational Infrastructure:**
- Blog/articles (if absent)
- Newsletter (if no email list building)
- Email course/series
- Video tutorials/webinars

**Lead Generation Assets:**
- Case studies/success stories
- Free templates or tools
- Product demos
- Free trials

**Authority Builders:**
- Original research/reports
- Industry benchmarks
- Best practice guides
- Comparison guides

### Gap Identification Logic

Check for presence of these keywords:
- **Email course**: `email\s+course|email\s+series|drip\s+campaign`
- **Video tutorials**: `video|tutorial|webinar|recording`
- **Case studies**: `case\s+stud|success\s+stor|customer\s+stor`
- **Templates**: `template|tool|calculator|generator`
- **Free trial**: `free\s+trial|trial\s+version|try\s+free`
- **Demo**: `demo|demonstration|walkthrough|tour`

## CTA (Call-to-Action) Patterns

### Primary CTAs
**Purchase/Commitment:**
- "Get started", "Start now", "Start today", "Start free"
- "Buy now", "Purchase", "Sign up"
- "Join us", "Join now", "Join today"

**Engagement:**
- "Book a demo", "Schedule a call", "Request demo"
- "Get a quote", "Request pricing", "Talk to sales"
- "Contact us", "Reach out", "Get in touch"

**Low Commitment:**
- "Learn more", "Explore", "Discover"
- "Download", "Get the guide", "View resources"
- "Try it free", "Free trial", "Test drive"
- "Subscribe", "Join our list"

### Extraction Logic

Match these common patterns:
- `\b(get\s+started|start\s+(?:now|today|free))\b`
- `\b(book\s+(?:a\s+)?(?:demo|call|consultation))\b`
- `\b(sign\s+up|join\s+(?:now|today|us))\b`
- `\b(request\s+(?:a\s+)?(?:demo|quote|consultation))\b`
- `\b(try\s+(?:it\s+)?free|free\s+trial)\b`
- `\b(download\s+(?:now|today)?)\b`
- `\b(learn\s+more)\b`

## Friction Level Assessment

### Low Friction Indicators
- "Free" mentioned frequently (>5 times)
- "No credit card required"
- "Instant access", "Get started in seconds"
- Self-service signup/trial
- Automated onboarding
- No sales call required

**Score:** Low friction count > (High friction count × 2) → **"low"**

### Medium Friction Indicators
- Mix of self-service and assisted options
- Free trial available but limited
- Some forms require multiple fields
- Demo available alongside trial
- Sales assistance optional

**Score:** Balanced counts → **"medium"**

### High Friction Indicators
- "Schedule", "Book a call", "Speak with sales"
- "Contact us for pricing"
- Multi-step approval process
- Enterprise-only language
- No self-service options
- Required discovery calls

**Score:** High friction count > (Low friction count × 2) → **"high"**

## Opt-In Mechanisms

### Types of Opt-Ins

1. **Newsletter Signup**
   - Email collection for regular updates
   - Pattern: Newsletter detected from earlier analysis

2. **Lead Magnet Download**
   - Content exchange for email
   - Pattern: Lead magnets detected from earlier analysis

3. **Free Trial**
   - Product access without payment
   - Pattern: `\bfree\s+trial\b|try\s+free|no\s+credit\s+card`

4. **Demo Request**
   - Scheduled product demonstration
   - Pattern: `\bdemo\b|\bdemonstration\b|product\s+tour`

5. **Free Consultation**
   - Expert advice or assessment
   - Pattern: `\bconsultation\b|\bassessment\b|free\s+audit`

6. **Webinar Registration**
   - Educational event signup
   - Pattern: `\bwebinar\b|live\s+training|online\s+event`

### Identification Logic

Check combined text for each pattern. If pattern found, add mechanism to list.

Return sorted by likelihood of conversion:
1. Free trial (highest intent)
2. Demo request
3. Lead magnet download
4. Newsletter signup
5. Webinar registration
6. Free consultation

## Quality Checks

### Red Flags for Invalid Data

**Under-Construction Sites:**
- "Coming soon", "Under construction", "Stay tuned"
- Lorem ipsum text
- Placeholder images
- Minimal content (<300 words total)

**Generic/Template Sites:**
- Repeated generic phrases
- Stock photo heavy
- No unique value proposition
- Template placeholder text

**Insufficient Data:**
- Total word count < 500
- Only homepage available
- No clear offer
- No contact information

### Validation Checklist

Before returning data, verify:
- [ ] At least 500 words of content extracted
- [ ] At least 2 pages successfully scraped
- [ ] Company offer identified (not "Unable to determine")
- [ ] At least 2 CTAs found
- [ ] At least 1 messaging theme identified
- [ ] Voice samples extracted (minimum 2)

If checks fail, set quality_flag appropriately:
- Failed word count or offer → `INSUFFICIENT_DATA`
- Failed voice samples or generic phrases → `GENERIC_VOICE`
- All checks pass → `PASS`
