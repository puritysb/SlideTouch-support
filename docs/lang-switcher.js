// lang-switcher.js - Language switcher for SlideTouch support site
(function() {
    'use strict';

    const SUPPORTED_LANGS = ['en', 'ko', 'ja'];
    const DEFAULT_LANG = 'en';
    const PAGES = ['', 'features.html', 'support.html', 'privacy.html', 'releases.html'];

    function getCurrentLang() {
        const path = window.location.pathname;
        const basePath = '/SlideTouch-support';
        let cleanPath = path;
        if (path.startsWith(basePath)) {
            cleanPath = path.substring(basePath.length);
        }

        for (const lang of SUPPORTED_LANGS) {
            if (cleanPath.startsWith('/' + lang + '/') || cleanPath === '/' + lang) {
                return lang;
            }
        }
        return DEFAULT_LANG;
    }

    function getLocalizedPath(targetLang) {
        const basePath = '/SlideTouch-support';
        const path = window.location.pathname;

        let page = '';
        for (const p of PAGES) {
            if (p && (path.includes(p) || path.endsWith(p.replace('.html', '')))) {
                page = p;
                break;
            }
        }

        if (targetLang === DEFAULT_LANG) {
            return basePath + '/' + page;
        }
        return basePath + '/' + targetLang + '/' + page;
    }

    function updateDropdownLinks() {
        const currentLang = getCurrentLang();

        document.querySelectorAll('.lang-option').forEach(function(link) {
            var lang = link.dataset.lang;
            if (lang) {
                link.href = getLocalizedPath(lang);
                if (lang === currentLang) {
                    link.classList.add('active');
                } else {
                    link.classList.remove('active');
                }
            }
        });

        var langCode = document.querySelector('.lang-code');
        if (langCode) {
            langCode.textContent = currentLang.toUpperCase();
        }
    }

    function initDropdown() {
        var switcher = document.querySelector('.lang-switcher');
        var button = document.querySelector('.lang-current');

        if (!switcher || !button) return;

        button.addEventListener('click', function(e) {
            e.stopPropagation();
            switcher.classList.toggle('open');
        });

        document.addEventListener('click', function() {
            switcher.classList.remove('open');
        });

        var dropdown = document.querySelector('.lang-dropdown');
        if (dropdown) {
            dropdown.addEventListener('click', function(e) {
                e.stopPropagation();
            });
        }
    }

    document.addEventListener('DOMContentLoaded', function() {
        updateDropdownLinks();
        initDropdown();
    });
})();
