/* ==========================================================================
   SYNKRONISERAD TEMA-MOTOR: Körs i footern och väntar in hela HTML-strukturen
   ========================================================================== */

// Denna funktion körs direkt på 0 sekunder för att förhindra en vit blixt om mörkt läge är sparat
(function() {
    const activeTheme = localStorage.getItem('site-theme');
    if (activeTheme === 'dark') {
        document.documentElement.classList.add('dark-theme');
        document.body.classList.add('dark-theme');
        injectDarkCSS();
    }
})();

// Väntar in att knappar och ikoner är 100 % redo på skärmen innan vi sätter igång
window.addEventListener('DOMContentLoaded', () => {
    const activeTheme = localStorage.getItem('site-theme');
    const sun = document.getElementById('sun-icon');
    const moon = document.getElementById('moon-icon');

    if (activeTheme === 'dark') {
        if (sun) sun.style.setProperty('display', 'block', 'important');
        if (moon) moon.style.setProperty('display', 'none', 'important');
    } else {
        if (sun) sun.style.setProperty('display', 'none', 'important');
        if (moon) moon.style.setProperty('display', 'block', 'important');
    }
});

function toggleSiteTheme() {
    const docBody = document.body;
    const docHtml = document.documentElement;
    const sunIcon = document.getElementById('sun-icon');
    const moonIcon = document.getElementById('moon-icon');
    
    docBody.classList.toggle('dark-theme');
    docHtml.classList.toggle('dark-theme');
    
    if (docBody.classList.contains('dark-theme')) {
        if (sunIcon) sunIcon.style.setProperty('display', 'block', 'important');
        if (moonIcon) moonIcon.style.setProperty('display', 'none', 'important');
        localStorage.setItem('site-theme', 'dark'); // Sparar valet i minnet
        injectDarkCSS();
    } else {
        if (sunIcon) sunIcon.style.setProperty('display', 'none', 'important');
        if (moonIcon) moonIcon.style.setProperty('display', 'block', 'important');
        localStorage.setItem('site-theme', 'light'); // Sparar valet i minnet
        removeDarkCSS();
    }
}

function injectDarkCSS() {
    if (document.getElementById('dynamic-dark-style')) return;
    const style = document.createElement('style');
    style.id = 'dynamic-dark-style';
    style.innerHTML = `
        /* ALLMÄNT MÖRKT: Mörklägger alla yttre ramar och behållare */
        html.dark-theme, 
        body.dark-theme, 
        .dark-theme #main,
        .dark-theme #content,
        .dark-theme .main, 
        .dark-theme .main-inner, 
        .dark-theme .content-wrapper, 
        .dark-theme .container, 
        .dark-theme .content, 
        .dark-theme .posts, 
        .dark-theme .post, 
        .dark-theme .post-summary, 
        .dark-theme .post-content,
        .dark-theme article,
        .dark-theme section,
        .dark-theme aside,
        .dark-theme .welcome-section {
            background-color: #1c1c1e !important;
            background: #1c1c1e !important;
            color: #f2f2f7 !important;
        }

        /* KROSSA VITA RUTOR INUTI BLOGGPOSTER: Tömmer bakgrunden i enskilda inlägg */
        .dark-theme .post-content *,
        .dark-theme .post-summary *,
        .dark-theme article * {
            background-color: transparent !important;
            background: transparent !important;
        }

        /* SKOTTSÄKER STARTSIDES-FIX: Tvingar bort alla vita bakgrunder på förhandsvisningarna */
        .dark-theme .posts *,
        .dark-theme .posts .post,
        .dark-theme .posts .post-summary,
        .dark-theme .posts p,
        .dark-theme .posts div {
            background-color: transparent !important;
            background: transparent !important;
        }

        /* FIX FÖR VÄLKOMSTTEXTEN: Krossar den sista vita hinnan på din nya div och dess p-tagg */
        .dark-theme .welcome-section,
        .dark-theme .welcome-section *,
        .dark-theme .welcome-section p,
        .dark-theme .welcome-section a {
            background-color: transparent !important;
            background: transparent !important;
        }

        /* Gör alla rubriker och vanlig text helvita och skarpa */
        .dark-theme h1, .dark-theme h2, .dark-theme h3, .dark-theme h4, .dark-theme h5, 
        .dark-theme span, .dark-theme a, .dark-theme .post-title, .dark-theme p, .dark-theme em {
            color: #ffffff !important;
        }

        /* Håller kvar dina snygga kornblå länkfärger och datum i mörkret */
        .dark-theme .post-meta, .dark-theme .post-time, 
        .dark-theme .archive-post-link, .dark-theme .archive-post-time, 
        .dark-theme .read-more-link, .dark-theme .posts .read-more-link {
            color: #6495ed !important;
        }
    `;
    document.head.appendChild(style);
}

function removeDarkCSS() {
    const style = document.getElementById('dynamic-dark-style');
    if (style) style.remove();
}
