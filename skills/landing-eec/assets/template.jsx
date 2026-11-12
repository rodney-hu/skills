import { useState } from "react";

const CONTENT = {
  meta: {
    pageTitle: "{{CHALLENGE_NAME}} | The Free 5-Day Challenge",
  },
  hero: {
    eyebrow: "The Free 5-Day Challenge",
    headline: "{{NUMBER}} Days to Finally Fix {{DOING_TOPIC}}",
    headlineAccent: "One move a day. Real results by Day 5.",
    subheadline:
      "Each morning you get one focused challenge delivered to your inbox. Do the thing. See the shift. By Day 5, you'll have {{TANGIBLE_OUTCOME_1}}, {{TANGIBLE_OUTCOME_2}}, and {{TANGIBLE_OUTCOME_3}} — without {{COMMON_FRUSTRATION}}.",
  },
  primaryCta: {
    inputPlaceholder: "Drop your email to join",
    buttonLabel: "Accept the Challenge →",
    microcopy: "Free. Starts tomorrow. No fluff.",
  },
  whatToExpect: {
    label: "Inside the Challenge",
    intro: "Five days. Five moves. Each one lands in your inbox first thing in the morning — short enough to act on the same day, specific enough to actually change something.",
    days: [
      { day: "Day 1", title: "{{DAY_1_CHALLENGE_TITLE}}", teaser: "{{DAY_1_ONE_LINE_TEASER}}" },
      { day: "Day 2", title: "{{DAY_2_CHALLENGE_TITLE}}", teaser: "{{DAY_2_ONE_LINE_TEASER}}" },
      { day: "Day 3", title: "{{DAY_3_CHALLENGE_TITLE}}", teaser: "{{DAY_3_ONE_LINE_TEASER}}" },
      { day: "Day 4", title: "{{DAY_4_CHALLENGE_TITLE}}", teaser: "{{DAY_4_ONE_LINE_TEASER}}" },
      { day: "Day 5", title: "{{DAY_5_CHALLENGE_TITLE}}", teaser: "{{DAY_5_ONE_LINE_TEASER}}" },
    ],
  },
  socialProof: {
    label: "From Past Participants",
    items: [
      { quote: "{{TESTIMONIAL_QUOTE_1}}", name: "{{TESTIMONIAL_NAME_1}}", title: "{{TESTIMONIAL_TITLE_1}}", initials: "T1" },
      { quote: "{{TESTIMONIAL_QUOTE_2}}", name: "{{TESTIMONIAL_NAME_2}}", title: "{{TESTIMONIAL_TITLE_2}}", initials: "T2" },
      { quote: "{{TESTIMONIAL_QUOTE_3}}", name: "{{TESTIMONIAL_NAME_3}}", title: "{{TESTIMONIAL_TITLE_3}}", initials: "T3" },
    ],
  },
  author: {
    label: "Who's Running This",
    name: "{{SENDER_FIRST_NAME}} {{SENDER_LAST_NAME}}",
    title: "{{SENDER_TITLE}}",
    bio: "{{2-3 SENTENCE BIO — who you are, why you're qualified, and what you help people do.}}",
    initials: "RH",
  },
  secondaryCta: {
    label: "Are you in?",
    supporting: "{{NUMBER_OF_SUBSCRIBERS}} {{SPECIFIC_AUDIENCE}} have already taken this challenge.",
    buttonLabel: "Accept the Challenge →",
  },
  trustSignals: [
    "Free to join",
    "One email per day for 5 days",
    "Bail anytime — no hard feelings",
  ],
};

const style = `
  @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=DM+Sans:wght@300;400;500&display=swap');

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --bg: #0d0d0b;
    --surface: #131310;
    --surface2: #1a1a16;
    --border: rgba(212,185,120,0.15);
    --gold: #c9a84c;
    --gold-light: #e8c97a;
    --gold-dim: rgba(201,168,76,0.12);
    --text: #e8e4d9;
    --text-muted: #857f72;
    --text-dim: #4a4640;
    --white: #f5f1e8;
  }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
    font-weight: 300;
    line-height: 1.7;
    -webkit-font-smoothing: antialiased;
  }

  .page { max-width: 700px; margin: 0 auto; padding: 0 24px 80px; }

  .topbar {
    border-bottom: 1px solid var(--border);
    padding: 20px 0;
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 72px;
  }
  .topbar-dot { width: 7px; height: 7px; background: var(--gold); border-radius: 50%; }
  .topbar-label { font-size: 11px; letter-spacing: 0.15em; text-transform: uppercase; color: var(--text-muted); }

  .eyebrow {
    font-size: 11px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .eyebrow::before { content: ''; display: block; width: 28px; height: 1px; background: var(--gold); }

  .headline {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: clamp(36px, 6vw, 58px);
    font-weight: 600;
    line-height: 1.1;
    color: var(--white);
    margin-bottom: 6px;
    letter-spacing: -0.01em;
  }
  .headline-accent {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: clamp(20px, 3vw, 32px);
    font-weight: 400;
    font-style: italic;
    color: var(--gold-light);
    line-height: 1.3;
    margin-bottom: 28px;
    display: block;
  }
  .subheadline {
    font-size: 17px;
    color: var(--text-muted);
    line-height: 1.75;
    margin-bottom: 40px;
    max-width: 560px;
  }

  .cta-form { display: flex; flex-direction: column; gap: 10px; margin-bottom: 14px; }
  .cta-row { display: flex; gap: 10px; }
  .cta-input {
    flex: 1;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 14px 18px;
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    color: var(--white);
    outline: none;
    transition: border-color 0.2s;
  }
  .cta-input::placeholder { color: var(--text-dim); }
  .cta-input:focus { border-color: var(--gold); }
  .cta-btn {
    background: var(--gold);
    color: #0d0d0b;
    border: none;
    border-radius: 4px;
    padding: 14px 24px;
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    font-weight: 500;
    cursor: pointer;
    white-space: nowrap;
    transition: background 0.2s, transform 0.1s;
    letter-spacing: 0.02em;
  }
  .cta-btn:hover { background: var(--gold-light); transform: translateY(-1px); }
  .cta-btn:active { transform: translateY(0); }
  .microcopy { font-size: 12px; color: var(--text-dim); }

  .trust-row {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
    margin-top: 20px;
    padding-top: 20px;
    border-top: 1px solid var(--border);
    margin-bottom: 80px;
  }
  .trust-item { display: flex; align-items: center; gap: 7px; font-size: 12px; color: var(--text-muted); }
  .trust-check { color: var(--gold); font-size: 13px; }

  .section-divider { display: flex; align-items: center; gap: 16px; margin-bottom: 40px; }
  .section-divider-line { flex: 1; height: 1px; background: var(--border); }
  .section-label { font-size: 10px; letter-spacing: 0.22em; text-transform: uppercase; color: var(--text-dim); white-space: nowrap; }

  .expect-intro { font-size: 15px; color: var(--text-muted); margin-bottom: 32px; line-height: 1.7; }

  .day-list { display: flex; flex-direction: column; gap: 0; margin-bottom: 80px; }
  .day-item {
    display: grid;
    grid-template-columns: 52px 1fr;
    gap: 0 20px;
    padding: 22px 0;
    border-bottom: 1px solid var(--border);
    align-items: start;
    transition: background 0.15s, padding 0.15s, margin 0.15s;
    cursor: default;
  }
  .day-item:first-child { border-top: 1px solid var(--border); }
  .day-item:hover { background: var(--gold-dim); margin: 0 -16px; padding: 22px 16px; border-radius: 2px; border-color: transparent; }
  .day-num { font-family: 'Cormorant Garamond', serif; font-size: 13px; font-weight: 600; color: var(--gold); letter-spacing: 0.05em; padding-top: 2px; }
  .day-title { font-family: 'Cormorant Garamond', serif; font-size: 20px; font-weight: 600; color: var(--white); line-height: 1.3; margin-bottom: 4px; }
  .day-teaser { font-size: 13px; color: var(--text-muted); line-height: 1.6; }

  .testimonial-grid { display: flex; flex-direction: column; gap: 16px; margin-bottom: 80px; }
  .testimonial-card { background: var(--surface); border: 1px solid var(--border); border-radius: 4px; padding: 24px; position: relative; }
  .testimonial-card::before {
    content: '\u201C';
    font-family: 'Cormorant Garamond', serif;
    font-size: 64px;
    color: var(--gold);
    opacity: 0.3;
    position: absolute;
    top: 8px;
    left: 20px;
    line-height: 1;
  }
  .testimonial-quote { font-size: 15px; color: var(--text); line-height: 1.75; margin-bottom: 16px; padding-top: 18px; }
  .testimonial-meta { display: flex; align-items: center; gap: 12px; }
  .testimonial-avatar {
    width: 36px; height: 36px; border-radius: 50%;
    background: var(--gold-dim); border: 1px solid var(--border);
    display: flex; align-items: center; justify-content: center;
    font-size: 11px; font-weight: 500; color: var(--gold); flex-shrink: 0;
  }
  .testimonial-name { font-size: 13px; font-weight: 500; color: var(--white); }
  .testimonial-title { font-size: 12px; color: var(--text-muted); }

  .author-card {
    display: grid; grid-template-columns: 64px 1fr; gap: 20px;
    background: var(--surface); border: 1px solid var(--border); border-radius: 4px;
    padding: 28px; margin-bottom: 80px; align-items: start;
  }
  .author-avatar {
    width: 64px; height: 64px; border-radius: 50%;
    background: var(--gold-dim); border: 1px solid var(--gold);
    display: flex; align-items: center; justify-content: center;
    font-family: 'Cormorant Garamond', serif; font-size: 22px; font-weight: 600; color: var(--gold); flex-shrink: 0;
  }
  .author-name { font-family: 'Cormorant Garamond', serif; font-size: 22px; font-weight: 600; color: var(--white); margin-bottom: 2px; }
  .author-title { font-size: 12px; color: var(--gold); letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 12px; }
  .author-bio { font-size: 14px; color: var(--text-muted); line-height: 1.75; }

  .secondary-cta-block { background: var(--surface); border: 1px solid var(--border); border-radius: 4px; padding: 40px; text-align: center; }
  .secondary-cta-label { font-family: 'Cormorant Garamond', serif; font-size: 30px; font-weight: 600; color: var(--white); margin-bottom: 8px; }
  .secondary-cta-support { font-size: 14px; color: var(--text-muted); margin-bottom: 24px; }
  .secondary-form { display: flex; gap: 10px; max-width: 420px; margin: 0 auto 12px; }

  .success-box { background: var(--gold-dim); border: 1px solid var(--border); border-radius: 4px; padding: 28px 24px; text-align: center; }
  .success-icon { font-size: 22px; color: var(--gold); margin-bottom: 10px; }
  .success-title { font-family: 'Cormorant Garamond', serif; font-size: 24px; color: var(--gold-light); margin-bottom: 6px; }
  .success-sub { font-size: 13px; color: var(--text-muted); }

  @media (max-width: 480px) {
    .cta-row { flex-direction: column; }
    .secondary-form { flex-direction: column; }
    .author-card { grid-template-columns: 1fr; }
    .trust-row { gap: 12px; }
  }
`;

function SectionDivider({ label }) {
  return (
    <div className="section-divider">
      <div className="section-divider-line" />
      <span className="section-label">{label}</span>
      <div className="section-divider-line" />
    </div>
  );
}

function CtaForm({ inputPlaceholder, buttonLabel, microcopy, onSubmit, submitted, compact }) {
  const [email, setEmail] = useState("");
  const handleSubmit = () => { if (email) onSubmit(email); };

  if (submitted) {
    return (
      <div className="success-box">
        <div className="success-icon">✦</div>
        <div className="success-title">Challenge accepted.</div>
        <div className="success-sub">Day 1 hits your inbox tomorrow morning. Show up.</div>
      </div>
    );
  }

  return (
    <div className="cta-form">
      <div className={compact ? "secondary-form" : "cta-row"}>
        <input
          className="cta-input"
          type="email"
          placeholder={inputPlaceholder}
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleSubmit()}
        />
        <button className="cta-btn" onClick={handleSubmit}>{buttonLabel}</button>
      </div>
      <div className="microcopy">{microcopy}</div>
    </div>
  );
}

export default function EECLandingPage() {
  const [submitted, setSubmitted] = useState(false);
  const { hero, primaryCta, whatToExpect, socialProof, author, secondaryCta, trustSignals } = CONTENT;

  return (
    <>
      <style>{style}</style>
      <div className="page">

        <div className="topbar">
          <div className="topbar-dot" />
          <span className="topbar-label">Free 5-Day Challenge</span>
        </div>

        <section style={{ marginBottom: 48 }}>
          <div className="eyebrow">{hero.eyebrow}</div>
          <h1 className="headline">{hero.headline}</h1>
          <span className="headline-accent">{hero.headlineAccent}</span>
          <p className="subheadline">{hero.subheadline}</p>
          <CtaForm
            inputPlaceholder={primaryCta.inputPlaceholder}
            buttonLabel={primaryCta.buttonLabel}
            microcopy={primaryCta.microcopy}
            onSubmit={() => setSubmitted(true)}
            submitted={submitted}
          />
        </section>

        <div className="trust-row">
          {trustSignals.map((t, i) => (
            <div className="trust-item" key={i}>
              <span className="trust-check">✦</span>
              <span>{t}</span>
            </div>
          ))}
        </div>

        <SectionDivider label={whatToExpect.label} />
        <p className="expect-intro">{whatToExpect.intro}</p>
        <div className="day-list">
          {whatToExpect.days.map((d, i) => (
            <div className="day-item" key={i}>
              <div className="day-num">{d.day}</div>
              <div>
                <div className="day-title">{d.title}</div>
                <div className="day-teaser">{d.teaser}</div>
              </div>
            </div>
          ))}
        </div>

        <SectionDivider label={socialProof.label} />
        <div className="testimonial-grid">
          {socialProof.items.map((t, i) => (
            <div className="testimonial-card" key={i}>
              <p className="testimonial-quote">{t.quote}</p>
              <div className="testimonial-meta">
                <div className="testimonial-avatar">{t.initials}</div>
                <div>
                  <div className="testimonial-name">{t.name}</div>
                  <div className="testimonial-title">{t.title}</div>
                </div>
              </div>
            </div>
          ))}
        </div>

        <SectionDivider label={author.label} />
        <div className="author-card" style={{ marginTop: 32 }}>
          <div className="author-avatar">{author.initials}</div>
          <div>
            <div className="author-name">{author.name}</div>
            <div className="author-title">{author.title}</div>
            <p className="author-bio">{author.bio}</p>
          </div>
        </div>

        <div className="secondary-cta-block">
          <div className="secondary-cta-label">{secondaryCta.label}</div>
          <p className="secondary-cta-support">{secondaryCta.supporting}</p>
          <CtaForm
            inputPlaceholder={primaryCta.inputPlaceholder}
            buttonLabel={secondaryCta.buttonLabel}
            microcopy={primaryCta.microcopy}
            onSubmit={() => setSubmitted(true)}
            submitted={submitted}
            compact
          />
        </div>

      </div>
    </>
  );
}
