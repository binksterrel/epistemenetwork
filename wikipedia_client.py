import wikipediaapi
from typing import Optional
from config import WIKIPEDIA_LANGUAGE

class WikipediaClient:
    def __init__(self):
        # User-Agent requis par Wikipedia API
        self.wiki = wikipediaapi.Wikipedia(
            user_agent='StudentGraphProject/1.0 (contact@example.university.edu)',
            language=WIKIPEDIA_LANGUAGE
        )
    
    def get_scientist_text(self, name: str) -> tuple[Optional[str], list]:
        """
        Récupère le texte Wikipedia d'un scientifique.
        Retourne le résumé + début du contenu pour ne pas surcharger le LLM.
        """
        page = self.wiki.page(name)
        
        if not page.exists():
            return None
            
        # On construit un texte riche mais concis
        # 1. Le résumé est crucial (contient souvent les dates, nationalité, domaine)
        content = f"Titre: {page.title}\n\nRésumé:\n{page.summary}\n\n"
        
        # 2. On ajoute les 25000 premiers caractères (compromis Vitesse/Exhaustivité)
        # Lire tout le texte est trop lent et cause des timeouts.
        content += f"Détails:\n{page.text[:25000]}"
        
        # 3. Récupérer les liens (c'est très utile pour aider le LLM à identifier les noms corrects)
        links = list(page.links.keys())[:300]
        
        return content, links
    
    def page_exists(self, name: str) -> bool:
        """Vérifie si une page existe pour ce nom."""
        return self.wiki.page(name).exists()
