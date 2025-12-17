import os

def generate_slides():
    # Configuration des couleurs (Thème "Clean" du projet - Light Mode)
    colors = {
        "bg": "bg-[#FAFAFA]",            # Fond blanc cassé comme visualizer.py
        "text_main": "text-[#0A0A0A]",   # Texte presque noir
        "text_muted": "text-[#6A6A6A]",  # Gris moyen pour les détails
        "card_bg": "bg-white/80",        # Glassmorphism blanc
        "accent": "text-blue-600",
        "border": "border-gray-200"
    }

    html_content = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Présentation - Réseau Scientifique</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;800&display=swap" rel="stylesheet">
        <style>
            body {{ font-family: 'Inter', sans-serif; }}
            .slide {{
                height: 100vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                scroll-snap-align: start;
                padding: 2rem;
                position: relative;
            }}
            .container {{
                scroll-snap-type: y mandatory;
                overflow-y: scroll;
                height: 100vh;
            }}
            .glass {{
                background: rgba(255, 255, 255, 0.8);
                backdrop-filter: blur(20px);
                border: 1px solid rgba(0, 0, 0, 0.05);
                box-shadow: 0 10px 40px rgba(0,0,0,0.05);
            }}
            .gradient-text {{
                background: linear-gradient(135deg, #111827 0%, #4B5563 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }}
        </style>
    </head>
    <body class="{colors['bg']} {colors['text_main']} overflow-hidden">

        <!-- Arrière-plan subtil (noeuds flous) -->
        <div class="fixed inset-0 pointer-events-none opacity-30 z-0">
            <div class="absolute top-20 left-20 w-64 h-64 bg-blue-200 rounded-full mix-blend-multiply filter blur-3xl animate-blob"></div>
            <div class="absolute top-20 right-20 w-64 h-64 bg-purple-200 rounded-full mix-blend-multiply filter blur-3xl animate-blob animation-delay-2000"></div>
            <div class="absolute bottom-20 left-1/3 w-64 h-64 bg-pink-200 rounded-full mix-blend-multiply filter blur-3xl animate-blob animation-delay-4000"></div>
        </div>

        <div class="container no-scrollbar relative z-10">
            
            <!-- SLIDE 1 : TITRE & MEMBRES -->
            <section class="slide">
                <div class="max-w-4xl w-full text-center space-y-8">
                    <!-- Logo / Icone -->
                    <div class="inline-flex items-center justify-center w-20 h-20 rounded-2xl bg-white shadow-xl mb-6">
                        <span class="text-4xl">🔬</span>
                    </div>

                    <h1 class="text-6xl font-extrabold tracking-tight text-slate-900">
                        RÉSEAU SCIENTIFIQUE <br> Scientifique
                    </h1>
                    
                    <div class="w-24 h-1 bg-gradient-to-r from-blue-500 to-purple-500 mx-auto rounded-full"></div>

                    <p class="text-xl {colors['text_muted']} font-medium uppercase tracking-widest pt-4">
                        Projet Graphe & Open Data - L3 MIASHS
                    </p>
                    
                    <div class="pt-12">
                        <div class="glass px-10 py-6 rounded-2xl inline-block transform hover:scale-105 transition duration-300">
                            <span class="text-xs font-bold text-slate-400 uppercase tracking-wider block mb-2">Réalisé par</span>
                            <div class="text-2xl font-bold text-slate-800">
                                Terrel NUENTSA
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SLIDE 2 : IDÉE, ENTITÉS, RELATIONS -->
            <section class="slide">
                <div class="max-w-4xl w-full flex flex-col items-center gap-12 text-center">
                    
                    <!-- Texte -->
                    <div class="space-y-6">
                        <h2 class="text-5xl font-bold text-slate-900">Le Concept</h2>
                        <p class="text-xl leading-relaxed text-slate-600">
                            L'histoire des sciences n'est pas une ligne droite, mais un <strong class="text-blue-600">tissu complexe</strong>.
                        </p>
                        <p class="text-lg text-slate-500">
                            Notre objectif : cartographier dynamiquement comment les idées voyagent d'un cerveau à l'autre à travers les siècles.
                        </p>
                    </div>

                    <!-- Cartes (côte à côte si possible, ou empilées) -->
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 w-full">
                        
                        <!-- Card: Entités -->
                        <div class="glass p-8 rounded-2xl border-t-4 border-blue-500">
                            <div class="flex flex-col items-center gap-4">
                                <div class="bg-blue-50 p-4 rounded-full text-blue-600 mb-2">
                                    <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
                                </div>
                                <div>
                                    <h3 class="text-2xl font-bold text-slate-800">Les Entités</h3>
                                    <p class="text-slate-500 mt-2 text-sm">Scientifiques, mathématiciens & philosophes.</p>
                                </div>
                            </div>
                            <div class="mt-6 inline-block px-3 py-1 bg-slate-100 rounded-full text-xs font-mono text-slate-500">Nœuds (Nodes)</div>
                        </div>

                        <!-- Card: Relations -->
                        <div class="glass p-8 rounded-2xl border-t-4 border-purple-500">
                            <div class="flex flex-col items-center gap-4">
                                <div class="bg-purple-50 p-4 rounded-full text-purple-600 mb-2">
                                    <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg>
                                </div>
                                <div>
                                    <h3 class="text-2xl font-bold text-slate-800">Les Relations</h3>
                                    <p class="text-slate-500 mt-2 text-sm">Influences intellectuelles directes extraites des biographies.</p>
                                </div>
                            </div>
                            <div class="mt-6 inline-block px-3 py-1 bg-slate-100 rounded-full text-xs font-mono text-slate-500">Arêtes (Edges) A → B</div>
                        </div>

                    </div>
                </div>
            </section>

            <!-- SLIDE 3 : DONNÉES & QUESTIONS -->
            <section class="slide">
                <div class="max-w-4xl w-full flex flex-col items-center gap-12 text-center">
                    <div class="mb-4">
                        <h2 class="text-4xl font-bold text-slate-900">Analyse & Données</h2>
                    </div>
                    
                    <div class="flex flex-col w-full gap-8">
                        
                        <!-- Col 1: Données (Centré) -->
                        <div class="glass p-8 rounded-2xl w-full flex flex-col items-center">
                            <h3 class="text-xl font-bold mb-6 flex items-center gap-2 text-slate-800">
                                <span>📊</span> Données
                            </h3>
                            <ul class="space-y-4 text-sm text-slate-600 flex flex-col items-center w-full">
                                <li class="flex items-center gap-3 bg-white/50 p-3 rounded-lg w-full max-w-md justify-center">
                                    <span class="w-2 h-2 rounded-full bg-blue-500 flex-shrink-0"></span>
                                    <span><strong>Source :</strong> Wikipédia (API)</span>
                                </li>
                                <li class="flex items-center gap-3 bg-white/50 p-3 rounded-lg w-full max-w-md justify-center">
                                    <span class="w-2 h-2 rounded-full bg-blue-500 flex-shrink-0"></span>
                                    <span><strong>Moteur :</strong> LLM (Groq / Llama 3)</span>
                                </li>
                                <li class="flex items-center gap-3 bg-white/50 p-3 rounded-lg w-full max-w-md justify-center">
                                    <span class="w-2 h-2 rounded-full bg-blue-500 flex-shrink-0"></span>
                                    <span><strong>Volume :</strong> ~250 Nœuds</span>
                                </li>
                            </ul>
                        </div>

                        <!-- Col 2: Questions (Centré) -->
                        <div class="glass p-8 rounded-2xl w-full relative overflow-hidden flex flex-col items-center">
                            <div class="absolute top-0 right-0 p-4 opacity-10 pointer-events-none">
                                <svg class="w-32 h-32" fill="currentColor" viewBox="0 0 20 20"><path d="M9 2a1 1 0 000 2h2a1 1 0 100-2H9z"></path><path fill-rule="evenodd" d="M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z" clip-rule="evenodd"></path></svg>
                            </div>
                            
                            <h3 class="text-xl font-bold mb-6 text-slate-800">Les 3 Questions Clés</h3>
                            
                            <div class="space-y-4 w-full flex flex-col items-center">
                                <div class="flex gap-4 items-center group bg-white/30 p-3 rounded-xl w-full max-w-lg">
                                    <div class="flex-shrink-0 w-8 h-8 rounded-full bg-slate-900 text-white flex items-center justify-center font-bold text-sm shadow-lg group-hover:scale-110 transition">1</div>
                                    <p class="text-slate-600 text-left flex-1"><strong>Centralité :</strong> Qui sont les scientifiques les plus influents du réseau ?</p>
                                </div>
                                <div class="flex gap-4 items-center group bg-white/30 p-3 rounded-xl w-full max-w-lg">
                                    <div class="flex-shrink-0 w-8 h-8 rounded-full bg-slate-900 text-white flex items-center justify-center font-bold text-sm shadow-lg group-hover:scale-110 transition">2</div>
                                    <p class="text-slate-600 text-left flex-1"><strong>Communautés :</strong> Peut-on identifier des "écoles de pensée" automatiquement ?</p>
                                </div>
                                <div class="flex gap-4 items-center group bg-white/30 p-3 rounded-xl w-full max-w-lg">
                                    <div class="flex-shrink-0 w-8 h-8 rounded-full bg-slate-900 text-white flex items-center justify-center font-bold text-sm shadow-lg group-hover:scale-110 transition">3</div>
                                    <p class="text-slate-600 text-left flex-1"><strong>Connexions :</strong> Quel est le chemin d'influence entre deux savants éloignés ?</p>
                                </div>
                            </div>
                        </div>

                    </div>

                    <div class="text-center mt-12">
                        <a href="index.html" class="inline-flex items-center gap-3 px-8 py-4 bg-slate-900 hover:bg-slate-800 text-white rounded-xl shadow-lg hover:shadow-xl transition transform hover:-translate-y-1 font-medium">
                            <span>Lancer la Visualisation</span>
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                        </a>
                    </div>
                </div>
            </section>

        </div>
        
        <!-- Style pour l'animation de fond -->
        <style>
            @keyframes blob {{
                0% {{ transform: translate(0px, 0px) scale(1); }}
                33% {{ transform: translate(30px, -50px) scale(1.1); }}
                66% {{ transform: translate(-20px, 20px) scale(0.9); }}
                100% {{ transform: translate(0px, 0px) scale(1); }}
            }}
            .animate-blob {{
                animation: blob 7s infinite;
            }}
            .animation-delay-2000 {{
                animation-delay: 2s;
            }}
            .animation-delay-4000 {{
                animation-delay: 4s;
            }}
        </style>
    </body>
    </html>
    """

    output_path = "output/presentation.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"✅ Slides (Version Clean) générés : {output_path}")

if __name__ == "__main__":
    generate_slides()
