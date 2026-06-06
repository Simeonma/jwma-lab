// Shared language switching for jwma-lab.com
(function() {
    const currentLang = localStorage.getItem('labLang') || 'en';
    const enBtn = document.getElementById('en-btn');
    const cnBtn = document.getElementById('cn-btn');
    const enElements = document.querySelectorAll('[id$="-en"]');
    const cnElements = document.querySelectorAll('[id$="-cn"]');

    function initLanguage(lang) {
        if (lang === 'cn') {
            cnBtn.classList.add('active');
            enBtn.classList.remove('active');
            cnElements.forEach(function(el) {
                if (!el.classList.contains('carousel-desc')) el.style.display = 'block';
            });
            enElements.forEach(function(el) {
                if (!el.classList.contains('carousel-desc')) el.style.display = 'none';
            });
            document.documentElement.lang = 'zh-CN';
        } else {
            enBtn.classList.add('active');
            cnBtn.classList.remove('active');
            enElements.forEach(function(el) {
                if (!el.classList.contains('carousel-desc')) el.style.display = 'block';
            });
            cnElements.forEach(function(el) {
                if (!el.classList.contains('carousel-desc')) el.style.display = 'none';
            });
            document.documentElement.lang = 'en';
        }
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
