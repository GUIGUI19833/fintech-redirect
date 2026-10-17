import os
import datetime
import subprocess

os.makedirs("articles", exist_ok=True)
index_path = "index.html"
gumroad_url = "https://unfreezepayments.gumroad.com/l/fintech-legal-trilogy"

# Objectif financier de l'exercice
OBJECTIF_FINANCIER = 10000
DATE_LIMITE = "31/12/2026"

print(f"🎯 [OUROBOROS] Démarrage de la session - Objectif : {OBJECTIF_FINANCIER} € d'ici le {DATE_LIMITE}")

articles_du_jour = [
    {
        "filename": "recours-legal-fonds-geles-ucc-4a-502.html",
        "title": "Fonds bloqués par Stripe ou PayPal : Activer le recours UCC § 4A-502 en 48h",
        "briefing_id": "INSTITUTIONAL BRIEFING #01",
        "subtitle": "Guide juridique pour contester les rétentions abusives de trésorerie",
        "focus": "UCC § 4A-502, Demandes formelles, Déblocage de réserves",
        "content_html": "<p>Contestation formelle des rétentions abusives sous le cadre de l'UCC Article 4A pour accélérer les flux de trésorerie vers l'objectif de l'exercice.</p>"
    },
    {
        "filename": "mastercard-ancrm-chargeback-compliance.html",
        "title": "Mastercard ANCRM Compliance & Excessive Chargeback Mitigation (2026 Rules)",
        "briefing_id": "INSTITUTIONAL BRIEFING #02",
        "subtitle": "Navigating Acquirer Excessive Chargeback Programs & Reserve Escrows",
        "focus": "Mastercard Tier 1/2 Thresholds, Dispute Audits, Reserve Escalations",
        "content_html": "<p>Analyse des seuils ANCRM et des programmes de surveillance pour protéger le chiffre d'affaires des pénalités.</p>"
    },
    {
        "filename": "multi-mid-failover-protocols.html",
        "title": "Architecture Multi-MID et Failover : Garantir 99.98% de temps de fonctionnement",
        "briefing_id": "INSTITUTIONAL BRIEFING #03",
        "subtitle": "Stratégies d'ingénierie des risques pour la continuité des paiements",
        "focus": "Routage dynamique, Redondance des passerelles, Load-balancing",
        "content_html": "<p>Mise en place d'une architecture multi-acquéreur pour éliminer les interruptions de paiement et sécuriser les encaissements.</p>"
    },
    {
        "filename": "etude-cas-recouvrement-147k.html",
        "title": "Étude de cas : Récupération de 147 000 $ bloqués en réserve sous 41 jours",
        "briefing_id": "INSTITUTIONAL BRIEFING #04",
        "subtitle": "Retour d'expérience opérationnel sur la levée d'un gel de 180 jours",
        "focus": "Cas Pratiques, Croissance rapide, Preuves de fulfillment",
        "content_html": "<p>Retour d'expérience chiffré sur le déblocage rapide de réserves de 180 jours pour alimenter la trésorerie opérationnelle.</p>"
    }
]

dark_gold_css = "body { background-color: #0a0c10; color: #e6edf3; font-family: sans-serif; padding: 40px; max-width: 800px; margin: auto; line-height: 1.6; } h1 { color: #d4af37; }"

if os.path.exists(index_path):
    with open(index_path, "r", encoding="utf-8") as f:
        index_content = f.read()
else:
    index_content = '<ul class="article-list" id="seo-briefings-list"></ul>'

for item in articles_du_jour:
    article_path = os.path.join("articles", item["filename"])
    article_html = f"<!DOCTYPE html><html lang='fr'><head><meta charset='UTF-8'><title>{item['title']}</title><style>{dark_gold_css}</style></head><body><a href='../index.html'>← Retour</a><h1>{item['title']}</h1>{item['content_html']}<br><a href='{gumroad_url}'><b>Obtenir la Trilogy sur Gumroad (Objectif {OBJECTIF_FINANCIER}€) →</b></a></body></html>"
    
    with open(article_path, "w", encoding="utf-8") as f:
        f.write(article_html)
    
    new_entry = f'<li><a href="articles/{item["filename"]}">{item["title"]}</a> (Objectif {OBJECTIF_FINANCIER}€)</li>'
    if item['filename'] not in index_content and '<ul class="article-list" id="seo-briefings-list">' in index_content:
        index_content = index_content.replace('<ul class="article-list" id="seo-briefings-list">', f'<ul class="article-list" id="seo-briefings-list">\n{new_entry}')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_content)

print(f"[Ouroboros] Succès ! 4 articles générés, index mis à jour pour l'objectif de {OBJECTIF_FINANCIER}€.")

try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", f"Ouroboros Session: 4 new briefings (Target: {OBJECTIF_FINANCIER}E)"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("[Ouroboros] 🚀 Déploiement GitHub réussi !")
except Exception as e:
    print(f"[Ouroboros] Git info : {e}")