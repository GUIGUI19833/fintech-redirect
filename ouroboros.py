import os
from google import genai

# Récupération de la clé API
API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    print("❌ Erreur : La variable GEMINI_API_KEY n'est pas configurée.")
    exit(1)

# Initialisation du client moderne Google GenAI
client = genai.Client(api_key=API_KEY)

# Lecture des directives depuis GOALS.md
goals_content = ""
if os.path.exists("GOALS.md"):
    with open("GOALS.md", "r", encoding="utf-8") as f:
        goals_content = f.read()

prompt = f"""
Based on the following strategy directives, write 1 complete, highly detailed SEO technical article in Markdown.

DIRECTIVES:
{goals_content}

REQUIREMENTS:
- Written entirely in high-converting B2B English.
- Include a compelling title, problem breakdown, action steps, CTA linking to appropriate Gumroad guides, and the mandatory legal disclaimer at the bottom.
"""

print("🤖 Ouroboros s'éveille et consulte GOALS.md...")
print("📝 Génération de l'article SEO en cours via gemini-3.8-flash...")

try:
    # Utilisation du modèle recommandé gemini-3.8-flash
    response = client.models.generate_content(
        model='gemini-3.8-flash',
        contents=prompt,
    )
    article = response.text
    
    # Sauvegarde de l'article dans un fichier Markdown
    filename = "latest_article.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(article)
        
    print(f"\n✅ Succès ! Article généré avec succès dans '{filename}'.")
except Exception as e:
    print(f"\n❌ Erreur lors de l'exécution : {e}")