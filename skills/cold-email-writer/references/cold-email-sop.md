# **Programmatic Cold Email Outbound: Standard Operating Procedure (SOP)**

**Document Version:** 2.0.0

**Target Audience:** Human Marketing Operators, GTM Engineers, and Autonomous AI Writing/Lead-Gen Agents

**Purpose:** To serve as the definitive "source of truth" for technical setup, list preparation, signal-led copywriting, campaign execution, and performance monitoring.

## **Module 1: Technical Infrastructure Setup & Deliverability Auditing**

This module governs the setup of all outbound domains and mailboxes. AI agents or system engineers must verify these exact standards before any message is cleared for transmission.

### **1.1 DNS Authentication Protocol**

All outbound sending domains must completely isolate traffic from the primary corporate domain. Every secondary domain must configure the following three TXT records and one CNAME record:

1. **Sender Policy Framework (SPF):** Defines authorized sending servers.  
   * **Rule:** Maximize lookup safety. Never publish multiple SPF records on a single domain. Ensure the record conforms to the RFC 7208 limit of 10 or fewer DNS lookups.  
   * **Google Workspace Value:** v=spf1 include:\_spf.google.com \~all  
   * **Microsoft 365 Value:** v=spf1 include:spf.protection.outlook.com \~all  
2. **DomainKeys Identified Mail (DKIM):** Cryptographic verification signature.  
   * **Rule:** Generate a secure 2048-bit key in the mail admin console. Publish at the host name specified by the provider (e.g., google.\_domainkey).  
3. **Domain-Based Message Authentication, Reporting, and Conformance (DMARC):**  
   * **Rule:** Initialize at p=none to collect aggregate reports (rua). Transition to enforcement after validation.  
   * **Phase 1 (Monitoring):** v=DMARC1; p=none; rua=mailto:dmarc@yourdomain.com  
   * **Phase 2 (Enforced):** v=DMARC1; p=quarantine; pct=100; aspf=s; adkim=s  
4. **Custom Tracking Domain (CNAME):** Overrides shared platform pixels to prevent shared-reputation contamination.  
   * **Rule:** Create a unique subdomain (e.g., track.yourdomain.com) pointing to the outbound tool’s tracking endpoint.

### **1.2 Mailbox and Domain Capacity Algorithm**

To maintain safe sending profiles, domain acquisition and mailbox configuration must scale according to the following mathematical constraints:

* **Maximum Mailboxes per Domain:** 2 to 3 individual accounts.  
* **Format Requirement:** Person-first names only (e.g., first.last@domain.com). Avoid role-based aliases like sales@, info@, or hello@.  
* **Daily Volumetric Equation:**  
  To compute the exact number of secondary domains (![][image1]) required to meet a targeted daily send volume (![][image2]):![][image3]  
  Where:  
  * ![][image1] is the total number of secondary domains to acquire.  
  * ![][image2] is the target daily send volume.  
  * ![][image4] is the number of active mailboxes configured per secondary domain (![][image5]).  
  * ![][image6] is the strict maximum daily sending volume limit per individual mailbox (![][image7]).

### **1.3 Warmup & Throttling Protocol**

Every new mailbox must undergo a rigorous warmup cycle to build sender reputation before running cold campaigns:

* **Warmup Phase Duration:** 21 to 30 days (minimum 4 to 6 weeks when targeting high-security enterprise networks).  
* **Warmup Automation Rules:** Enable peer-to-peer sending simulation, auto-reply, and automatic "unspam" actions using a closed warmup network.  
* **Volume Scalability Limit:** When starting live campaigns, daily sending volume increases must not exceed a maximum weekly growth rate of ![][image8] to ![][image9].

## **Module 2: Ideal Customer Profile (ICP) Validation & Lead Signal-Scoring**

Campaigns must target dynamic intent events rather than static corporate directories. This section outlines how AI agents and researchers build and validate outbound databases.

### **2.1 Quantitative ICP Validation Framework**

Before establishing cold email targets, service offerings must be validated via unstructured customer/market discovery interviews (![][image10]).

* **Demand Threshold Rule:** At least 8 out of 15 interviewed profile targets must report the exact same operational pain point.  
* **Unit Economic Alignment Rule:** The target Annual Contract Value (ACV) dictates the required channel unit economics.![][image11]![][image12]  
  Where:  
  * ![][image13] is Customer Lifetime Value.  
  * ![][image14] is Customer Acquisition Cost.  
  * ![][image15] is the payback period for acquiring a customer.  
  * High ACV (![][image16]) requires highly personalized enterprise campaigns (e.g., Level 3 high-effort custom audits).

### **2.2 Intent-Signal Scoring Matrix**

Lead lists must be segmented dynamically by ranking opportunities based on real-time business changes:

| Intent Signal | Context / Operational Pain Point | Target Role Alignment | Outreach Priority |
| :---- | :---- | :---- | :---- |
| **Active Relevant Hiring** | Indicates active budget allocation to solve a specific bottleneck. | VP / Director / Head of Department | Priority 1 (High Intent) |
| **Executive Transition** | New leaders auditing software/services stack within first 90 days. | Incoming Executive | Priority 1 (High Intent) |
| **Tech Stack Change** | Installation or churn of relevant competitor tools. | Engineering / IT / Marketing Ops | Priority 2 (Medium Intent) |
| **Funding Announcement** | Pressure to scale operations quickly with newly unlocked budget. | Founder / C-Suite / Head of Growth | Priority 2 (Medium Intent) |

## **Module 3: Copywriting Architectures & Linguistic Engineering**

This module governs the structural logic and formatting constraints for all written output. AI agents must generate copy that adheres to these specifications without exception.

### **3.1 Strict Structural Rules**

* **Word Count:** Target 25 to 50 words for initial touchpoints. The absolute limit is 100 words.  
* **Mobile-First Formatting:** Use a single-sentence-paragraph format. Insert a complete line break after every single sentence to ensure high skimmability on mobile displays without vertical scrolling.  
* **Readability Grading:** Sentences must be written at a 3rd- to 5th-grade reading level. Use basic vocabulary and an active voice.  
* **Subject Lines:** 1 to 3 words. Lowercase or natural sentence-case only. Keep under 50 characters (or under 8 words). Must mimic internal, low-key operational communications (e.g., "team priority" or "quick thought"). Emojis, exclamation marks, and sales cliches are strictly banned.  
* **Preview Text Optimization:** Banish polite filler (e.g., *"I hope this email finds you well"*). Open directly with personalization and signals to ensure high open rates.  
* **Disable Open Tracking Pixels:** Disabling tracking pixels eliminates the secure gateway security checks that flag hidden images. Rely on click tracking via custom subdomains or simple direct reply rates.

### **3.2 The "Anti-AI Slop" Filter**

Autonomous copy-generation agents must run all drafts through a structural filter to remove robotic markers.

#### **Filter List:**

1. **Banned Connectors:** *additionally, moreover, furthermore, however, therefore, in addition, consequently, indeed.*  
2. **Banned Jargon / Buzzwords:** *streamline, leverage, optimize, utilize, synergize, crucial, landscape, next-gen, paradigm shift, revolutionary.*  
3. **Formatting Restrictions:** No em-dashes (—), no bolded inline phrases, no exclamation points, and no marketing adjectives (e.g., *groundbreaking*).  
4. **Sentence Variance:** Balance short and punchy declarations with slightly longer compound sentences. Target ![][image8] to ![][image9] of sentences to be under 10 words.  
5. **Tone Profile:** Peer-to-peer alignment. Write as a professional colleague. Avoid subservient greetings (*"Thank you for your valuable time"*) or insincere compliments (*"Congratulations on your impressive growth"*). Use conversational contractions naturally (*don't, we'll, it's, can't*).

## **Module 4: Scripting and Conversational Framework Library**

AI agents must select the appropriate copywriting framework from the library below based on the prospect segment and the campaign's structural objective.

### **4.1 Classical Copywriting Frameworks**

* **Problem-Agitate-Solve (PAS):** Define the problem, agitate the consequences of ignoring it, and present your solution as the logical path.  
* **Before-After-Bridge (BAB):** Show their current state, project a better future state, and present your product/service as the bridge.  
* **Star-Arch-Success (SAS):** Introduce a peer customer (Star), map their core challenge (Arch), and outline the metrics of their resolution (Success).

### **4.2 Lavender's 4-Stage Model**

This is the default structural framework for outbound generation:

\[STAGE 1: OBSERVATION\]   
Reference a specific, verifiable hiring/intent signal (1-2 sentences).  
  ↓  
\[STAGE 2: CONNECTION\]   
Connect that observation to a hypothesis about an operational problem they face.  
  ↓  
\[STAGE 3: CREDIBILITY\]   
Validate how you solve this problem with social proof or a quantitative metric.  
  ↓  
\[STAGE 4: CALL TO CONVERSATION (CTC)\]   
Ask a low-friction, interest-based question.

### **4.3 Specialized Campaign Playbooks**

#### **Playbook A: The Vanilla Ice Cream Playbook**

*Designed to present core business value with minimal friction.*

* **Context:** State the direct context for reaching out in one sentence.  
* **Clarification (Part 1):** Seek to clarify "what we do" in plain, simple terms.  
* **Clarification (Part 2):** Explicitly explain "why that is relevant" to their current role.  
* **Closing:** End with a low-friction Call to Conversation (CTC).

#### **Playbook B: The Referral Playbook**

*Used to navigate larger organizations and locate the correct stakeholder.*

* **Introductions:** Mention a relevant department or shared connection early.  
* **Verification:** Ask if they are the correct person to handle this specific business function.  
* **Context:** Explain why they might be the best person, linking back to your research.  
* **Relevance:** Conclude by explaining the original reason for reaching out.

#### **Playbook C: The Competitor Playbook**

*Targeting active accounts of a direct, known competitor.*

* **Acknowledge:** Name their current vendor directly and professionally.  
* **Compliment:** Acknowledge that the competitor is a strong option.  
* **Shortcomings:** Gently highlight a known, specific technical limitation of that vendor.  
* **Dialogue:** Open a conversation with an interest-based question on how they handle that limitation.

#### **Playbook D: The Feedback / Beta Playbook**

*Low-friction go-to-market validation framework.*

* **Introduction:** Frame the outreach around a specific industry problem.  
* **Objective:** State clearly that you are looking for feedback, not trying to sell.  
* **Context:** Briefly explain what your company does and share your professional background.  
* **Request:** Ask if they are open to a brief conversation to share their perspective on the solution.

#### **Playbook E: The Permission-Based Async Video (Service Businesses)**

*To scale high-impact video outreach without wasting resources.*

* **Step 1 (Permission Request Email):** Identify a specific operational bug (e.g., slow mobile load speed, broken signup page, or security gap). Request permission to send a 90-second video explaining the fix.  
* **Step 2 (The Async Video):** Upon reply, record a Loom under 2 minutes. Walk through the issue live on screen and present the fix. Close by offering a simple chat to discuss next steps.

## **Module 5: Campaign Sequences & Behavioral Routing Rules**

Every outbound campaign must follow a multi-touch cadence with distinct thematic angles. Senders must not simply repeat their original pitch.

### **5.1 Default Multi-Touch Progression Sequence**

* **Touch 1 (Day 1):** The core problem hook (Lavender’s 4-Stage or PAS).  
* **Touch 2 (Day 4):** Case-study/social-proof push (BAB or SAS frame, pointing back to the first email thread).  
* **Touch 3 (Day 9 \- "Something New"):** Share a high-value, unbranded industry resource, or notify them of a recent market shift relevant to their industry.  
* **Touch 4 (Day 15):** The "Permission-Value" offer (e.g., Level 2 or Level 3 value offer).  
* **Touch 5 (Day 22 \- "Timing is Off" / Polite Breakup):** Acknowledge that timing might be wrong, outline the core problem one last time, and ask them to keep the door open if priorities change.

### **5.2 Behavioral Automation Rules**

Outbound systems must apply the following conditional logic to active contacts:

                        \[Prospect Opens Email or Clicks Link\]  
                                         │  
                   ┌─────────────────────┴─────────────────────┐  
                   ▼                                           ▼  
      \[Within First 3 Steps\]                         \[Step 4 or Later\]  
                   │                                           │  
                   ▼                                           ▼  
      Delay next touchpoint by                      Flag as "Highly Active"  
      48 hours; dynamically swap                   and route to a priority  
      Touchpoint \+ 1 for an offer-               manual review task queue.  
      focused case study.

## **Module 6: Quality Assurance, Testing, and Optimization Metrics**

### **6.1 Strict Quality Control Limits**

Technical systems must monitor deliverability in real-time. If performance falls below these thresholds, stop the campaigns immediately to protect your sender reputation:

* **Hard Bounce Rate (![][image17]):** Must be strictly less than ![][image18].![][image19]  
* **Spam Complaint Rate (![][image20]):** Must be strictly less than ![][image21].![][image22]  
* **Reply Rate Goal:** Target a positive response rate greater than ![][image23].

### **6.2 A/B Testing Protocols**

To continuously optimize campaigns, teams must run structured experiments that adhere to these rules:

1. **Sample Size Constraint:** A minimum of 200 unique contacts per variant must complete the entire sequence before evaluating performance.  
2. **Single-Variable Rule:** Test only one element at a time (e.g., test the subject line *or* the framework structure, never both in the same experiment).  
3. **Data-Driven Scalability:** Only scale campaigns that hit positive reply rate benchmarks during the testing phase.

## **Appendix: Copywriting Prompt Template for AI Agents**

When utilizing autonomous LLMs to write cold email drafts, agents must be initialized with the following system instructions:

You are an expert sales copywriter and GTM consultant specializing in hyper-personalized, mobile-first cold email outbound. 

Your objective is to generate clear, conversational, high-converting cold email drafts using Lavender's 4-Stage Model.

CRITICAL INSTRUCTIONS FOR VOICING AND STYLE:  
1\. Write at a 3rd- to 5th-grade reading level. Use short, simple sentences.  
2\. Word count must be strictly between 25 and 50 words.  
3\. Every single sentence must be followed by a line break. No paragraphs may contain more than one sentence.  
4\. Banned words: moreover, additionally, furthermore, however, utilize, leverage, optimize, streamline, landscape, crucial.  
5\. Do not write formal introductions ("I hope this email finds you well"). Start directly with your observation.  
6\. Use natural contractions (don't, it's, we'll). Write as if you are sending a quick message to a colleague.  
7\. Use the prospect's first name in the greeting. Keep sign-offs simple (e.g., "Thanks," or "Best,").

OUTPUT STRUCTURE:  
Subject: \[1 to 3 words, lowercase\]

Hi \[Name\],

\[Observation based on input signal\]

\[Hypothesized pain point or business challenge connected to the observation\]

\[Low-friction social proof or metric\]

\[Low-friction interest-based call to conversation\]

Thanks,  
\[Sender Name\]  


[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAAZCAYAAAA8CX6UAAAAzElEQVR4Xu2RPQrCQBCFcwDbWGU3P+sV7LWxt/M4gp2H8QxiIxa2isTSOmAlKURnYWYhT9aNncV+MATe+yYMSZJEfiLP8zXNnebF86BpIDvjnhdZwtxCeevrPrBiURQ7zC1pmg64X2LXgYQFXzTFTvh2sYOEU0jq+6Kg1McRaYu5UJbljB3/35PvQ88JdgL1tXWMMUPsHCRcQifzNU/MO7DUYi5wf8O8Q5ZlIxZX2FVVpbnbYOegcq61PrBo50qz5zly1iilxrgbifwtbzDMT22SneQ7AAAAAElFTkSuQmCC>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAAaCAYAAAC6nQw6AAABAklEQVR4Xu2TPQrCQBSEExAEKy1sAsmGmBt4AS29heAxFAQvYekZbLSxsPAMXkCwE38aQYg6Cy9hMzE/loIfPNjMTN7uPhLL+lMFWyl1Qb2MOnEIWmT4EfsJnuctdMj3/R57MdpnLQMaDGW3MXsa+Ets1mU9g+u6HWm0Ys9xnAb0I+u5SKPrB/3BWiHSKDUHPI9QE1MrJadR+YAZboT1PgzDtpnRQKuzlgIv3uNGMvwdZzSlp0Rgo0NBEHh5YXwCLXhP1lMgNJXrHVAD9sVLiv0EmH0JndmLgRfpU7HO1GQnm42YwpNUBb9JU5XNpwpoMsO15rJes/8N+uo31JaNP7/IGwh/TvnHQM4NAAAAAElFTkSuQmCC>

[image3]: <data:image/png;base64,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>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAaCAYAAACkVDyJAAABq0lEQVR4Xu2VMUsDQRCFtVFB23BFTC6BVKfYWNsqqIWNrZWIjaikEhT9Af4BSyEgKFjZWykBSWUpCiEqCAqiEQSF+A3ZPTbjXchBCpE8eOzuvHczc3NL0tfXw79CNpvd9X2/DhuGFe1xgV51vPJcUXs6gpOkoTWLfD4/gb4jHhqd1HoikOTedBxbEK0GL9t5OgIJZuEyPItLRvzUrG2n0BFIUDZrMSpZKpUaYYRrxiMFT7QnEWwR+S6yT6fTo0r/lDWXy82Iji9w9cQgyYOzl4RL9sx+3fO8YaOVoyaQCNI1SVfsWRISO3TO4fjMOGMLcos99Aqsay2EdK3OkrRm9o9ao5ljN6aB5whu63gI3bF9i0wmMwXHnficxJnGmOvXEE+hUBjU8RAYntT52RS9UXEZVeQ4eesDtBK8jvMI+hFvYdUN+s2R/HrINBEVv6Lghuz5htO+udEtILgPX+ELfIffVmNk83DR8X443jf4RYEtI0vTYRPsS2h79tx1kHxBFZRLNeR6uoogCAYocid7+TWyxSm62ersIihyDi8osuo3L03bv7ceevib+AFdkIybTA6tFwAAAABJRU5ErkJggg==>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEIAAAAaCAYAAAADiYpyAAAC4ElEQVR4Xu2XXYiMURjHV1soXyXT1Hy95qOmhtjaxI0LN+Sr3LjkhpAS2itaceFu3SnFndpSFBG544o2WqlVLkRty7ZCyc5GMdbvMedMx/N+zMzOtJT3X//ec57//zzveZ457/vu9vTEiBEjRovI5XJnPc+rwlnDUe1xgT7ueGXdgPb8TbCfi2ZvNTik9aZwipvVmkU+n1+HfkY8NLBf692GvVc2m92gtSDg/boaOPPIegLBgreeORlas0CbgI+jPN0A+a/AGjX1aS0MlUploSl82sYY35IYeQ673lBg3gEPwrthRRK/aa5ys0BPpyDvPVjNZDJprbUCU/QTZ35fYpze3a4vFJhHzHUgqMhEIrGUZMeMRxpxQ3s6QC/5nsPJcrm8TIudoO0fzZrluZdxOp3OKP2bXOn2NtPhiqvPBdJccr2DY0x7td4p2Osd2WuhUFihtVDIhpyxFLrfzhkfTyaTS4w20laHI2ByTZVKpeVa6wQ0YJNX/3K8hM/k3aE9gZBfmWIP2bkUSuyqM288BqJFNYKvShJ9FFa1FgbudRv/jD6F3QB5H8h+U6nUKq35IL+MmkuxE2Y8qTU2ft2NaeC5Bgd1vBlYcwnWaOZ6rc0V9lEXas0HbbIL+XZvhmud+E6Jk3yN69cQD8d9kY63CtafNnvYrrUo4D8q6/QLt51GvFfzj2bxKxWXIx+YkFNyGW0YjoV52oW8pyQX131aC4ItmL2cszE+wyUbd6w+LMDwGo67Qa9+tH0LwxISe8rNT8iYY73VM1+YboF8W+ABHdeQlzq+KTfG/IXsmX15brwBxAvwM/wEp+EPq5FwF9zreGcc7xf4ncJPGVma2WgO42H3F5lvcP/zsh/4wVx/FovFrPZ1HRS9RzVCjuZi1/NfwPx9/0bG5g+k302hGSf/dPrh1Y+8vICbkmd9pV7/z4GNPoSPKP6IV39ZRv4bb4G/D25shfpLECNGjBgxYsw/fgFk0vYk1yqsdAAAAABJRU5ErkJggg==>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAABZElEQVR4Xu2VrUsFQRTFlwdaFNuyZb9ZDBssmwQxiMWgxWJWmyIGLeJ/IHbFIgg2TQaNgtVgNYjBIgYFEUTQ5+/qDo6XZ9ldsOyBw8w99849M8My6zgtmkaapsNxHO+GYThttCiK1uyaWiiKoo+GH3Avy7KhJEnGmXfhJnzW9ZUhTTnFWC8dbmi9EjDYl4ZaF4gup9V6JZS7/tNIa5VhjOC2zjUKDLYssy9ynTu6rhHQeEWb8Zlf67pGgemkMdO5yqDZrNYE6AeNGQVBMMP1rGpdgMl6Y0Y0uoTHWhegv9sfBPEVfGPaYbwv4wU4BQ/hq7X8N2THQtd1B5V+FKlnhydpBO0Bnlh1Xc/zBmTOps64nbmfFRYovHO+d/hUmj7KKC+FrhVIzppPwFs7l+d5v4lrwTZiM+fE871ytUCjRbkeK7ZPt0TulHGUsGP0SqDJhe/7mRW/mLn8Vohv4LLRWrT4P3wCKhtotpPIcVoAAAAASUVORK5CYII=>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHoAAAAaCAYAAAB4rUi+AAAEtklEQVR4Xu2YW6gVVRjHj3giKiiL4nBue/a5FFhQ0YkSiaB8CPKhSIouBKIPCZV0NYx6CKWXjC6kCEWU+JAVFCTR5SFKiggCFS3qLVCCssij6Vbz1O87+5t9lv89s/fsy1HirB98zKz/961v1lozs9aa6emJRCKRSOTMMT4+fkmSJJvK5fI9FHtNo7xUwuY2IyMjVzEof2D/Yt8yWAs0xsD3LDaJHcFWqr8LzFOhCLTl71Kp9CXH/uHh4Ws5HqP8sPVHY08jhfpCG//C1o2NjQ1T7GXsF1H+XuMM9Pf8Hv0wMDBwrvobQuJVVHw1LXO+1ZNdE8ZZcuzzoLwH+zqMaRduyoXk+p22fKW+Zlhbqf9Ulk6+z1SfbbjuTT5+69WXhceeYrT70TBmYmLiLNNHR0dLLs332P4wriFp8kYa0+L5GmN4ozLf/iIMDQ2Nk6NCjm3qKwL1lme1y0iqs85i1WcLHrb7fdweUl8jfAzXYm9jD6jfIGYHtk+0DXl9z8QSaAVvcE3jfKfGuG5xb6jeDAblBqvL8SX1tQI5DmW1y0A/oNpsYDfJx+EO9RWBev+opnj+TaItzut7Iaj8tCe+NdCsXJc0T8+DQbnb6zypvnZIqm+t5astKacLrvkaNkWfFqmvFchxQjUhnaafCUX2VYnrrT9gNPp2q8zxlVD3hHU3NE9XiHncY+9TXyeQb2nahsA+0rhuQv4PsAqz0aj62oFcx7CN2EFyvuN9qC053IurXXssrOdfGZn7k4ZQaQNJ3+V4kspLxGcXqruheXoI/v62GlQQ2nxb2o7AjmhcN0h38kkX135yTdKHW9Iyb+p1dg32Lxe5/2Yfv9UztWobWGvL66FeGC4w6Am2p5qX625onp6FTXFJdap7WX3dgs5f0Uqb2oX8T/h1lqmvG3juSTtnp32ZlRm3R8IYPq8u9rh1od4SOlhabqY3gnhbXI7aNKW+VsibIci90to0ODg4pL5uw3Xu9TF4UH1FsU8n1WRc59k5N3ptGGPf3R5XbDkk8GQir396Idsdezlzd+txP6peBBq+gLq/YTvU1wyrS9s+VN3wHyZ1bZ1NmG5v9PF6Xn2NKM18kp2yOU3HX8qZu+6kyLc0Qcs0qeupNt/KNOgujTFMwzeheov0kmdvUn1gpq/XDGJfTHI+n9B/4kHYHZS3YL/6mraf46fYWyxRl3L8BK3C9HhBmKNd/L+Aba4KfXISt8LG0JZL0e0N/jko25JX65NB29dYXKg1xILZwZ2dlnk6rzQN+1jjuNiqoPxCSxcqgA28alkk1VnIHrLLRZ/+NAw1YlajvY/9EsRZ/xbauU2JxGyeqdE5/lB9oXoW2l7K21WzmVU170Ptj2ZTbHdHhSm3A55gY0bcOeZjYL7juAur9BT8n9ttuPZxO9pT7+097MdvNNYwX7oWpv0IfPaWTy9RZ4JgU3XQj0d7MsY1fYPp8zaOx7E3NWbOE95YBuo5yluyfJEOSao/NgqZ1u0UXzcPp2XOK/ZXyc5L1c+xQ319fefxAJRrlXLwT8+6NmdZucM/Zv9L6PT1RU3rdgqDvp4bemdQnhL/n9jWUMvDplltb54lvgeIRCKRSCQSiUQic4H/APWHscAIoakYAAAAAElFTkSuQmCC>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACYAAAAZCAYAAABdEVzWAAACE0lEQVR4Xu1VzytEURQek/wsUTQZM3OnMSljoygLdrKSZGNhK2Vvp2zYKBYkNuz4C2QndgorNBFZSbKYFWUmzRjf6d3bnDnz7phRyuJ9dXrnfOe755w39943Pp+Hf4JIJDIhOYloNNovuT8DBupTSmX0MxsOhwelhoChHpCfknwJUGgEwhQsDzsH5ZcaAnJLsDfYB2zWJZ/HMN3ko2Yb4jQsB1tAPIbnru7xKteWAKIt2A6LqWkehWJCdws7ZnESdiY0eVsMv1M/MwVFGdBi/LRDkuNF4/F4i2xK0GtbyQ8Gg+1S4xIvqkq2MBAINMshCJKDfyU1mifdHo9lnoW1qpItNIB4Bds2LDg5WFFs4+F/wmbIR81R2BzPGf/X0A2/RPzjYIw7gKUYt4wtn+S6qoECN1QcZ6bJcG4DlOM5EolEHTQvJobfq5wLdsp1ZUGXgBrhsHdw3jaAjedAPmt8fon0+b4rKC3Q3x0aql7mbAPYeAO86Cry4yZGjydwhyZG7tH4NvhlA8T7zH+Xec3TYK5vjQEakHvmnNZvM80Gz5dAsYPOuJzx8abTtsGQG5A8ga9nnBxsk+eLoJwrTgtKTOjoYzrP4jWpMQC/Tp8LyYO7QO7IxMq2laFQqEsOwywttI3EY7hLPK+V89dSwzUEvYWuDen8Ug3y9eFPSs2fAc3uJccRi8V6lLNLJzLnwYMHD1XiG8+8yOjbJAGaAAAAAElFTkSuQmCC>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACYAAAAZCAYAAABdEVzWAAACLElEQVR4Xu1VPUhbURROsbRKQWoRQtMkN4lBMAVbtGM36WIRK4KDaxHc3QpdnAQzqNApjk6OIl1EN0GdKoSWSicJ4pAuLWgoSeN3fOea8857Lz9DwOF9cLjnfOe7934v9768SCTEPUEymZzSnEYqlXqtua4Bhl4aYyo8VhOJxButIcDUGfozmvcgnU6/gvA3oo44wsSnWkNA7zPiD+IK8dGnX4eZIcphbgD1NaKGWEL9DmOB97jUcz2AiUUIN2yNfIsnj0kd6u+IPVEXEYdKUw+qkT/nsdJQNAGb8CwouWw22681BOLsrxuLxQa1xqf+ZNo5QgKEJZ8FXMaQf9Ma5km3KWvdF+VD084RBoGfijacFJzLaBCP/B9innLcqQnEguzZvGPgWD7QRhjXJa8NNOOZo3taFtwy1pyWuraByXlM3sZYo6dVPY+BZrxELpd7BM2FrZGPGOetPpC6lojH4y94w13LBRkI4iXQr9pcvkTRaPQJ8h8NZRvQG+q6FW+BE1hB/72tcRLn4HZsjd4vm3tgnD/AguJuN8RCb7n+62eAdb5PDQO96JUkx/ovQrMm+3eAaNaaULzleqiGwTmtIRCH3rjmCejVfDhtzPWSuUBinP1jW+PzNMoLfNU6+kqIetXPLAF8Xr9ABHDHxn13g48Sl/0ZBP85yvqphK6PzZ1gPDXOp+WB1vER+m5IP4B9GL78Ra3pGrDZT81JZDKZYeP8Ee/rXogQIUJ0iBtIiMjnGYCiMgAAAABJRU5ErkJggg==>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEMAAAAaCAYAAADsS+FMAAACGklEQVR4Xu2Xu0oDQRSGk6igIHbpkp1kXWwEFeIb6BP4FIKFiJWdhY3a2yhe0cJGVEQlXhob30AbGxEbE7yAQjTof9iZMJ7sbrIiu4LzwWEz//lzdvY4zk4SCYPBYPghQohlxAvik8KyrFUPT1XlpWeIeyKkFXOocJHI5XK7yC1ks9luDJP5fL4fcz2CPsC9gegPy3ME9LNMJuNwPSpw/6sm5nihe2Rscl8jkvjSIWJHFhjhBr8JRA3m8ew3F+jnWAUTuG4gJnm+KbCUxrG0Bumz6ij3QPvgWhw0aMYJLkmuhwJFStrnR7qZ4zhdSrNtuwcdn1XjOGnQjGLiF5pRK077glwd11p+K51Od6pxnAQ1Ayv8mFY58hV6EZAPf8RR7guC9ot9XZDNqN3Q7+ZeYAfvE+7/rFesY3JrmOiKcN9iS4hFXiMIEdAM1N5DTGvjdvLifsOazR99v9A1KoKYp7HweZXFQVAzvJDP0ZwfxjLXCFUEjenFdYbn4yKoGYVCoY1rYZvhaYRelIVusI908Lwf8OcRc2GC1whC+DQDm7xFOuJA16VW5/eCTnOnXJSkwhSKCr9mYAXbpPP9QT5Dw2NBC0wP+PIlTyiQf0W8cT1O5JzqmkFIPaXG2ECnSKONVLN9B8ltmJ4QJeGeK6rcQ9DZHrkxrseBcH8/3SNuZdwhyvJ3iIJWcwXxTk2g+CtHAoPBYDAYDIZ/zRdxy8cYztFa1gAAAABJRU5ErkJggg==>

[image11]: <data:image/png;base64,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>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAABECAYAAAA89WlXAAAVM0lEQVR4Xu2dC9RtVVXHL2Bl76wIuHD3PJdLQVhmUhpSOSBKUAtLHfnKJPDR8DGUolKRHKJFmabkI5Ecpo2UEC0VEFG7CQIJKCiIpjwUBVQEElAS8fb/7zXX+eaZZ+1zznfv913u5f5/Y6xx9ppzrrXXXmvvtdZej33WrBFCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCTLH33nv/aNd1B2S52DKQpwftv//+35vlOwqj0ejRWSamWb9+/W9lmRBiB8HMzoU7C+59cGfCfQju4KpHRTqCfxPcXXAnxbAtYP5jtM/yIWB7jsffu7322uvnXf51/qIhe66nq6bvwyn8L8LmbOr5i/M/POoj++yzz/dl2SIg7i8zbYj/0KzbkUDePiyU1d1w66Oenbno31w2bNiwLssa7JIFiXn6VQV5c23Nq6zLwOakkK83Zj3hvTvUocN9eb8sg/2PZNlKsGDZLAtc8xn1GPfYifBf5u7CaJeB/ny4T1T7KmedFcymgO3n4b7L/M66WcD+8EXDIAm7w/ZTtHf3LdRtP05djQO/G22ybrskxgH/BSjb9+P3DLhzgvxWuD2i7b0ZXOsr4S62pbL+OPL3Y/g9F/nz9Gy/HXGfLIigPu2ybHsC5XOVlXv/fVkntgBWJMxY3PzHJ9V9PMP38N+5lZWVimcTHqiXZF0Gdv8Hd36SvQnuynguvFU+OJx/6iaH/NvUwe4Xsq6yaPoH2IlhV6LDdsABB3xPlm0P4Np/m+XFPEbZvoYy+qNNzWMrnbnNye+dGQbxH4bf8+CuyQaQXQh3BWyeT9tcqe25554/4ed+Ftx1cBujfmuCc391Xh5Af743Pu9mx4v3Rw4D/1XQvcPK88Jr+7ukp4yu74S4Oy7azMPKC9lr4d4Kd3vWI41vhPwWLxuW0cOSSV92cC+ygbJrget6HGyvzXIrnSo+c8/Jugr0n6UN6q99qoyjv56OZse3YuXFdGbZZKx0lOaGYcfa0/DmKIf/gnpdQXa0294dbcm6devWuu5OXONPR90i6bi3wWtG+f5Bkt3peTHVLmyr8MUWaX7vUBlCfpvXCf39na95WwRp3D/LiN+/6rCtNJ6xj4wyjliFm2rnqBvC4+ld1kVm2ZjfqEk2y/4qdCR2y/IIbK62RkO0KAh76Up02Oalc1uFeY9K5L5oRH6udtjwe2K2Ce6bdURhUfwczwz+2y087Dj+JwsNG44fyTDV7zJWcPePfrhjo83WAud9RU5fpurx+0522HjMyjroL0AF/zPB33c0YPvkIOM1Vnf3UOU5hId5R/V7Y/Gl6meDEa+D93C+Lvpnld0QDNcamUVcH6nXlHXEOzMfbujHHcckn8Aa9848Qnpmjt7SBnn2q1lOrHSMp/IuyyqQfzfLCOSXI49eneX3ZgbyqH+ZhrsuK7ZFkM7/hXs93Ota1wPZzbvtttsPBv9NtENZ7xfttjWQxi9kGfGymVsPiGXiN8VhSfbx1k01hI9ufNQLaTAcdO+ifkYHqB/ZiwL4j/Mw/xjlrhs810qBc1wyI70LwWmq7bnDhp+d2RmqHbYqSzabBTsZOTzO8/go8/tqovPl98RjeQz7P85x8H7Jsq0F0vM3s86Ne8GqHr+nscOG36Ma15yfhQmZDTTqCzL1rI3KdF5Ow3jaMshey+NFyq4F9D87ZOMdtr7D25oKhvwz1u6wLYQtY3qTID1HwP7lft0nZ30Fui/Mihdlvm/Ww//BLKtA/p0sI2zUh8JsTZCGU7JsNcB5nti63vry0NJtRdhpnFiqMw/YH9NKc74WrxMo+3K029ZoXQvxtKvDttIwY/OCVivrBZoF0QK256DTthcqt5fMCpdvyhYt/VA4m1GBrhQ4x8V4eH4zy5cD4rhre+6w4fq/GDtsLOtsE/3LAWE/l8NzNI8yTgfB7enlf3i0cVk/GuTHuTF8dpZtLeZ12IinmWvY+g4bZQj3kKTP1zQhw/FdUb8crCxBmEojZUjP0+oxryXrazibU3ZRHrEyetBs6Nhh46+fZ6Kz6HK+TG61Dhtsv+G/G2eF8/QO6knW185XrhsgexXcE6MskuO5h9illtVqgmv9dOt6zUeq4F6ZdasNy411Is596ZoFZ6AqtmCHbUi2LYHyf+ZQ+jzt6rCtNMzY2CHxG+p6z/BjZlW8FQtv+gyXK3mX/97m3oAI8y85XLfAotN99933h21prUOPlbVQRwf/zPRYWfR6J873KPrZWfEw47UTXE8F2VdCmD5OLhg3f0AR/i/9+Bi3ORbuDuqQX6/2eL9FP9wJbnOL+9/k/oM9rr6Bt9LYj9c5MG7438DjOH0F2d6Mw+M6Gf7fcPt+40cNP8AuHq53CPv+bBD0b4f75nIq8ho2ypBvu/q5/hxxPc9tHhRtYrhWHF1ZI8W8HXeCIpYWn7vteOMK/C+r8ZqvtUJn5HfcP950wdFTl/WjTqMy2jc1/ZUxL8vqRnPWfsLmQLc9Lci4to0NFxenc93cNTHMLGxgXZaf4yyk54F+3N+vST+Y77HsojxC/VC9Ejps/5rjNl+Ab40OG58hT8/EqKOVdZUf4jFfTG2Bsqkgjd8P289Wv8c/8eLg8rp5ZNnTc97w5+ucmT7ov51l9xRIy0OzbCXxfJ26XsqRd0/J8tUE5zwF99mpWb4cbKDDlsF5XuDX/qysI16n30kb2J7IOn3t2rU/6WHYttzlHcvHUhY3DYU1kn09ZmVzx5089nWYfGGgnkuU6ibAv6Jsjbd7OD4G5/1ntxu3axWXn8n72/0TbQ3kj4L/yuDfn3Vn9YsBmIldGkGyZY6wdWGB8FBYFMaRXohTugXo16dwWqEKFo0H5/3DaJvjgf4/6nEL2F9koYPnMjaU40okpwX+34V7V9Tnt2hSO3+8Wen3BiWm9XCk76nBvwnuZdVfZX7Y51HSXbY+bMjw8NlmoXy0yYXttyXdZsVJWmnqlqYD2Ml8KY9xHQ+INjFcKw4rZUD5k6K8AvkNFqadrLFRAP4vUYYyuG+QMc4zg5/50ldqQcaO69w88EXIjK93rACzTcVtcmfkG6PJTiZtbo02Q9RzDsg5cnYIj1EWz23oB/M9ll2URzxMc7H4aKmzX9ekjUfRcXyD/0512FxO+/jy+JVsh/ifkWVDwPbUunudePy3RBvCcnPdp7JuHgi7n6dnPFIzmt95/0yWLQLCva3lmH6U21usrBU9xd2UXcsh7AcYLp9rJQjTnnzGbrayPpJ+PrfN+2c1sPJCdEeeWdgcbMEOm1/nzVkeMd+4MgodHStr5SaWE3hcE+1R5y/2yea85M/1IcP9WfV3/lIcbSpD4VGmD/bjr8G9PerjdYgBvBA2u8OWOyJ8c/awO0U5e/itQlwUDzte4IjjO6J+iHxTMZzH9QncIE+Iti1gdxHsjkwyVmh9nHVEgfkQnU0ukm922IinpX+LNx/+r+fD8U3Zlg1IOk9tPPspgqjryqheP1pXw1sahanh54G47u/nePG8MNDfaD6qMQ9P00R84U3xBJz36TxGnjww2sRwrTg6f7PsfDRxHlY+c5MrmGsbMp6r/+xEHV3L95E1RoeGgN1pfg81p34I5KdbYzdhpis7SptxZMxH0RtyXt+53PDg1/a8hn4w32PZRXkkh4mMwuishVFQ3M+/3vmLjS3eYWP63xht6v0UZUNkO49/KmznmzNsgTJq4WHfymNcp2V9xsoI6Pgl4p6GabEyO/DyrNsSOl+Hit+9s25rYGVW6AbO1GTd5mILdNh8TfhE3d8C+f7UHJc1XlL8/trIY4R5OP15w4+lZ8rDTMUzChvOctsa8fDXZNnI18sj7F+7DWeRjm2tVxUNmGnrt2ANGzL+v2rhRgf532fbqsvyCPRfyzKC+J5Tw1qZ1ltoXZn5VGyS3RbSOnNEwhodNpz7eIZl58n8LQeyQ5MbdxSoRxy7xzgqFrZ5W5mu4RqdfuTHpkdu+mm7fC7X9aNBWWdh+o56uE8vxVhk0Z+xMsL4D13psPXf47M09ZM/WWJz1vtEeK3ZNnTun8SG2o8PjDYuq/k2Pq503ohyDVyUR6C/wsO+Ge6SHIelTzG4jHn83zzG79PoR5n8SrKZ22GD/tZ169b9Mn5Py9/piozKiFDzHs35PpqzhjRiszs9HB3rd+Ehzhc09DXfZ5ZdlEdymMgodNhGoUGyMKprs9Ped9jqiyPi+Ito0y2zw9ZyiPOIIdssjwzpY1gLU7BDwOaMlexErAC8V24cbeF0YWaRPF1N/Nm7fM2c3cHLweZ32PrnLgtb4F5+crY1bweSjPdsXWrAum5TrjsQ17/HcK2893jGy526+R22qbbGwpKCzr9GUd2uu+76Q9FeNMiZSFAonxwqiIw1dqrVAsjykQ//w70t6yrQXZ1lFQ87uLOqhaUOm6XdVx7nxVEWsUaHDf5/C3FO7bbLUF/fnHH8zpYe7vVcM1P9aMw3rEkLWikfDXwgGLo/XSQdFj40WmXRn/Ewx7LDNlraJTreIWalQ5cfbE6psaKby6ixwxOyR0eZp+HZ0cZl/Rs97E9txNGvaYqyCvOWOjbeVTbyz0nwuPMpfvMPQFYbl7EM+s9v1EXjcC9MNvM6bJzu+86oPA/jTQc5DEe58jRMtTHfSWlhVMMGNhK0sMZOzZF//Lp2Bjz+ifvVZR91+7ll14L6oU+/sByi3893dDe5znZuh636Ed8Hos2iHbahxsPPMRV+5Es+srzi61n7UbSMLa2BO8EW2BVoPjW8XKws5Vhpx1HFidmUlcJKnlyV5S34ghb97JAMvazRdkg3hJV7buYU5SLYjA5bV2YFxlOXhHkc/RFeR47Lyjcos4z5eK4f90sd1vvUZLCZ2OXsYVrx/G3wPyaFeV04pu1UWwP3CD/OM2Rz21GxpmQiF1Mn2eWLZB5sXmiN7x5BdinDc3SkoRv8cKXNeSC8wOmaCzFb+EMwcSNGPfynd43RwIqVDsnEPz14GsY3I45vio2/y/pGzY9v52iKH0/cxC77ekojRy6mdgBamSLK68cm1tKx0Y361NAx3RNv8PG8LRDf/6Ac900dtnEYb6haC07HX2Q3X08WbSLUxQ/hWrlHYsPL6Zbx21pd+1X9bFzdP34TtrLm5ZrqjyDNT6B97AzxfDVO80bCBt5WLXTwrZRV/pDwzE88kHCuvsPmG2TyNXHBPD9Iy0/bvLQrU0T9M8IRJFzHe6o9cftYNrvPSgd1zIvgn5jutjJNPLHgm3pLo7azyq4Fw8T7MmLTH9RmHZPLYNEOW/9PJcmm/8B3lLVA+s7OMmK+aWHt2rU/0NBdh/z8ZJaTeef0tDNfxt8SHGJeXFsLpOMxWbZS2NLMxcyPx0J//MjXfsL+ev7CfwTkb+jSZ2eS7cy2Zggv/83+OoENdNhY7lbaAT6DfOa5HIRLHCY6cJGaR0nWuuc32WR7RP94vVqQjdeUub8Vz/jj3cjLh1QbLoXowkYjt51qazrfvMdjhH981ke/CHRlKrNvWKzchBdCdpCVr5VTRsdty1N05S21bxzoYiUD/5+E8HTs8BwSw8P/R657MdcBdWWhMhvMcSPfwso3mBYuVNg+yLyCtTLq02/pp8M5D+Vb/rz4oL+INyIfdM6zd+Uvs6begj3e09Ex+yULO/mI39h3jMpfPE08KK6nPFYsU29OFSv/7nAjbJ7CG57nq7racYF7laejn17G74FsSFzHB+U1VhYY9+sd4C7l5xiWzjKJlTdprl/jF9tpnzdh3IpO3QM44uTnyYvjpxrdSOfrGXhspcw4AtOPNjr921e3tLuV6Zn4DtSojJD1lbANfLspwjRaycs9cO2/Visf/L7Hylvo+LuCcJd5GfUvMu5eEeJi2s62kvarQl5PdD4iYXcpv/P3Fo+jH2kj4TwTjrbB5rKuvGzwEwv9KOModNjhfyhlceF8pCs7tTax3MLuzomP73qcz3f7L/Laoj6UHadyWmU3BWyuY34lGRupforV0zF+ibLwCRDzFz533ChCHa+fH/2t8rh4mvfK56AfWemA/qfbNEfVrXzctMaTO+L9i2hwU+UbdEdxVK3uLM5TUBlLne1ZLGq32thmbn6Yhy2VER1fmprrYb1MY73JtW4TU4pDx7xv6/Fy2bBhw08hrltZV2TdELwGC3WK1xHj66ry7EZh01nEyq7x2gbfMCp1Or+AUMP2dbotLfug60fZPDz9fHlhm8h13f0zxhcR81kTOj5XXWnzrq6ybvrj3Yewbgiy/oXKXf8s2lJbwzo3PsNH+c7U47z8xDbKTqMybcVKdKE3Ft9VOf5vvc1h5J958MX7E2v35oFzPyI3aBE2/NA/bk1jzQNH2KA7KMsro7QuppuxWB66+8H+yKEb3BuJg7N8S7Dyl0/vzfKKlbURZ3X+MdsWe4W/Esog7B6sHPgAZ13F75eT+DaXdWRUPkXB/8dd6M0f9vuxQmR+umhiCno5cMq7doxYdnR5YW8Lv+aJfxpZDixnxPER3g9ZV7HUwY54Bc1drRwlbV5/V0YmPubT9FOw7ODePavsIqzwYbvVOh28X0a+zpDPL44P48LubLdSsMOK6zsZ7jyeK+tbsC6y8BIwhE+tbrW8G2K0jM7KaoF8uLJLsyNWppc/z2M+2zj+YNVl2y3FOxpXZPn2gm9umPpMzXLxNm9ZoGx+3393Z/ihJRJCiHuA+DdLYuvBBj7LtgXQUFyPyvoZWS5mw84aG7ks3xFBXmyML91WNsu9qPPvszGv/IXkq/RH21kvlkIIsUNjc9Y1idXBNvNTE6tN68/uxWysfGx5Y5bvyCA/ru7KDsfxZjUrU3x8IeCX+C/h8oNsO7SpRAghxCrtJBOz2ZYbJjSc67fl9G1jcGdx3lknhBBCCLH6cD1blolpbMZ37YQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQ9xb+H7RRnVWv37OkAAAAAElFTkSuQmCC>

[image13]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAC0AAAAaCAYAAAAjZdWPAAAB3klEQVR4Xu2WvUoDQRSFE6zEQqy2yG52s6lFEMTCSkUQBcE3sBJBrGwtfABRsbKyUBC00c7GwkpsBAXxBbTwP8QfRE3Uc8kMXC47s9MJMh8cNnvuPXdmNxNIoeDx/GPiON6AnqEfpjq0nNH7IPqsUpltqMn8b2hPzB0X2TteN6ID0udQPYqiPunRRrhXLpen4b1wL28+MiOoH0rfRlENPZUFDTY7gfo89yqVSg/lkiRZ5X4QBB3wN7mXt2lbLRMEZtXQMVnToFaTHt7OPuVw7RL+MD0k99B3ZdoYHnoX6pe+FQy7NQ3UYOiM9ExvLwzDblyK3ItbZ5v6e7mP3nZ4N9xzwrR4HirXlH4Wsfo28S3MCf+D3zujFj+Rvg36Qarckqxlwc7/jvbweQpaZG1u6DcQG84z/CHpEfAPKJemaaesmVDrXPN7XncGwXtbGLW69Ai1AWMuC57B9QJvP5A9TtgWh78ADUqfULmG9G3otXCuU1yPZd2VNjXoXBaq1WpkehgsOqByTudZozdtmusEFl9RQyaFv678M+5r4F9SHT+iRNZsINNQuVFZywXBLegzbv0noP8CtEEtuqfh76VSKWSZNegNqkGP0BP0Cn1RL59vAn1HlJW+x+PxeDx/wi9RC759CYa9FgAAAABJRU5ErkJggg==>

[image14]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAaCAYAAADxNd/XAAACP0lEQVR4Xu2VvUscURTFFwRFUogKbsIu82ZnNwQWTJEiJDYWIZVWFqksbLRIEWwtTJcipEthSIoQyJ+RTkgRUhgCEjBYWImKIUT8dtVz9U64e3be7ETWJswPLjNzzn33vjfzZqZQyMm5PsrlcikMw1nE2yAIolh3zo3YvDSQ+wKxwLoP9OlHzGDMu0qlcj/WcV60ealg8EfEGeInYgwLuS2TQKwjHorHY3xILib0hXUGefPacwv5T3DTQtUOq9XqUOaeWuQ0iqI+9lBzTnwcv7OXBHJXtd4eexb4B5InNyrBu7hhMif2WkDSSbuVarEJ1plSqVRG3lfN99aEt5HmC1rjNetNIOG3JOIu9LJnadcsJs5LWwD0b+Jhf99hz6LzGmD9LzCHJQlbY4U9xjcZC3KeSuh54gJqtVqPeifsMUnjm0BCQ5KS9v1VsA19C4C2Jjpe2Efs/TO+JlcBT3ERtW7F1063ps1RvWM9O1asWCzeQJ0fVnP6IuO0i/SO9BS6tNgGG0y7hvAPEX8ojmQcXtS7lJtpATKetRayFMPWeICYYj0Ge3kc/ssE/ZnUxnHS6ll66l/5A+stOP3hFOgxG+QpbbJo8U0GE3isk31ldVy/Fx0fjsDqFvgN1rxoE/mk8V69h9iymkXukrvcJkvsCXgqo1r7M3vQ9sXDT2/Q6hhzE/qx1TKBQZ+0mcSuHDHBac6Lgb/sLr8yv3QyTYuQSai/jdhBNOr1erfNQf03pufFFwvac5uTk5OTk5Pz33IO73PJoqqCzL8AAAAASUVORK5CYII=>

[image15]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACIAAAAaCAYAAADSbo4CAAABiUlEQVR4Xu2Vq0sEURTGN1gsBo07T1iDYFJsFotWo4JBLGLyD7CYzIo2qyBYxCSIURAEk7DiowgmWXRX8VF0/V3m3OXucTe4zEyaDz72nu+cuee7j9kplQoU+AeiKNoMw7ABm8JP+Oxq1Bzo5zKDbar1OI5DMXOic5lAjJxr3aCbydTBaudk1TM653lef25GaFLt1gj9UEzO6lzq6LZitCkxsaVzmcAagXX4Ar8kviqXy0O6PhPY+wGXdC5XYODGGNF67rDHovXcIUbutd4JHOMRtcfw0WqMR+ADrJJfQepz6iP0V7gPd63+ByTXjBHql3VOg7oPLq4n42alUhngP2aQ8bdT09rZIAgmiesyXjXP21wLiNvwLUzeEPNdeYc/us4Co/NuEwszB00WnLhVY8bm82DjVICRCybe0brbmJpF4tNOudRAk3VWvmFj3/dH5fzdHWiwA9P8XkvcZoTyWzfuGUx8GSWX9QnGoo3BmmmCuQnGdxgeNznuz3CYHPsZ3GufrUCBAr3hF+u6gj8zbrA6AAAAAElFTkSuQmCC>

[image16]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAF0AAAAZCAYAAABTuCK5AAAEbklEQVR4Xu1YW2yMQRQuDRqeCEovO922iCYETRB3gigiLhGhDyJeRN3SB+KWSCrSxC3xUA9KECQ0xCXqGrdGxEMf3EqDNOoSpFGNlKhofWf3TJ09+2/772pjH/4vOflnvvPNmTPzz8w/uwkJHjx46ACkpaUNSk1NTdO8h05CdnZ2D2PMDVh5cnJyL+330MHIyMg4g8luhpXAtsBe+Xy+h1oHfiWsEdYC/1XtJ4Cvhc2lF4cX2Q+xV0HfpHVugHal3FdtZmamT/sJ8E+FvSAd7KT2W8BXxpqqlJSUntrfJpDADG68WvtiAeL4Yc1URuy1KC9g/rjf758kdJWYwOVcTeQcWmiHWA3rAry0nJyc7lLjBpQT+p8p6i3of5bSFJLO1vkFt0hNbm5uN+LES7O5D5Q6V8AEjefGu7UvGqD9bdgRLhfAFvBRQ7Evs6wryr/kaqOVzJqQVczcPuS3H9+IYdLnFmhfRHEkR7tHc9zXUM1h8otFvQL2Tmn26FhRgT5+CPATdkr73ACDuYu2jVQ2POlcpgHlUZlWGNedBh3GyXos4LhVTnxWVlY6lZHTfKe+THAuWnmOVaI045zaRg2cU30RqB7J3NO+toA2eZxYA2yN4UnXAH8Y5lccteusSb8ZgT/A5VtOfYGrEbw9SrZJDY4tw/xCyccMTHoSd0wrJVH7nQDtB07CWqnWaNDHiLVvJc/cV9h9WDWsQfrdgGJgHBedeNgVLlMfTpP+zPKIMYLbFEoNfeCJxy7fJPl/ArZgf0oq0g3DCdAv4wStPdEaCfi/28EpXq/8L5prB/T9oP7PaQfzL0U5LC64R5bHcxqVMQ/rpAb13tz+kORjArbNEARqwhs+pn1ugLYFSGgxnmcpKcQbrjUEaNbzwNrdSfZGkZ6ePlH7IoEn6rwTD6vgcmB3OmieWh4f/sFURg4bpIaPYopVJPmoQFc7TnSX9rUHJDQZbeuobIIf0sA5Z4L39rJQdWDCc8mn+UhA/Cmc20HtiwTWX3PiDa9OE/lMfy34LlRGDpulhj7GHCtf8q6AYEu5ccx3drR9w0nSR0feXu7ATkgtr5AfkjPiTDfBFxUyEfaqB9sp+bbAesfbC8a8hMtbdV/Mu769mGju6r7gjxjasvO0L1pgEMWINYrKJnTSf8NGCim9lHpRD8BhgO+ln+PLHyfEDcj4+0MrDNBXybgE7ObRmqM6rsx9NAe7JOrN6Oux1GD+NupYbQIBdhiepI4CJYAXmGV40pHUUTw/a00Eaz1qUF6kz2LWPHfgIn4TaCLJj7EmWQ71b7BKqUP9I6zG1ullUjv6FWo55DOB+2oF9x+4ev5XIOHrdjJM+HbMF74Q02cvuL3s+8TPsBuCCR4NVehzhfZZIO50ag/NBTzrYQ+0hgC+jvsq53wytcaubMQ6jWeT4V/gcQEjjpfOBvqZjUkYo/m4BLZeKhKe48YwqLG6fbwA+VVrLm5BNwhaIW7MqD+D4gV0Z0du2zXvoRNhormqefDgwYMHDx2EPztKsWMltUe/AAAAAElFTkSuQmCC>

[image17]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAAaCAYAAAAEy1RnAAACXUlEQVR4Xu2XPWgUYRCGcxpRhJBC8OfOu839wDWC4kULsZCQTiyFgJDSRmxiI9hYKig2qQJCwDJN7CKGFIoKgqDEn9glBLSQJEokl5BofIab0eG7PdKYYpd94WVn3pmd75vZn9vr6sqQIUNqEUXRPfgDbiubcAlumtYHwvNSAWswRp8WvVgsVsNY4qFNv4jRBzT2IYwlGty9Q9JYqVQaDGPoYxobD2OJBk19jLu1BXqVY2OJRlxjXP1TaFtw3uupgTa9RKOvOb6FG6LVarX9YW4qYM8zHPA6/qfw6uNfE43ne9jriQNNfA6bEzCMO6JXq9XDXkd7moam5Sq3NY32U/Wc12n4SVqaftlBbxuGNv2A2Cv4HE5YrNFo7NNh3YBrSN2i+1p85JxRf93HKpVKL3WnsFc5nrea+MfgJnfebashwH+m+1in5gnTdwQn3JJCnHwpJvZ3o+bLUTbGgjedPmO+zw99b1OjIZv1sejf8HKdzsNelTjr3YWP43I6gqRRKQBXotZ39nf4y+fI9HQzX2CzXq/3iK5XY8TysK9IXqFQOB4urv4eZ5t+Ogqapomj3tfjxbCmxeE3uKhsy/mvCJvGv47/mxdeMVxc/Hw+f9Bs0xloP/6Gz2Noh7wvRwZxIaxpcda9HOq7Bm36vvnY7+RnT22/wb0yDHN8DPsh3PKxcrl8xPvepv4BdXMyMHJPoi+4nEdm7wqkaXnpsNB7uIx/1cfR5uAs+qTX2ehZ9K/wTV/ra287av19lQ8hecRW5Ocxaj1q4jddzXmpCUeddk5rLPiBZciQIUOGNOEPWiLpRYdo/k8AAAAASUVORK5CYII=>

[image18]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAZCAYAAADAHFVeAAABsUlEQVR4Xu2UP0sDQRDFY1TEP/inOA7PXDa5pBOrIBZqKSJaWSp+BVs/gFgKoiBYCVqojakECxs7sZQgiKBfQCwsFBSjb2QP555rYmrzgyE7b97O7G1ySaWaWPL5vJ/NZodZ15RKpXbWGiaXy10aYw4wbBmfj1wXMplMJ2ofrCdAgwmYHsSIuICU1nVog7oJ1meIJ8Q1YhYxg7gTTxiGk3pvAhi2ENsqf5ZNOEAUa1gf6mFoOAptzqZt8kT2qW5jjxNpgisaY003x7qic9CKfFXl4nnX+Q983+/mxgJreIoVyqdwwOk4R22z5vXFyAmxeZy0xLAoivp0btQPxPO8HlPv+mphh1VJm0e8Ie5xuCWlJ3wNgeu5kmFBEHRxjYF3R98K9q3Zgy5onxP5oYi5WCx6XGPg6YX3Js6xPsHgU7s+LhQK4bebgHHADurgmgvx1smdL76Qdpj3da7BwXbpdWlx7Hf/kxjHl2x+eW8wpB+1CuvcnPNYfJWCK9gr/FU3fI34ixniASpeEubUV4M97BlhXUBtHU99ZNdl6c2ehsB3dc6aBsM2MKiKWORakyb/lE8UdYkk+7UI6gAAAABJRU5ErkJggg==>

[image19]: <data:image/png;base64,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>

[image20]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAE8AAAAaCAYAAAD2dwHCAAADSElEQVR4Xu1YS2yMURSeEfF+JVLDTDtHZypNSrwiYUHQ2ImFejfBRmxIrNh0Q0JiwYJ0ZSV20o1YiISkC/HcEA0lUalFbagpxbSqHd+Ze+44PX7JjGgbcb/k5D+ve+79v/v4H7FYQEBAwH8KIjoH+QgpiOQhvZAh71sM2HYBCp6oCP9t9tfU1GRtLEAg5N2N8DdK7JmNBQDYlXuZoHQ6vcXG4L8kscs2FhArEvQ8assyZNVFxgJi0QRhNa6E7zukW/sDDIS8XhD2CNcnkEH21dXVTbW5AQr+vIM0aj/sTrsaJwq1tbUrMJZ3FPFAs0BOF+S09Y8J0NHLKJJA6ln2Z7PZBTY2EcADa1c55GHcp5C3yvqjkEgkZqLuUusvG7LqfiEPvs/ij9vYRABj2V4OeZUA9W78DfLu/cYfReoiyBBm+KSOQz+EgVyD/wLkKvvUkdAGeQxph3RhGy5H7Dr0fHV19RJpXzxnIUfJHRn9kDOqfom8hoaGKdC/oL9jXAMv8Enpb63UKOaJXshkMnORe5Nr4rpeYvwlVYyz+H7KBhq1cEMU3BYRG1XU68bXj0tczqQ33o96J2CfF/2ArcMEs47rQtiDKjYC30aTu070EnnoLwG9R9ImmfrNPk/sAqRNzLgdS8UrD41ayc1sjtx3bB9kWOdgNpdJx28h+fr6+tm4btWde8D3itQq4QH5PHI380LlltrzitA2udW3WtkPSL5syJFX2iF8XpF7gX9tajSRIY8nSdtar5i8PwUGsUl37kHuCdfqbRC/xuehzR7oHSq31L6qqmqWuZkBGk3eLbR/KjqTd1/045BPKk/XGHU2ciyVSs3XttJHeNewzhPp/WMG7hw3NE3MOBPFPw3gz6mcKyQrETO7H3qnipUGj/fIOeZmmLwmZRd4hbGOOrshD70fYzjIOm46LfY+ie0gQx5vc20rvQdj35BMJmfExuvBiE67IR2kVhufVbCHIe8hmyWPt2zxaOAVRD9/d/XJlvXHxoDkD4Cgw+Q+F4fwMEmxH76dkvuB3NadTO432h3IEXIv9u0m7yK5Y4Dr5/iVi9zxxHZexjwP+lc/Kf80cCPfSG3bgDLBry8grgBpwYqbbuMBAQEBAeOPH18iO+Hm1cNsAAAAAElFTkSuQmCC>

[image21]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACsAAAAZCAYAAACo79dmAAACUUlEQVR4Xu2VP2hUQRCHLykUUUEj52Huz7vjTg6OYMRGhKCFRAipFCMEEywESwlBUwSrFClSWqYLCnKpYiNopZ3BVKZIHWIhiJ2CCFG/ibuXYbJ7dykSUN4Hw9v5zbzZ2Xnv3mUyKf8BSZKMNhqNI1bXlMvla1Y7dGj0d6VSucF1vVQqzdu4QOwJtmb1PeRyueOc6o0UxT4g9dicTsQ2ou5HbMn7bg+xRRofxh56Td8XpFAo5CWR6zHx8/n8GXdjr0ndAxutqs2Dm7nYqPK/+TXTzjntebFYHPB6FBK/c/Km0dawH1prB7nT7ZrV7yL+WxWWYfXJflqLIsWY0B2jzcY2D9GpWeqPKX/bxrUfhcdw1RUb0jqTuCe6nFrrMdo1S62XxDa8z3pTxZa7evwCyVOyCXZJ6zIJ0Ylf1nqMds0KxL5S853L2fnxVqvVs8nfH3N3kDwnBZjwBaPfdIe4q/UYnZoNYfJ78dexLVkrfRdO+0BuYoIXjX5bdK7XtR5jv83Kq0Hthvfl3mw2e8KvdzMV/p3FrmidQpOiy2dN6zH20yzvaD+5773P+r6+l70n6GvQ+y1qtdpRN8ED+xpYbB57v9YaUz+FNqNzWrjJPjXaq0DRMf8Rt3TbrNTlaZ3XGs01zWRP4z/WOS1CU3QHuKWkHqcFG0JfkBhPKmtjHv4ZC4n5QxDQRkyzk8HXwEPyC2zbXeUHN2VzKLJC7JHW8H9in7FP2Ja7fsGe6TyXGzyoQOxXvV4/6dbRvEOBw4/TxDmra4hvimVin66UlJSUf48/B0i5ZE97fzAAAAAASUVORK5CYII=>

[image22]: <data:image/png;base64,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>

[image23]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACYAAAAZCAYAAABdEVzWAAAB90lEQVR4Xu1VzytEURQeJT9SotRkmpk7jUkZG8V/ICtJNha2Un5ExErZWCkWLKxYKgs72YmdBStqIrJiErGimDTT+E5zb3M67n3NS1MW76uve853zr33e3PvexMKBfgniMfjQ1KTSCQSPVKrGmCoWymV02M+Fov1yR4CTN2hPiJ1J9C8hElTUjdAfQV8Bz/BcUu9CDMdFMNcK/IvsAAuIh/AuEM94LOc+wto2ge/9QTitOwhQL8Gj1meAc9ET9GVI27XY67cUSFcxlKpVLPclEAafuEWiiORSJvsseTLys8RGriMQbuUm2id+nd5LussrVWVHKENHsZIdxnjx0VXYoxi3Kl+cILXTOwbfzXGtD3wjWmrOPJh3ucLetEZh16RMYl0Ol2HnieTI+5Spbf6lPd5gjbBzz9r020GXDoH6nkT85coHA43Ib4pd3pAG5uz6TYDLt0Ax7eG+qDJsfYDtEOTo3ZvYk/QJpg4b9E/bAa0MetTY50G1LJc0/3brGeT153QxhakjicddRlDrVfqBNQKFk0a2+J1K8wHEtyQNYI2PcnydZtZAq1BnwupQztH7cjkyusoUTwAX8Es+KjHFyW+O9FotFGbu8B4pUp/LTW8h6CP0LohLn+9eRh9+TOyp2rAZrdS40gmk5300OCJrAUIECCAT/wAyoK0MslSk+AAAAAASUVORK5CYII=>
---

## Appendix B: Pre-Sold Protocol — Copy Examples by Trigger Type

These are the core email patterns for the Pre-Sold Protocol offer. Each follows the same structure: **friction → impact → solution (+ optional proof) → low-friction CTA.**

---

### Pattern 1: Booking-Only CTA

Subject: discovery call drop-off

Hi [Name],

Your only CTA is a discovery call, which means most visitors leave before they're warm enough to book.

You're filtering for the most ready buyers and losing everyone else.

We build content systems for coaches that warm your audience before they ever see a calendar.

We recently helped a personal development coach go from 2 booked calls a month to 9 within 60 days of launch.

Is capturing more of that traffic a priority for you right now?

Thanks,
Rodney

---

### Pattern 2: No Opt-In or Capture Layer

Subject: traffic leaving with nothing

Hi [Name],

Your site drives visitors straight to a high-ticket offer with no capture layer in between.

You're only converting the people ready to buy on first contact — a small fraction of your traffic.

We build pre-sell content systems that capture and warm everyone else before they disappear.

Is that something you're actively thinking about?

Thanks,
Rodney

---

### Pattern 3: YouTube Channel, No Email List

Subject: YouTube audience, no list

Hi [Name],

Your YouTube channel is building real trust, but there's no mechanism moving that audience into a list you own.

The algorithm controls your reach right now, not you.

We build content systems that convert YouTube viewers into an owned email list.

Is building that asset a priority this quarter?

Thanks,
Rodney

---

### Pattern 4: Generic Newsletter Subscribe

Subject: newsletter opt-in drop-off

Hi [Name],

Your email opt-in doesn't give visitors a specific reason to subscribe, so most leave without joining your list.

That's a consistent leak that compounds over time.

We build targeted content sequences that give people a compelling reason to opt in.

Is growing your list more aggressively on your roadmap?

Thanks,
Rodney

---

### Offer-Specific Rules

- Never name the deliverable format externally (no "email course", "funnel", "sequence")
- Never say "Pre-Sold Protocol" or "Pre-Sold Content" in outreach
- The optional proof line should be specific and believable — skip it when you don't have a real result to cite
- CTA is always an interest-based question, never a meeting request
- Sign off as Rodney — first name only, no title, no signature block in first touch

