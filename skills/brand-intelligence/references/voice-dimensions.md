# Voice Analysis Dimensions

Reference guide for analyzing brand voice across 5 dimensions.

## 1. Formality

Measures how formal or casual the language is.

### Casual
**Indicators:**
- Conversational words: hey, hi, cool, awesome, yeah, nope, gonna, wanna
- Frequent exclamation marks
- Emoticons or casual punctuation
- Contractions everywhere
- Very short, punchy sentences

**Example:**
"Hey! We're stoked to help you crush your goals. No BS, just results."

### Approachable
**Indicators:**
- Balanced mix of professional and casual
- Some contractions but not everywhere
- Friendly but not overly casual
- Clear and direct without being stiff

**Example:**
"We help businesses grow with smart automation. It's simple, effective, and actually works."

### Professional
**Indicators:**
- Formal language: facilitate, leverage, pursuant, comprehensive
- Long-form phrases: "we are pleased to", "we are committed to"
- Minimal contractions
- Structured, complete sentences
- Industry-specific terminology

**Example:**
"We facilitate comprehensive solutions that leverage cutting-edge technology to optimize enterprise workflows."

## 2. Complexity

Measures technical depth and vocabulary sophistication.

### Simple
**Indicators:**
- Short words (avg < 5 letters)
- Minimal jargon or technical terms
- Explanations for complex concepts
- Everyday language
- Accessible to non-experts

**Example:**
"We make your work easier. Connect your tools. Save time. Get more done."

### Moderate
**Indicators:**
- Mix of simple and complex words
- Some industry terms but explained
- Balanced sentence structure
- Technical concepts presented clearly

**Example:**
"Our platform connects your CRM and email tools so your team can work faster without switching apps."

### Technical
**Indicators:**
- Industry jargon: API, SDK, automation, infrastructure, scalability
- Technical terms: algorithm, protocol, methodology, architecture
- Long average word length (> 6.5 letters)
- Assumes domain knowledge

**Example:**
"Our API-first infrastructure enables seamless integration with your existing tech stack, providing scalable deployment across distributed environments."

## 3. Energy

Measures enthusiasm and activation level.

### Reserved
**Indicators:**
- Minimal exclamation marks
- Calm, measured tone
- Few action verbs or intensifiers
- Straightforward statements
- Professional restraint

**Example:**
"Our solution provides reliable results for your business needs. Contact us to learn more about our services."

### Balanced
**Indicators:**
- Moderate use of action words
- Occasional exclamations
- Clear but not overly energetic
- Confident without hyperbole

**Example:**
"We help businesses grow with proven systems. Start seeing results in weeks, not months."

### Energetic
**Indicators:**
- Frequent exclamation marks
- Action verbs: launch, transform, revolutionize, skyrocket, supercharge
- Intensifiers: amazing, incredible, extraordinary, outstanding
- High enthusiasm
- Urgency and momentum

**Example:**
"Transform your business NOW! Skyrocket your revenue with our incredible platform! Join thousands of thriving companies today!"

## 4. Point of View (POV)

Measures focus on company vs. customer.

### We-Focused
**Indicators:**
- Heavy use of "we", "our", "us"
- Company-centric messaging
- Focus on what the company does
- Less emphasis on customer benefits

**Example:**
"We built our platform with cutting-edge technology. Our team has years of experience. We offer comprehensive solutions."

### Balanced
**Indicators:**
- Mix of "we" and "you"
- Alternates between company and customer focus
- Benefits mentioned alongside features

**Example:**
"We designed this platform to help you save time. Our automation handles the busy work so you can focus on growth."

### You-Focused
**Indicators:**
- Heavy use of "you", "your"
- Customer-centric messaging
- Focus on customer outcomes
- Benefits over features

**Example:**
"You'll save 10 hours every week. Your team will work faster. You'll see results in your first month."

## 5. Sentence Length

Measures average words per sentence.

### Short
**Indicators:**
- Average < 12 words per sentence
- Punchy, direct statements
- Frequent periods
- Sentence fragments used stylistically

**Example:**
"Save time. Work faster. Get results. It's that simple."

### Medium
**Indicators:**
- Average 12-20 words per sentence
- Standard business writing
- Complete thoughts in single sentences
- Natural flow

**Example:**
"Our platform helps teams work faster by automating repetitive tasks and connecting your essential tools in one place."

### Long
**Indicators:**
- Average > 20 words per sentence
- Complex sentence structures
- Multiple clauses
- Detailed explanations in single sentences

**Example:**
"Our comprehensive platform leverages advanced automation technology to seamlessly integrate your existing tools, enabling your team to work more efficiently while maintaining the high standards that your business requires to succeed in today's competitive marketplace."

## Scoring Guidelines

When analyzing text:

1. **Combine all text** from website pages
2. **Look for patterns** rather than isolated instances
3. **Count indicators** for each dimension
4. **Calculate ratios** relative to total word count
5. **Choose the dominant characteristic**

### Thresholds

Use these approximate thresholds for scoring:

**Formality:**
- Casual ratio > 2.0 per 100 words → Casual
- Professional ratio > 1.5 per 100 words → Professional
- Otherwise → Approachable

**Complexity:**
- Avg word length < 5.0 AND jargon < 1.0 per 100 → Simple
- Avg word length > 6.5 OR jargon > 3.0 per 100 → Technical
- Otherwise → Moderate

**Energy:**
- Energy score < 2.0 per 100 words → Reserved
- Energy score > 8.0 per 100 words → Energetic
- Otherwise → Balanced

**POV:**
- You/We ratio < 0.5 → We-focused
- You/We ratio > 2.0 → You-focused
- Otherwise → Balanced

**Sentence Length:**
- Avg < 12 words → Short
- Avg > 20 words → Long
- Otherwise → Medium
