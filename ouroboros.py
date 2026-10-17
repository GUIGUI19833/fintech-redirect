import os
import json
import subprocess

# --- CONFIGURATION INITIALE ---
os.makedirs("articles", exist_ok=True)
os.makedirs("glossary", exist_ok=True)
index_path = "index.html"
db_path = "articles_db.json"

OBJECTIF_FINANCIER = 10000
DATE_LIMITE = "31/12/2026"

print(f"🎯 [OUROBOROS] Démarrage — Stratégie de Teasing & Protection IP (Objectif : {OBJECTIF_FINANCIER} €)")

# --- CATALOGUE DES PRODUITS GUMROAD ---
GUMROAD_TRILOGY = "https://unfreezepayments.gumroad.com/l/fintech-legal-trilogy"
GUMROAD_CONTINUITY = "https://unfreezepayments.gumroad.com/l/payment-continuity-protocol"
GUMROAD_STRIPE_AUDIT = "https://unfreezepayments.gumroad.com/l/stripe-compliance-audit-playbook"
GUMROAD_SURVIVAL = "https://unfreezepayments.gumroad.com/l/payment-survival-guide"

# --- BANQUE DE SUJETS STRATÉGIQUES (TEASERS ISSUS DES OUVRAGES) ---
BANQUE_SUJETS = [
    {
        "filename": "5-precursor-signals-processor-termination.html",
        "briefing_id": "BRIEFING #01",
        "title": "The 5 Precursor Signals of Impending Merchant Termination",
        "desc": "Identify the hidden automated risk triggers before your payment processor freezes payouts.",
        "gumroad_link": GUMROAD_SURVIVAL,
        "gumroad_title": "Get The Payment Survival Guide ($59) →",
        "content_body": """
            <h2>1. Recognizing Algorithmic Risk Triggers</h2>
            <p>Payment processors deploy automated machine learning models that continuously recalculate merchant risk scores based on chargeback velocity, refund spikes, and fulfillment latency. Recognizing precursor signals—such as out-of-cycle KYC verification requests or sudden payout schedule shifts—allows merchants to execute pre-emptive mitigation before cash flow is seized[cite: 7, 27].</p>
            <div class='callout'><b>Operational Warning Window:</b> In over 80% of analyzed cases, merchants experience clear precursor signals 5 to 14 days prior to a total account freeze[cite: 28].</div>
            <h2>2. Why Frontline Support Fails</h2>
            <p>Standard merchant support tickets cannot override automated risk determinations. Reinstatement requires structured, objective compliance evidence[cite: 6]. <em>For the complete 15-document emergency underwriting checklist and direct escalation workflows, consult the full Survival Guide.</em></p>
        """
    },
    {
        "filename": "unlocking-frozen-funds-ucc-4a-502.html",
        "briefing_id": "BRIEFING #02",
        "title": "Unlocking Frozen Merchant Reserves Under UCC § 4A-502",
        "desc": "Legal and operational levers to contest arbitrary 180-day processor reserve retentions.",
        "gumroad_link": GUMROAD_TRILOGY,
        "gumroad_title": "Access The Fintech Legal Trilogy ($149) →",
        "content_body": """
            <h2>1. The Legal Limits of Reserve Retention</h2>
            <p>When processors terminate an account, they routinely freeze balances for 180 days under boilerplate clauses. However, under Uniform Commercial Code (UCC) § 4A-502 and common law principles, holding 100% of unencumbered funds when dispute ratios remain below network thresholds constitutes bad-faith retention[cite: 8].</p>
            <div class='callout'><b>The 30-Day Escalation Pathway:</b> Recovery success relies on structured progression through formal legal demand letters, regulatory complaints (CFPB/FCA), and binding arbitration[cite: 8, 33].</div>
            <h2>2. Executing Legal Leverage</h2>
            <p>Formal legal demands bypass standard support queues by engaging institutional compliance counsel[cite: 8]. <em>The exact legal demand letter templates, Small Claims strategies, and AAA arbitration frameworks are fully detailed in the Legal Trilogy.</em></p>
        """
    },
    {
        "filename": "multi-mid-redundancy-architecture.html",
        "briefing_id": "BRIEFING #03",
        "title": "Multi-MID Redundancy & Payment Continuity Architectures",
        "desc": "Eliminate single points of failure by distributing transaction volume across independent acquiring rails.",
        "gumroad_link": GUMROAD_CONTINUITY,
        "gumroad_title": "Get The Payment Continuity Protocol ($69) →",
        "content_body": """
            <h2>1. The Fragility of Single-Processor Models</h2>
            <p>Relying exclusively on a single payment facilitator creates total operational exposure[cite: 10, 45]. High-volume digital enterprises must deploy a resilient multi-processor architecture that distributes volume across independent acquiring banks and separate corporate entities[cite: 10, 45].</p>
            <div class='callout'><b>Uptime Benchmark:</b> Dual-MID load-balanced architectures achieve 99.98% operational uptime during sudden processor interruptions[cite: 10, 46].</div>
            <h2>2. Compliant Load Balancing Rules</h2>
            <p>Transaction routing must follow legitimate business segmentation (geography, product lines) rather than unapproved volume splitting designed to mask dispute ratios[cite: 10, 45]. <em>Step-by-step gateway routing specifications and multi-entity isolation blueprints are available in the Payment Continuity Protocol.</em></p>
        """
    },
    {
        "filename": "visa-vamp-mastercard-ancrm-2026.html",
        "briefing_id": "BRIEFING #04",
        "title": "Navigating Visa VAMP & Mastercard ANCRM 2026 Standards",
        "desc": "Essential compliance thresholds for dispute ratios, fraud monitoring, and acquirer audits.",
        "gumroad_link": GUMROAD_STRIPE_AUDIT,
        "gumroad_title": "Get The Stripe Compliance Audit Playbook ($59) →",
        "content_body": """
            <h2>1. Unified Card Network Thresholds</h2>
            <p>Card brands enforce strict compliance metrics. Visa VAMP consolidates dispute and fraud ratios under unified monitoring parameters, while Mastercard ANCRM penalizes excessive chargeback levels through escalating monthly assessments[cite: 18, 71].</p>
            <div class='callout'><b>Critical Metric:</b> Crossing a 0.75% to 0.9% dispute ratio triggers mandatory program placement and potential acquirer fines[cite: 7, 18, 60, 71].</div>
            <h2>2. Pre-Dispute Defense Systems</h2>
            <p>Deploying automated alert systems (Verifi RDR and Ethoca) intercepts disputes before formal chargeback conversion occurs[cite: 6, 7, 44]. <em>For complete audit preparation checklists and statement descriptor optimization blueprints, access the Stripe Compliance Playbook.</em></p>
        """
    }
]

# --- GESTION DE LA BASE DE DONNÉES LOCALE (ACCUMULATION) ---
if os.path.exists(db_path):
    with open(db_path, "r", encoding="utf-8") as f:
        articles_enregistres = json.load(f)
else:
    articles_enregistres = []

if not articles_enregistres:
    articles_enregistres = BANQUE_SUJETS[:4]
    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(articles_enregistres, f, indent=4)

# Accumulation automatique du prochain sujet s'il en reste dans la banque
filenames_actuels = [a["filename"] for a in articles_enregistres]
for sujet in BANQUE_SUJETS:
    if sujet["filename"] not in filenames_actuels:
        articles_enregistres.append(sujet)
        print(f"➕ [OUROBOROS] Nouvel article-teaser accumulé : {sujet['title']}")
        break

with open(db_path, "w", encoding="utf-8") as f:
    json.dump(articles_enregistres, f, indent=4)

# --- DISCLAIMER JURIDIQUE GLOBAL ---
LEGAL_DISCLAIMER = """
    <footer style="margin-top: 4rem; padding: 2rem 0; border-top: 1px solid var(--border-color); text-align: center; font-size: 0.75rem; color: var(--text-muted); line-height: 1.5;">
        <p><b>Legal Disclaimer:</b> The content provided on UnfreezeStripe Advisory is for informational and educational purposes only and does not constitute formal legal, financial, or regulatory advice. High-risk merchant processing, account freezes, and chargeback mitigation involve complex legal frameworks (including UCC and card brand rules). Always consult with qualified legal counsel or licensed financial professionals before initiating legal disputes or altering payment architectures.</p>
        <p>© 2026 UnfreezeStripe Advisory Hub. All rights reserved. Target: 10,000€ by 31/12/2026.</p>
    </footer>
"""

# Glossaire SEO inchangé pour le maillage
glossary_terms = [
    {
        "filename": "ucc-4a-502-funds-freeze.html",
        "term": "UCC § 4A-502 & Creditor Process",
        "definition": "Legal framework governing fund transfers and restraining orders against financial intermediaries to contest unlawful merchant account freezes.",
        "playbook_link": GUMROAD_TRILOGY,
        "playbook_text": "Get the UCC Dispute Templates in the Legal Trilogy ($149) →"
    },
    {
        "filename": "rolling-reserve-mitigation.html",
        "term": "Rolling Reserve Ratio & Escrow Release",
        "definition": "Mechanisms used by payment processors to withhold a percentage of transactions. Strategies to legally cap and release escrow funds.",
        "playbook_link": GUMROAD_STRIPE_AUDIT,
        "playbook_text": "Learn audit defense in the Stripe Compliance Playbook ($59) →"
    },
    {
        "filename": "visa-vamp-monitoring.html",
        "term": "Visa VAMP (Visa Acquirer Monitoring Program)",
        "definition": "Card brand compliance program monitoring excessive fraud and dispute rates, carrying severe non-compliance acquirer penalties.",
        "playbook_link": GUMROAD_SURVIVAL,
        "playbook_text": "Read mitigation steps in the Payment Survival Guide ($59) →"
    },
    {
        "filename": "multi-mid-redundancy.html",
        "term": "Multi-MID Redundancy & Load Balancing",
        "definition": "Payment architecture distributing transaction volume across multiple Merchant IDs to ensure 99.98% uptime against sudden terminations.",
        "playbook_link": GUMROAD_CONTINUITY,
        "playbook_text": "Build redundant routing with the Payment Continuity Protocol ($69) →"
    }
]

# --- GÉNÉRATION DES ARTICLES ---
for art in articles_enregistres:
    art_path = os.path.join("articles", art["filename"])
    art_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{art['title']} | UnfreezeStripe Advisory</title>
    <meta name="description" content="{art['desc']}">
    <style>
        :root {{
            --bg-dark: #0a0c10;
            --card-bg: #12161f;
            --gold-primary: #d4af37;
            --text-main: #e6edf3;
            --text-muted: #8b949e;
            --border-gold: rgba(212, 175, 55, 0.3);
            --border-color: #30363d;
        }}
        body {{
            background-color: var(--bg-dark);
            color: var(--text-main);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            margin: 0; padding: 0; line-height: 1.7;
        }}
        .container {{ max-width: 800px; margin: 0 auto; padding: 3rem 1.5rem; }}
        a.back-link {{ color: var(--gold-primary); text-decoration: none; font-weight: bold; font-size: 0.9rem; }}
        a.back-link:hover {{ text-decoration: underline; }}
        .tag {{ color: var(--gold-primary); font-size: 0.8rem; font-weight: bold; letter-spacing: 1px; margin-top: 1.5rem; display: block; }}
        h1 {{ color: var(--gold-primary); font-size: 2.2rem; margin-top: 0.5rem; border-bottom: 1px solid var(--border-color); padding-bottom: 12px; }}
        .callout {{ background: var(--card-bg); border-left: 4px solid var(--gold-primary); padding: 18px; margin: 20px 0; border-radius: 0 6px 6px 0; }}
        .cta-box {{
            background: var(--card-bg);
            border: 2px solid var(--gold-primary);
            padding: 30px;
            border-radius: 10px;
            text-align: center;
            margin: 3.5rem 0;
        }}
        .btn {{
            display: inline-block;
            background: linear-gradient(135deg, #d4af37 0%, #aa820a 100%);
            color: #000;
            font-weight: bold;
            padding: 12px 25px;
            border-radius: 6px;
            text-decoration: none;
            margin-top: 15px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <a href="../index.html" class="back-link">← Return to Gateway Hub</a>
        <span class="tag">{art['briefing_id']}</span>
        <h1>{art['title']}</h1>
        <p><i>{art['desc']}</i></p>
        <hr style="border-color: var(--border-color); margin: 2rem 0;">
        
        {art['content_body']}

        <div class="cta-box">
            <h3 style="color: var(--gold-primary); margin-top: 0;">Unlock Full Legal Templates & Protocols</h3>
            <p>Access ready-to-use demand letters, step-by-step dispute escalation frameworks, and institutional audit checklists.</p>
            <a href="{art['gumroad_link']}" class="btn" target="_blank">{art['gumroad_title']}</a>
        </div>
        
        {LEGAL_DISCLAIMER}
    </div>
</body>
</html>"""
    with open(art_path, "w", encoding="utf-8") as f:
        f.write(art_html)

# --- GÉNÉRATION DU GLOSSAIRE ---
for entry in glossary_terms:
    gloss_path = os.path.join("glossary", entry["filename"])
    gloss_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{entry['term']} | Fintech Legal Glossary</title>
    <meta name="description" content="{entry['definition']}">
    <style>
        :root {{
            --bg-dark: #0a0c10;
            --card-bg: #12161f;
            --gold-primary: #d4af37;
            --text-main: #e6edf3;
            --text-muted: #8b949e;
            --border-gold: rgba(212, 175, 55, 0.3);
            --border-color: #30363d;
        }}
        body {{
            background-color: var(--bg-dark);
            color: var(--text-main);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            margin: 0; padding: 0; line-height: 1.7;
        }}
        .container {{ max-width: 800px; margin: 0 auto; padding: 3rem 1.5rem; }}
        a.back-link {{ color: var(--gold-primary); text-decoration: none; font-weight: bold; font-size: 0.9rem; }}
        a.back-link:hover {{ text-decoration: underline; }}
        h1 {{ color: var(--gold-primary); font-size: 2rem; border-bottom: 1px solid var(--border-color); padding-bottom: 12px; }}
        .def-box {{ background: var(--card-bg); border: 1px solid var(--border-color); padding: 25px; border-radius: 8px; margin: 25px 0; }}
        .cta-box {{ background: var(--card-bg); border: 2px solid var(--gold-primary); padding: 30px; border-radius: 10px; text-align: center; margin: 3.5rem 0; }}
        .btn {{ display: inline-block; background: linear-gradient(135deg, #d4af37 0%, #aa820a 100%); color: #000; font-weight: bold; padding: 12px 25px; border-radius: 6px; text-decoration: none; margin-top: 15px; }}
    </style>
</head>
<body>
    <div class="container">
        <a href="../index.html" class="back-link">← Return to Gateway Hub</a>
        <h1>{entry['term']}</h1>
        <div class="def-box">
            <p style="color: var(--text-main); font-size: 1.1rem; margin: 0;"><b>Institutional Definition:</b> {entry['definition']}</p>
        </div>
        <p>Understanding this compliance standard is vital to preventing sudden processing interruptions and safeguarding operating capital.</p>
        
        <div class="cta-box">
            <h3 style="color: var(--gold-primary); margin-top: 0;">Access Complete Executive Frameworks</h3>
            <p>Get ready-to-use audit defenses, legal templates, and gateway resilience architectures.</p>
            <a href="{entry['playbook_link']}" class="btn" target="_blank">{entry['playbook_text']}</a>
        </div>
        
        {LEGAL_DISCLAIMER}
    </div>
</body>
</html>"""
    with open(gloss_path, "w", encoding="utf-8") as f:
        f.write(gloss_html)

# --- GÉNÉRATION DE L'INDEX ---
derniers_articles = articles_enregistres[-4:]
cards_html = ""
for art in derniers_articles:
    cards_html += f"""
            <div class="briefing-card">
                <div>
                    <span class="briefing-tag">{art['briefing_id']}</span>
                    <a href="articles/{art['filename']}" class="briefing-title">{art['title']}</a>
                    <p class="briefing-desc">{art['desc']}</p>
                </div>
                <a href="articles/{art['filename']}" class="read-link">Read Briefing →</a>
            </div>"""

archives_html = ""
for art in articles_enregistres:
    archives_html += f'<li><a href="articles/{art["filename"]}" style="color: var(--gold-primary); text-decoration: none;"><b>{art["briefing_id"]}</b> — {art["title"]}</a></li>\n'

glossary_links_html = ""
for entry in glossary_terms:
    glossary_links_html += f'<li><a href="glossary/{entry["filename"]}" style="color: var(--gold-primary); text-decoration: none;">{entry["term"]}</a> — <span style="color: var(--text-muted); font-size: 0.85rem;">{entry["definition"][:80]}...</span></li>\n'

index_full_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UnfreezeStripe | Institutional Fintech Risk Advisory</title>
    <meta name="description" content="Enterprise-grade compliance frameworks, legal escalation playbooks, and multi-MID routing protocols.">
    <style>
        :root {{
            --bg-dark: #0a0c10;
            --card-bg: #12161f;
            --gold-primary: #d4af37;
            --text-main: #e6edf3;
            --text-muted: #8b949e;
            --border-gold: rgba(212, 175, 55, 0.3);
            --accent-blue: #58a6ff;
            --border-color: #30363d;
            --danger-red: #f85149;
            --safe-green: #2ea043;
        }}
        body {{
            background-color: var(--bg-dark);
            color: var(--text-main);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            margin: 0; padding: 0; line-height: 1.6;
        }}
        header {{
            border-bottom: 1px solid var(--border-gold);
            padding: 2.5rem 1rem;
            text-align: center;
            background: linear-gradient(180deg, rgba(212, 175, 55, 0.08) 0%, rgba(10, 12, 16, 1) 100%);
        }}
        .container {{ max-width: 1100px; margin: 0 auto; padding: 2rem 1rem; }}
        h1 {{ color: var(--gold-primary); font-size: 2.1rem; margin-bottom: 0.5rem; }}
        h2 {{ color: var(--gold-primary); font-size: 1.5rem; margin-top: 2.5rem; border-bottom: 1px solid var(--border-color); padding-bottom: 8px; }}
        p {{ color: var(--text-muted); }}
        .hero-banner {{ text-align: center; margin: 2rem 0; }}
        .hero-banner img {{ max-width: 100%; height: auto; border-radius: 8px; border: 1px solid var(--border-gold); }}
        .briefings-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
            margin-top: 1.5rem;
        }}
        @media (max-width: 768px) {{ .briefings-grid {{ grid-template-columns: 1fr; }} }}
        .briefing-card {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 22px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}
        .briefing-card:hover {{ border-color: var(--gold-primary); }}
        .briefing-tag {{ color: var(--gold-primary); font-weight: bold; font-size: 0.75rem; letter-spacing: 1px; margin-bottom: 8px; display: block; }}
        .briefing-title {{ color: var(--text-main); font-size: 1.05rem; font-weight: bold; text-decoration: none; margin-bottom: 10px; display: block; }}
        .briefing-title:hover {{ color: var(--gold-primary); }}
        .briefing-desc {{ color: var(--text-muted); font-size: 0.85rem; margin-bottom: 15px; }}
        .read-link {{ color: var(--accent-blue); font-size: 0.85rem; font-weight: 500; text-decoration: none; }}
        .read-link:hover {{ text-decoration: underline; }}
        .calc-box {{
            background: var(--card-bg);
            border: 2px solid var(--gold-primary);
            border-radius: 10px;
            padding: 30px;
            margin-top: 2.5rem;
        }}
        .calc-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-top: 20px;
        }}
        @media (max-width: 768px) {{ .calc-grid {{ grid-template-columns: 1fr; }} }}
        .input-group {{ margin-bottom: 15px; }}
        .input-group label {{ display: block; color: var(--text-main); font-size: 0.9rem; margin-bottom: 6px; font-weight: 500; }}
        .input-group input {{
            width: 100%;
            background: #0a0c10;
            border: 1px solid var(--border-color);
            color: var(--text-main);
            padding: 10px;
            border-radius: 6px;
            font-size: 1rem;
            box-sizing: border-box;
        }}
        .input-group input:focus {{ border-color: var(--gold-primary); outline: none; }}
        .calc-result {{
            background: #0a0c10;
            border: 1px solid var(--border-color);
            padding: 20px;
            border-radius: 8px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            text-align: center;
        }}
        .metric-value {{ font-size: 2rem; font-weight: bold; margin: 10px 0; }}
        .status-safe {{ color: var(--safe-green); }}
        .status-danger {{ color: var(--danger-red); }}
        .archives-box, .glossary-box {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 20px 30px;
            margin-top: 2rem;
        }}
        .archives-box ul, .glossary-box ul {{ padding-left: 20px; }}
        .archives-box li, .glossary-box li {{ margin-bottom: 10px; }}
        .cta-box {{
            background: var(--card-bg);
            border: 2px solid var(--gold-primary);
            padding: 30px;
            border-radius: 10px;
            text-align: center;
            margin: 3.5rem 0;
        }}
        .btn {{
            display: inline-block;
            background: linear-gradient(135deg, #d4af37 0%, #aa820a 100%);
            color: #000;
            font-weight: bold;
            padding: 12px 25px;
            border-radius: 6px;
            text-decoration: none;
            margin-top: 15px;
        }}
    </style>
</head>
<body>
    <header>
        <h1>Fintech Redirect & Institutional Payment Continuity Gateway</h1>
        <p>Enterprise-grade compliance frameworks, legal escalation playbooks, and multi-MID routing protocols. (Target: {OBJECTIF_FINANCIER}€ by {DATE_LIMITE})</p>
    </header>

    <div class="container">
        <div class="hero-banner">
            <img src="images/banner.jpg" alt="Dark Gold Fintech Payment Continuity" onerror="this.src='banner.jpg'">
        </div>

        <h2>Latest Technical Briefings (Featured)</h2>
        <div class="briefings-grid">
{cards_html}
        </div>

        <!-- CALCULATEUR DE RISQUE -->
        <div class="calc-box">
            <span style="color: var(--gold-primary); font-weight: bold; font-size: 0.75rem; letter-spacing: 1px; display: block; margin-bottom: 5px;">INTERACTIVE TOOL</span>
            <h2 style="margin-top: 0; border: none; padding: 0;">Visa VAMP & Chargeback Risk Calculator</h2>
            <p>Input your monthly processing metrics to evaluate your standing against 2026 card brand monitoring thresholds.</p>
            
            <div class="calc-grid">
                <div>
                    <div class="input-group">
                        <label for="txCount">Monthly Transactions Count:</label>
                        <input type="number" id="txCount" value="5000" min="1" oninput="calculateRisk()">
                    </div>
                    <div class="input-group">
                        <label for="cbCount">Monthly Chargebacks Count:</label>
                        <input type="number" id="cbCount" value="35" min="0" oninput="calculateRisk()">
                    </div>
                </div>
                <div class="calc-result">
                    <span style="color: var(--text-muted); font-size: 0.85rem;">Estimated Dispute Ratio</span>
                    <div id="ratioDisplay" class="metric-value">0.70%</div>
                    <div id="statusDisplay" style="font-size: 0.9rem; font-weight: bold;" class="status-safe">Safe Standing (Below 0.9%)</div>
                </div>
            </div>
            
            <div id="ctaContainer" style="margin-top: 20px; text-align: center; display: none;">
                <p id="ctaText" style="color: var(--danger-red); font-weight: bold; margin-bottom: 10px;">⚠️ Warning: You exceed Visa VAMP thresholds. Immediate mitigation required.</p>
                <a id="ctaButton" href="{GUMROAD_SURVIVAL}" class="btn" target="_blank">Get The Payment Survival Guide ($59) →</a>
            </div>
        </div>

        <h2>All Technical Briefings & Archives</h2>
        <div class="archives-box">
            <ul>
{archives_html}
            </ul>
        </div>

        <h2>Institutional Glossary & Legal References</h2>
        <div class="glossary-box">
            <ul>
{glossary_links_html}
            </ul>
        </div>

        <div class="cta-box">
            <h3 style="color: var(--gold-primary); margin-top: 0;">The Fintech Legal Trilogy & Master Playbooks</h3>
            <p>Access complete legal frameworks, UCC § 4A-502 templates, arbitration demands, and institutional risk recovery guides.</p>
            <a href="{GUMROAD_TRILOGY}" class="btn" target="_blank">Access The Full Trilogy on Gumroad →</a>
        </div>

        {LEGAL_DISCLAIMER}
    </div>

    <script>
        function calculateRisk() {{
            const tx = parseFloat(document.getElementById('txCount').value) || 1;
            const cb = parseFloat(document.getElementById('cbCount').value) || 0;
            const ratio = (cb / tx) * 100;
            
            const ratioDisplay = document.getElementById('ratioDisplay');
            const statusDisplay = document.getElementById('statusDisplay');
            const ctaContainer = document.getElementById('ctaContainer');
            
            ratioDisplay.innerText = ratio.toFixed(2) + '%';
            
            if (ratio >= 0.9) {{
                statusDisplay.innerText = 'CRITICAL: VAMP Threshold Exceeded (>0.9%)';
                statusDisplay.className = 'metric-value status-danger';
                statusDisplay.style.fontSize = '1.1rem';
                ctaContainer.style.display = 'block';
            }} else if (ratio >= 0.65) {{
                statusDisplay.innerText = 'WARNING: High Risk / Watchlist Zone';
                statusDisplay.className = 'metric-value';
                statusDisplay.style.color = '#d4af37';
                statusDisplay.style.fontSize = '1.1rem';
                ctaContainer.style.display = 'block';
            }} else {{
                statusDisplay.innerText = 'Safe Standing (Below 0.9%)';
                statusDisplay.className = 'status-safe';
                statusDisplay.style.fontSize = '0.9rem';
                ctaContainer.style.display = 'none';
            }}
        }}
        calculateRisk();
    </script>
</body>
</html>"""

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_full_html)

print(f"✅ [OUROBOROS] Succès ! Teasers stratégiques générés et index mis à jour.")

# --- DÉPLOIEMENT GIT ---
try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", f"Ouroboros Teaser Strategy: High-value IP protected, Gumroad funnels active (Target: {OBJECTIF_FINANCIER}E)"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("🚀 [OUROBOROS] Déploiement GitHub réussi avec les teasers de conversion !")
except Exception as e:
    print(f"⚠️ [OUROBOROS] Info Git : {e}")