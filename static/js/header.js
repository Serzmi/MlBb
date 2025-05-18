const themeToggle = document.getElementById('theme-toggle');
let currentTheme = localStorage.getItem('theme');

if (!currentTheme) {
    currentTheme = 'dark';
    localStorage.setItem('theme', currentTheme);
}

if (currentTheme === 'light') {
    document.documentElement.setAttribute('data-theme', 'light');
    themeToggle.checked = true;
} else {
    document.documentElement.removeAttribute('data-theme');
    themeToggle.checked = false;
}

themeToggle.addEventListener('change', function() {
    if (this.checked) {
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('theme', 'light');
    } else {
        document.documentElement.removeAttribute('data-theme');
        localStorage.setItem('theme', 'dark');
    }
});

function hexToRgb(hex) {
    const r = parseInt(hex.slice(1, 3), 16);
    const g = parseInt(hex.slice(3, 5), 16);
    const b = parseInt(hex.slice(5, 7), 16);
    return `${r}, ${g}, ${b}`;
}

document.documentElement.style.setProperty('--accent-1-rgb', hexToRgb(getComputedStyle(document.documentElement).getPropertyValue('--accent-1')));
document.documentElement.style.setProperty('--accent-2-rgb', hexToRgb(getComputedStyle(document.documentElement).getPropertyValue('--accent-2')));