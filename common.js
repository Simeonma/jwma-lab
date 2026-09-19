// Shared language switching for MacroPhotonic Lab
(function() {
    const currentLang = localStorage.getItem('labLang') || 'en';
    const enBtn = document.getElementById('en-btn');
    const cnBtn = document.getElementById('cn-btn');
    const enElements = document.querySelectorAll('[id$="-en"]');
    const cnElements = document.querySelectorAll('[id$="-cn"]');
    const enTitle = document.title;
    const cnTitleMeta = document.querySelector('meta[name="cn-title"]');
    const cnTitle = cnTitleMeta ? cnTitleMeta.content : enTitle;

    function initLanguage(lang) {
        const showEn = lang !== 'cn';
        const show = showEn ? enElements : cnElements;
        const hide = showEn ? cnElements : enElements;

        enBtn.classList.toggle('active', showEn);
        cnBtn.classList.toggle('active', !showEn);
        // Show: remove the inline display so each element returns to the
        // display defined by the stylesheet (flex, inline-block, ...).
        // Hide: force display:none. Never force 'block' — it would break
        // flex containers and other non-block layouts.
        show.forEach(function(el) { el.style.removeProperty('display'); });
        hide.forEach(function(el) { el.style.display = 'none'; });
        document.documentElement.lang = showEn ? 'en' : 'zh-CN';
        document.title = showEn ? enTitle : cnTitle;
    }

    initLanguage(currentLang);

    enBtn.addEventListener('click', function() {
        localStorage.setItem('labLang', 'en');
        initLanguage('en');
    });

    cnBtn.addEventListener('click', function() {
        localStorage.setItem('labLang', 'cn');
        initLanguage('cn');
    });
})();
