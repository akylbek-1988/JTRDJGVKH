const themeToggle = document.getElementById('themeToggle');
const body = document.body;
const languageButtons = document.querySelectorAll('.lang-button');
const mobileToggle = document.getElementById('mobileToggle');
const navLinks = document.getElementById('navLinks');

if (themeToggle) {
    themeToggle.addEventListener('click', () => {
        body.classList.toggle('theme-dark');
        const isDark = body.classList.contains('theme-dark');
        themeToggle.textContent = isDark ? '🌙' : '☀';
    });
}

languageButtons.forEach(button => {
    button.addEventListener('click', () => {
        document.querySelectorAll('.lang-button').forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');
    });
});

if (mobileToggle && navLinks) {
    mobileToggle.addEventListener('click', () => {
        navLinks.classList.toggle('show');
    });
}

const forms = document.querySelectorAll('form');
forms.forEach(form => {
    form.addEventListener('submit', event => {
        const required = form.querySelectorAll('[required]');
        let valid = true;
        required.forEach(field => {
            if (!field.value.trim()) {
                valid = false;
                field.classList.add('invalid');
            } else {
                field.classList.remove('invalid');
            }
        });
        if (!valid) {
            event.preventDefault();
        }
    });
});
