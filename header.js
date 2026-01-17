/**
 * HEADER.JS - Shared Header Component
 * Clean Swiss Minimalist Design
 */

document.addEventListener("DOMContentLoaded", function () {
    const headerContainer = document.getElementById("app-header");
    if (!headerContainer) return;

    const currentPage = window.location.pathname.split("/").pop() || "index.html";

    // Create style element
    const styleEl = document.createElement('style');
    styleEl.textContent = `
        .app-header {
            position: fixed;
            top: 24px;
            left: 50%;
            transform: translateX(-50%);
            width: calc(100% - 48px);
            max-width: 1200px;
            height: 64px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 12px 0 32px;
            z-index: 1000;
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.5);
            box-shadow: 
                0 4px 20px -2px rgba(0, 0, 0, 0.05),
                0 0 0 1px rgba(0, 0, 0, 0.05);
            border-radius: 100px;
            transition: all 0.3s ease;
        }

        .header-logo {
            font-family: 'Inter', sans-serif;
            font-size: 14px;
            font-weight: 700;
            letter-spacing: -0.01em;
            color: #111;
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .header-logo::before {
            content: '';
            display: block;
            width: 8px;
            height: 8px;
            background: #111;
            border-radius: 50%;
            box-shadow: 0 0 10px rgba(0,0,0,0.2);
        }

        .header-nav {
            display: flex;
            gap: 6px;
            background: rgba(0,0,0,0.03);
            padding: 4px;
            border-radius: 16px;
        }

        .nav-link {
            font-family: 'Inter', sans-serif;
            font-size: 13px;
            font-weight: 500;
            color: #666;
            text-decoration: none;
            padding: 8px 16px;
            border-radius: 12px;
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
            position: relative;
            z-index: 1;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .nav-link:hover {
            color: #111;
            background: rgba(255,255,255,0.5);
        }

        .nav-link.active {
            color: #fff;
            background: #111;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15);
            font-weight: 600;
        }

        /* Mobile Menu Button */
        .mobile-menu-btn {
            display: none;
            background: none;
            border: none;
            padding: 12px;
            cursor: pointer;
            font-size: 24px;
            line-height: 1;
        }

        /* Mobile Styles - Bottom Sheet Design */
        @media (max-width: 768px) {
            .app-header {
                top: 12px;
                left: 12px;
                right: 12px;
                width: calc(100% - 24px);
                max-width: calc(100% - 24px);
                height: 56px;
                border-radius: 28px; /* Keep rounded */
                padding: 0 20px;
                transform: none;
                background: rgba(255, 255, 255, 0.85);
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
                border: 1px solid rgba(255, 255, 255, 0.5);
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            }
            
            .header-logo {
                font-size: 13px;
                z-index: 2002;
                position: relative;
            }
            
            .mobile-menu-btn {
                display: flex;
                flex-direction: column;
                justify-content: center;
                gap: 4px;
                padding: 0;
                width: 36px;
                height: 36px;
                border-radius: 50%;
                background: rgba(0, 0, 0, 0.05);
                z-index: 2002;
                position: relative;
                transition: all 0.3s;
            }
            
            .mobile-menu-btn:active {
                transform: scale(0.95);
                background: rgba(0, 0, 0, 0.1);
            }
            
            /* Burger Icon */
            .burger-line {
                width: 16px;
                height: 2px;
                background: #111;
                transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            }
            
            .mobile-menu-btn.active .burger-line:nth-child(1) {
                transform: rotate(45deg) translate(4px, 4px);
            }
            .mobile-menu-btn.active .burger-line:nth-child(2) {
                opacity: 0;
                transform: translateX(-10px);
            }
            .mobile-menu-btn.active .burger-line:nth-child(3) {
                transform: rotate(-45deg) translate(4px, -4px);
            }
            
            /* Bottom Sheet Menu */
            .header-nav {
                position: fixed;
                bottom: 0;
                left: 0;
                right: 0;
                width: 100%;
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(30px);
                -webkit-backdrop-filter: blur(30px);
                border-top-left-radius: 24px;
                border-top-right-radius: 24px;
                padding: 32px 24px calc(env(safe-area-inset-bottom) + 24px);
                flex-direction: column;
                gap: 8px;
                box-shadow: 0 -8px 32px rgba(0, 0, 0, 0.12);
                transform: translateY(100%);
                transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
                z-index: 2001;
                pointer-events: all;
            }
            
            .header-nav.open {
                transform: translateY(0);
            }
            
            /* Nav Links */
            .nav-link {
                width: 100%;
                padding: 16px 20px;
                font-size: 16px;
                font-weight: 500;
                background: rgba(0, 0, 0, 0.03);
                border-radius: 12px;
                text-align: left;
                transition: all 0.2s;
                color: #666;
            }
            
            .nav-link:active {
                transform: scale(0.98);
                background: rgba(0, 0, 0, 0.06);
            }
            
            .nav-link.active {
                background: #111;
                color: #fff;
                font-weight: 600;
                box-shadow: none;
            }
        }
        
        /* Backdrop for mobile menu */
        .menu-backdrop {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.3);
            backdrop-filter: blur(4px);
            -webkit-backdrop-filter: blur(4px);
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s;
            z-index: 2000;
        }
        
        .menu-backdrop.active {
            opacity: 1;
            pointer-events: all;
        }
    `;
    document.head.appendChild(styleEl);

    // Create header HTML
    const headerDiv = document.createElement('div');
    headerDiv.className = 'app-header';
    
    // Logo
    const logo = document.createElement('a');
    logo.href = 'index.html';
    logo.className = 'header-logo';
    logo.textContent = 'EPISTEME AI';
    
    // Mobile menu button (Burger)
    const menuBtn = document.createElement('button');
    menuBtn.className = 'mobile-menu-btn';
    menuBtn.setAttribute('aria-label', 'Menu');
    
    // Create 3 lines for burger icon
    for(let i=0; i<3; i++) {
        const line = document.createElement('span');
        line.className = 'burger-line';
        menuBtn.appendChild(line);
    }
    
    // Create backdrop for mobile menu
    const backdrop = document.createElement('div');
    backdrop.className = 'menu-backdrop';
    document.body.appendChild(backdrop);

    menuBtn.onclick = function() {
        const nav = document.getElementById('header-nav');
        const isOpen = nav.classList.toggle('open');
        menuBtn.classList.toggle('active');
        backdrop.classList.toggle('active');
        
        // Lock body scroll
        if (isOpen) {
            document.body.style.overflow = 'hidden';
        } else {
            document.body.style.overflow = '';
        }
    };
    
    // Close menu on backdrop click
    backdrop.onclick = function() {
        const nav = document.getElementById('header-nav');
        nav.classList.remove('open');
        menuBtn.classList.remove('active');
        backdrop.classList.remove('active');
        document.body.style.overflow = '';
    };
    
    // Navigation
    const nav = document.createElement('nav');
    nav.className = 'header-nav';
    nav.id = 'header-nav';
    
    const links = [
        { href: 'index.html', text: 'Index' },
        { href: 'graph.html', text: 'Graphe' },
        { href: 'top.html', text: 'Top 100' },
        { href: 'about.html', text: 'Info' }
    ];
    
    links.forEach(link => {
        const a = document.createElement('a');
        a.href = link.href;
        a.className = 'nav-link';
        a.textContent = link.text;
        
        // Check if active
        if (currentPage === link.href || (currentPage === '' && link.href === 'index.html')) {
            a.classList.add('active');
        }
        
        // Close menu on navigation (mobile)
        a.onclick = function() {
            nav.classList.remove('open');
            menuBtn.classList.remove('active');
            backdrop.classList.remove('active');
            document.body.style.overflow = '';
        };
        
        nav.appendChild(a);
    });
    
    // Assemble header
    headerDiv.appendChild(logo);
    headerDiv.appendChild(menuBtn);
    headerDiv.appendChild(nav);
    
    headerContainer.appendChild(headerDiv);
    
    // Dispatch custom event to notify that header is ready
    window.dispatchEvent(new CustomEvent('headerLoaded'));
});
