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

        /* Mobile Styles */
        @media (max-width: 768px) {
            .app-header {
                top: 0;
                left: 0;
                right: 0;
                width: 100%;
                max-width: 100%;
                height: 60px;
                border-radius: 0;
                border: none;
                border-bottom: 1px solid rgba(0,0,0,0.05);
                padding: 0 20px;
                transform: none;
                background: rgba(255, 255, 255, 0.95);
            }
            
            .header-logo {
                font-size: 14px;
                z-index: 2002;
                position: relative;
            }
            
            .mobile-menu-btn {
                display: flex;
                flex-direction: column;
                justify-content: center;
                gap: 5px;
                padding: 10px;
                width: 40px;
                height: 40px;
                z-index: 2002;
                position: relative;
            }
            
            /* Burger Icon Animation */
            .burger-line {
                width: 20px;
                height: 2px;
                background: #111;
                transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            }
            
            .mobile-menu-btn.active .burger-line:nth-child(1) {
                transform: rotate(45deg) translate(5px, 5px);
            }
            .mobile-menu-btn.active .burger-line:nth-child(2) {
                opacity: 0;
                transform: translateX(-10px);
            }
            .mobile-menu-btn.active .burger-line:nth-child(3) {
                transform: rotate(-45deg) translate(5px, -5px);
            }
            
            /* Fullscreen Overlay Menu - 100% Opaque for Clean Look */
            .header-nav {
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                background: #ffffff; /* Solid white to hide content behind */
                padding: 100px 32px 40px;
                flex-direction: column;
                justify-content: center; /* Centered items */
                align-items: center;
                gap: 32px;
                opacity: 0;
                pointer-events: none;
                transform: translateY(10px);
                transition: opacity 0.4s ease, transform 0.4s ease;
                z-index: 2001;
            }
            
            .header-nav.open {
                display: flex !important;
                opacity: 1;
                pointer-events: all;
                transform: translateY(0);
            }
            
            .nav-link {
                width: 100%;
                padding: 0;
                font-size: 36px;
                font-weight: 400;
                letter-spacing: -0.02em;
                background: transparent !important;
                border-radius: 0;
                justify-content: center;
                text-align: center;
                opacity: 0;
                transform: translateY(20px);
                transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
            }
            
            .header-nav.open .nav-link {
                opacity: 1;
                transform: translateY(0);
            }
            
            /* Staggered animation delays */
            .header-nav.open .nav-link:nth-child(1) { transition-delay: 0.1s; }
            .header-nav.open .nav-link:nth-child(2) { transition-delay: 0.15s; }
            .header-nav.open .nav-link:nth-child(3) { transition-delay: 0.2s; }
            .header-nav.open .nav-link:nth-child(4) { transition-delay: 0.25s; }
            
            .nav-link.active {
                background: transparent;
                color: #111;
                font-weight: 600;
                border-bottom: 2px solid #111;
                display: inline-block;
                width: auto;
            }
            
            .nav-link.active::before {
                content: '';
                margin: 0;
            }
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
    logo.textContent = 'EPISTEME NETWORK';
    
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

    menuBtn.onclick = function() {
        const nav = document.getElementById('header-nav');
        const isOpen = nav.classList.toggle('open');
        menuBtn.classList.toggle('active');
        
        // Lock body scroll and add class for blur effect
        if (isOpen) {
            document.body.style.overflow = 'hidden';
            document.body.classList.add('menu-open');
        } else {
             document.body.style.overflow = '';
             document.body.classList.remove('menu-open');
        }
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
            menuBtn.innerHTML = '☰';
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
