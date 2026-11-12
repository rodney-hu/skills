# Industry Classification Signals

Reference guide for inferring industry from website content.

## Primary Industries

### B2B SaaS
**Keywords:**
- Software, platform, SaaS, API, SDK
- Automation, workflow, integration
- Dashboard, analytics, reporting
- Subscription, monthly, annual
- Cloud-based, web-based

**Typical Offers:**
- "Platform for [business function]"
- "Automate your [process]"
- "Connect your tools"
- "All-in-one solution for [role]"

**Authority Signals:**
- API documentation
- Integration marketplace
- Uptime guarantees
- SOC 2 compliance
- Pricing tiers (Starter, Pro, Enterprise)

**Differentiators:**
- Integration count
- API-first architecture
- Workflow automation
- Real-time sync
- Custom fields/flexibility

### Marketing/Sales
**Keywords:**
- Marketing, sales, CRM, lead generation
- Outreach, email marketing, campaigns
- Conversion, funnel, nurture
- Prospects, leads, pipeline
- Attribution, analytics, ROI

**Typical Offers:**
- "Generate more leads"
- "Close more deals"
- "Automate your outreach"
- "Grow your pipeline"

**Authority Signals:**
- Case studies with metrics (% increase)
- Integration with HubSpot, Salesforce
- Deliverability rates
- Response rates

**Differentiators:**
- Deliverability claims
- AI personalization
- Multi-channel campaigns
- Warm-up technology

### E-commerce
**Keywords:**
- E-commerce, online store, retail
- Products, inventory, catalog
- Shopping cart, checkout, payments
- Shopify, WooCommerce, BigCommerce
- Fulfillment, shipping

**Typical Offers:**
- "Sell online"
- "Build your store"
- "Manage inventory"
- "Accept payments"

**Authority Signals:**
- Payment gateway logos
- Platform integrations
- Transaction volume
- Store count

**Differentiators:**
- Checkout experience
- Mobile optimization
- International support
- Abandoned cart recovery

### Healthcare
**Keywords:**
- Health, medical, patient, clinic
- Therapy, treatment, wellness
- Diagnosis, symptoms, care
- Healthcare, telehealth, virtual
- Provider, physician, doctor

**Typical Offers:**
- "Better patient outcomes"
- "Streamline practice management"
- "Telehealth platform"
- "Mental health support"

**Authority Signals:**
- HIPAA compliance
- Medical certifications
- Clinical studies
- Provider credentials

**Differentiators:**
- Privacy/security focus
- Specialty focus (mental health, chronic care)
- Integration with EHR systems
- Evidence-based approaches

### Fintech
**Keywords:**
- Fintech, financial, payments, banking
- Crypto, blockchain, wallet
- Lending, credit, investing
- Transaction, money, funds
- Compliance, regulation

**Typical Offers:**
- "Faster payments"
- "Modern banking"
- "Investment platform"
- "Financial automation"

**Authority Signals:**
- Regulatory licenses
- Security certifications (PCI DSS)
- Banking partnerships
- Transaction volume

**Differentiators:**
- Low fees
- Speed of transactions
- Security features
- Regulatory compliance

### Education
**Keywords:**
- Education, learning, training, course
- Student, teacher, school, classroom
- Curriculum, lesson, assessment
- E-learning, online learning, LMS
- Skill, certification, degree

**Typical Offers:**
- "Learn [skill]"
- "Online courses for [audience]"
- "Training platform"
- "Skill development"

**Authority Signals:**
- Completion rates
- Accreditation
- Instructor credentials
- Student outcomes

**Differentiators:**
- Learning methodology
- Certification value
- Instructor quality
- Hands-on projects

### Agency/Services
**Keywords:**
- Agency, consulting, services
- Strategy, design, creative
- Marketing agency, design agency
- Custom, bespoke, tailored
- Projects, clients, portfolio

**Typical Offers:**
- "We help [industry] with [service]"
- "Custom solutions"
- "Full-service [type] agency"
- "Strategic [service]"

**Authority Signals:**
- Client logos
- Portfolio/case studies
- Years in business
- Team credentials

**Differentiators:**
- Industry specialization
- Service approach
- Team expertise
- Results focus

### Beauty/Wellness
**Keywords:**
- Beauty, spa, salon, medspa
- Esthetician, skin care, facial
- Wellness, body, treatment
- Botox, filler, laser
- Massage, therapy, relaxation

**Typical Offers:**
- "Aesthetic treatments"
- "Beauty services"
- "Skin rejuvenation"
- "Wellness programs"

**Authority Signals:**
- Before/after photos
- Provider certifications
- Safety certifications
- Treatment protocols

**Differentiators:**
- Treatment technology
- Provider expertise
- Personalized approach
- Results guarantees

## Classification Algorithm

### Step 1: Keyword Matching
For each industry, count occurrences of keywords in combined website text.

```python
scores = {}
for industry, keywords in industries.items():
    score = sum(text.count(keyword) for keyword in keywords)
    scores[industry] = score
```

### Step 2: Weight by Specificity
Some keywords are more specific than others:
- High specificity (×3): API, SDK, HIPAA, fintech, medspa, esthetician
- Medium specificity (×2): SaaS, CRM, e-commerce, telehealth, blockchain
- Low specificity (×1): software, marketing, health, design, business

### Step 3: Context Validation
Check if offer aligns with industry classification:
- B2B SaaS: Offer mentions "platform", "automation", "integration"
- Healthcare: Offer mentions "patient", "care", "treatment"
- Fintech: Offer mentions "payment", "financial", "banking"

### Step 4: Fallback
If no clear industry match (all scores < 3):
- Check if B2B (mentions "business", "enterprise", "companies") → "B2B SaaS"
- Check if B2C (mentions "customers", "users", "people") → "General Business"
- Default → "General Business"

## Sub-Industry Classification

After primary industry is determined, identify sub-segments:

### B2B SaaS Sub-Segments
- **Sales tools**: CRM, outreach, prospecting mentioned
- **Marketing tools**: Campaigns, content, SEO mentioned
- **Operations tools**: Workflow, project management, collaboration mentioned
- **Analytics tools**: Data, reporting, insights mentioned
- **Automation tools**: Zapier-like, workflow, integration mentioned

### Healthcare Sub-Segments
- **Mental health**: Therapy, counseling, psychiatry mentioned
- **Telehealth**: Virtual, remote, online mentioned
- **Practice management**: EHR, scheduling, billing mentioned
- **Specialty care**: Specific condition or treatment focus

### E-commerce Sub-Segments
- **Platform**: Building/hosting stores mentioned
- **Fulfillment**: Shipping, logistics, warehouse mentioned
- **Marketing**: Abandoned cart, email, retention mentioned
- **Payments**: Checkout, gateway, processing mentioned

## Target Customer Inference

Based on industry and language patterns, infer target customer:

### B2B Indicators
- Plural business terms: "companies", "businesses", "teams", "organizations"
- Role-specific: "founders", "CEOs", "managers", "directors"
- B2B processes: "sales teams", "marketing departments"

### B2C Indicators
- Singular consumer terms: "you", "people", "customers", "users"
- Personal benefits: "your life", "your health", "your goals"
- Direct consumer services

### SMB vs. Enterprise
- **SMB indicators**: "small business", "startups", "solopreneurs", price <$100/mo
- **Enterprise indicators**: "enterprise", "large organizations", "security", custom pricing

## Edge Cases

### Ambiguous Industries
If multiple industries score similarly:
1. Check URL patterns (healthcare.com, fintech.io)
2. Review meta descriptions/titles
3. Look for regulatory mentions (HIPAA → Healthcare, PCI → Fintech)
4. Default to broader category (B2B SaaS if unclear)

### Multi-Industry Companies
If company serves multiple industries:
- Use primary industry based on highest score
- Note in positioning: "Multi-industry platform"
- Target customer should reflect breadth: "Businesses across industries"

### New/Undefined Industries
If no industry matches well:
- Use "General Business"
- Or create compound: "B2B SaaS - [Specialty]"
- Example: "B2B SaaS - Sales Automation"
