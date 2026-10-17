import os
import subprocess

# --- CONFIGURATION INITIALE ---
os.makedirs("articles", exist_ok=True)
os.makedirs("glossary", exist_ok=True)
index_path = "index.html"

OBJECTIF_FINANCIER = 10000
DATE_LIMITE = "31/12/2026"

print(f"🎯 [OUROBOROS] Démarrage de la session — Objectif : {OBJECTIF_FINANCIER} € d'ici le {DATE_LIMITE}")

# --- CATALOGUE DES PRODUITS GUMROAD ---
GUMROAD_TRILOGY = "https://unfreezepayments.gumroad.com/l/fintech-legal-trilogy"
GUMROAD_CONTINUITY = "https://unfreezepayments.gumroad.com/l/payment-continuity-protocol"
GUMROAD_STRIPE_AUDIT = "https://unfreezepayments.gumroad.com/l/stripe-compliance-audit-playbook"
GUMROAD_SURVIVAL = "https://unfreezepayments.gumroad.com/l/payment-survival-guide"

# --- 1. LES BRIEFINGS PRINCIPAUX (GRILLE 2X2) ---
articles_du_jour = [
    {
        "filename": "visa-vamp-2026-compliance-guide.html",
        "briefing_id": "BRIEFING #01",
        "title": "Visa VAMP 2026 Compliance & Risk Mitigation Guide",
        "desc": "Navigating thresholds, monitoring programs, dispute audits, and merchant risk mitigation.",
        "gumroad_link": GUMROAD_SURVIVAL,
        "gumroad_title": "Get The Payment Survival Guide ($59) →",
        "content_body": """
            <h2>1. Overview of Visa VAMP 2026 Updates</h2>
            <p>Visa System Integrity Monitoring Program (VAMP) imposes strict compliance thresholds on merchant chargebacks and fraud ratios. Failing to meet these metrics exposes high-risk merchants to immediate acquirer fines and processor termination.</p>
            <div class='callout'><b>Critical Metric:</b> Exceeding a 0.9% chargeback-to-transaction ratio for two consecutive cycles triggers automatic placement in the Visa Acquirer Monitoring Program.</div>
            <h2>2. Escalation & Dispute Strategy</h2>
            <p>Enforcing proper pre-arbitration protocols and submitting clear evidence of fulfillment are essential to contesting unfair acquirer holds.</p>
        """
    },
    {
        "filename": "mastercard-ancrm-chargeback-compliance.html",
        "briefing_id": "BRIEFING #02",
        "title": "Mastercard ANCRM & Chargeback Compliance",
        "desc": "Managing Acquirer Excessive Chargeback Programs, dispute audits, and reserve escrows.",
        "gumroad_link": GUMROAD_STRIPE_AUDIT,
        "gumroad_title": "Get The Stripe Compliance Audit Playbook ($59) →",
        "content_body": """
            <h2>1. ANCRM Tier 1 & Tier 2 Thresholds</h2>
            <p>Mastercard's Acquirer Excessive Chargeback Program (ECM) penalizes merchants exceeding acceptable dispute limits. Understanding the difference between Tier 1 and Tier 2 compliance is paramount to avoiding frozen merchant accounts (MIDs).</p>
            <div class='callout'><b>Escrow Protection:</b> Implementing legal notices prevents acquirers from holding reserve funds beyond contractual timeline limits.</div>
            <h2>2. Chargeback Reduction Framework</h2>
            <p>Deploying pre-dispute alert systems (Ethoca / Verifi RDR) reduces merchant dispute volume before it impacts card brand ratios.</p>
        """
    },
    {
        "filename": "multi-mid-failover-protocols.html",
        "briefing_id": "BRIEFING #03",
        "title": "Multi-MID Failover Protocols & Payment Continuity Architectures",
        "desc": "Engineering resilient payment routing systems to eliminate single points of failure and processor lock-in.",
        "gumroad_link": GUMROAD_CONTINUITY,
        "gumroad_title": "Get The Payment Continuity Protocol ($69) →",
        "content_body": """
            <h2>1. Redundant Routing & Gateway Architecture</h2>
            <p>Relying on a single payment gateway or MID exposes high-volume merchants to total operational shutdown when a freeze occurs. Multi-MID load balancing ensures continuous transaction routing.</p>
            <div class='callout'><b>99.98% Uptime Target:</b> Dynamic failover rules automatically reroute declined or blocked traffic to secondary acquiring banks.</div>
            <h2>2. Implementation Checklist</h2>
            <p>Cascading authorization, MID health checks, and tokenization synchronization across independent payment processors.</p>
        """
    },
    {
        "filename": "etude-cas-recouvrement-147k.html",
        "briefing_id": "BRIEFING #04",
        "title": "Étude de Cas : Récupération de 147 000 $ Bloqués sous UCC § 4A-502",
        "desc": "Retour d'expérience opérationnel et juridique sur la levée d'un gel de 180 jours.",
        "gumroad_link": GUMROAD_TRILOGY,
        "gumroad_title": "Access The Full Fintech Legal Trilogy ($149) →",
        "content_body": """
            <h2>1. Analyse de la Rétention Abusive</h2>
            <p>Étude détaillée d'un gel d'actifs de $147k par un processeur de paiement majeur sous motif de risque algorithmique préventif.</p>
            <div class='callout'><b>Action Légale :</b> Envoi d'une mise en demeure basée sur l'UCC § 4A-502 forçant l'examen manuel du dossier en 48h.</div>
            <h2>2. Déblocage et Transfert des Fonds</h2>
            <p>Méthodologie de restitution des réserves et mise en place d'un protocole d'arbitrage d'urgence.</p>
        """
    }
]

# --- 2. TERMES DU GLOSSAIRE JURIDIQUE & SEO (/glossary/) ---
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

# --- GENERATION DES ARTICLES PRINCIPAUX ---
for art in articles_du_jour:
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
            <h3 style="color: var(--gold-primary); margin-top: 0;">Recommended Playbook</h3>
            <p>Unlock the complete legal frameworks and step-by-step dispute execution templates.</p>
            <a href="{art['gumroad_link']}" class="btn" target="_blank">{art['gumroad_title']}</a>
        </div>
    </div>
</body>
</html>"""
    with open(art_path, "w", encoding="utf-8") as f:
        f.write(art_html)

# --- GENERATION DES PAGES DE GLOSSAIRE ---
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
        <p>In high-risk merchant environments, understanding this concept is critical to preventing sudden processing halts and preserving operating capital.</p>
        
        <div class="cta-box">
            <h3 style="color: var(--gold-primary); margin-top: 0;">Need Executive Implementation Frameworks?</h3>
            <p>Access ready-to-use legal documents, audit checklists, and failover architectures.</p>
            <a href="{entry['playbook_link']}" class="btn" target="_blank">{entry['playbook_text']}</a>
        </div>
    </div>
</body>
</html>"""
    with open(gloss_path, "w", encoding="utf-8") as f:
        f.write(gloss_html)

# --- CONSTRUCTEUR DE LA GRILLE D'ARTICLES ET DU GLOSSAIRE POUR INDEX.HTML ---
cards_html = ""
for art in articles_du_jour:
    cards_html += f"""
            <div class="briefing-card">
                <div>
                    <span class="briefing-tag">{art['briefing_id']}</span>
                    <a href="articles/{art['filename']}" class="briefing-title">{art['title']}</a>
                    <p class="briefing-desc">{art['desc']}</p>
                </div>
                <a href="articles/{art['filename']}" class="read-link">Read Briefing →</a>
            </div>"""

glossary_links_html = ""
for entry in glossary_terms:
    glossary_links_html += f'<li><a href="glossary/{entry["filename"]}" style="color: var(--gold-primary); text-decoration: none;">{entry["term"]}</a> — <span style="color: var(--text-muted); font-size: 0.85rem;">{entry["definition"][:80]}...</span></li>\n'

# --- REGENÉRATION DE INDEX.HTML ---
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

        .glossary-box {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 20px 30px;
            margin-top: 2rem;
        }}
        .glossary-box ul {{ padding-left: 20px; }}
        .glossary-box li {{ margin-bottom: 10px; }}

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

        <h2>Latest Technical Briefings</h2>
        <div class="briefings-grid">
{cards_html}
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
    </div>
</body>
</html>"""

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_full_html)

print(f"✅ [OUROBOROS] Succès ! 4 briefings + {len(glossary_terms)} pages de glossaire générées.")

# --- DEPLOIEMENT AUTOMATIQUE GITHUB ---
try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", f"Ouroboros Session: Added SEO Legal Glossary and enhanced internal linking (Target: {OBJECTIF_FINANCIER}E)"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("🚀 [OUROBOROS] Déploiement GitHub réussi !")
except Exception as e:
    print(f"⚠️ [OUROBOROS] Information Git : {e}")