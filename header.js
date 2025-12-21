// Header Component for Scientific Graph Project
// Injects a consistent header into any page with <div id="app-header"></div>

document.addEventListener("DOMContentLoaded", function () {
    const headerContainer = document.getElementById("app-header");
    if (!headerContainer) return;

    // 1. Inject Styles
    const style = document.createElement("style");
    style.innerHTML = `
        /* Premium Glass Header Styles */
        .app-header {
            position: fixed;
            top: 24px;
            left: 50%;
            transform: translateX(-50%);
            width: auto;
            min-width: 480px;
            max-width: 90%;
            height: 64px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 8px 0 24px;
            border-radius: 100px;
            z-index: 1000;
            
            /* Real Glass Effect */
            background: rgba(255, 255, 255, 0.65);
            backdrop-filter: blur(24px) saturate(180%);
            -webkit-backdrop-filter: blur(24px) saturate(180%);
            box-shadow: 
                0 20px 40px -10px rgba(0, 0, 0, 0.1),
                inset 0 1px 0 rgba(255, 255, 255, 0.8),
                inset 0 -1px 0 rgba(0, 0, 0, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.3);
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .header-content {
            display: flex;
            align-items: center;
            justify-content: space-between;
            width: 100%;
            gap: 32px;
        }

        .logo {
            font-family: 'Inter', sans-serif;
            font-weight: 700;
            font-size: 15px;
            color: #18181B;
            text-decoration: none;
            letter-spacing: -0.02em;
            white-space: nowrap;
            background: linear-gradient(135deg, #000 0%, #333 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .nav-links {
            display: flex;
            gap: 4px;
            background: rgba(0, 0, 0, 0.03);
            padding: 4px;
            border-radius: 100px;
        }

        .nav-link {
            font-family: 'Inter', sans-serif;
            color: #71717A;
            text-decoration: none;
            font-size: 13px;
            font-weight: 500;
            padding: 8px 16px;
            border-radius: 20px;
            transition: all 0.2s ease;
            white-space: nowrap;
        }

        .nav-link:hover {
            color: #18181B;
            background: rgba(255, 255, 255, 0.5);
        }

        .nav-link.active {
            background-color: #18181B;
            color: white;
            font-weight: 600;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        }
        
        @media (max-width: 600px) {
            .app-header {
                width: 90%;
                min-width: auto;
                padding: 0 16px;
            }
            .logo { display: none; }
            .nav-links { width: 100%; justify-content: space-between; }
        }
    `;
    document.head.appendChild(style);

    // 2. Inject HTML
    // Determine active link based on current URL
    const currentPath = window.location.pathname;
    const isGraph = currentPath.includes("graph.html");
    const isLive = currentPath.includes("live.html");
    const isAbout = currentPath.includes("about.html");
    const isHome = currentPath.endsWith("/") || currentPath.includes("index.html");

    headerContainer.innerHTML = `
        <header class="app-header">
            <div class="header-content">
                <a href="index.html" class="logo">Projet Graphe et Open Data</a>
                <nav class="nav-links">
                    <a href="index.html" class="nav-link ${isHome ? 'active' : ''}">ACCUEIL</a>
                    <a href="graph.html" class="nav-link ${isGraph ? 'active' : ''}">GRAPHE</a>
                    <a href="live.html" class="nav-link ${isLive ? 'active' : ''}">LIVE</a>
                    <a href="about.html" class="nav-link ${isAbout ? 'active' : ''}">À PROPOS</a>
                </nav>
            </div>
        </header>
    `;
});
