import os
import time
import google.generativeai as genai

# Clé API
GOOGLE_API_KEY = "AIzaSyBppJaowyE-pFj53k5kKMGu_uAQkMdRq14"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.5-pro')

# Dossier pour sauvegarder les articles
articles_dir = "articles"
os.makedirs(articles_dir, exist_ok=True)


# Données
questions_pinterest = [
    "c'est quoi pinterest ?",
    "pinterest c'est quoi ?",
    "a quoi sert pinterest ?",
    "comment poster sur pinterest ?",
    "comment fonctionne pinterest ?",
    "comment supprimer un compte pinterest ?",
    "comment utiliser pinterest ?",
    "pinterest est-il dangereux ?",
    "comment gagner de l'argent sur pinterest ?",
    "qu'est ce que pinterest ?"
]

keyword_pinterest = [
    "pinterest", "pinterest downloader", "pinterest noel", "pinterest video downloader",
    "pinterest cuisine", "pinterest français", "pinterest se connecter", "telecharger video pinterest",
    "pinterest download", "pinterest image", "pinterest fr", "Sign up", "logo pinterest",
    "pinterest france", "pinterest deco", "pinterest mon compte", "pinterest gratuit",
    "pinterest logo", "pinterest dessin", "image pinterest", "download pinterest video"
]

# Génération et sauvegarde
for i, question in enumerate(questions_pinterest):
    prompt = f"""
Écris un article de blog long, structuré et optimisé pour le SEO en répondant à la question suivante : "{question}"

L’article doit :
- Contenir au moins 1500 mots
- Être rédigé en français avec un ton clair et informatif
- Inclure les mots-clés suivants de façon naturelle et stratégique : {", ".join(keyword_pinterest)}
- Être bien structuré avec des balises H2/H3, des paragraphes courts et des listes si nécessaire
- Inclure une introduction, des sections explicatives et une conclusion
- Être optimisé pour le référencement Google

Commence maintenant.
"""
    try:
        print(f"⏳ Génération de l'article {i+1} : {question}")
        response = model.generate_content(prompt)
        article_text = response.text

        # Nettoyer le nom de fichier
        filename = f"article_{i+1}_{question[:40].replace(' ', '_').replace('?', '')}.md"
        filepath = os.path.join(articles_dir, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(article_text)

        print(f"✅ Article sauvegardé : {filepath}")
        time.sleep(3)  # Évite les limites d'API

    except Exception as e:
        print(f"❌ Erreur pour la question '{question}': {e}")