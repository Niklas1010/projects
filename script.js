// Navigation bar active state (for all pages)
document.querySelectorAll('.nav-bar a').forEach(link => {
    link.addEventListener('click', (e) => {
        if (!link.href.includes('index.html')) {
            e.preventDefault();
        }
        document.querySelector('.nav-bar a.active').classList.remove('active');
        link.classList.add('active');
    });
});

// Category card clicks (only for index.html)
if (document.querySelector('.category-grid')) {
    document.querySelectorAll('.category-card').forEach(card => {
        card.addEventListener('click', (e) => {
            if (!card.querySelector('a')) {
                const category = card.querySelector('h3').textContent;
                alert(`You clicked ${category}!`);
            }
        });
    });
}

// Lesson clicks and color matching (for category pages)
if (document.querySelector('.lesson-list')) {
    const categoryColors = {
        'Math': '#42A5F5',
        'Science': '#66BB6A',
        'History': '#FFCA28',
        'Art': '#AB47BC',
        'Language': '#26A69A'
    };
    const category = document.querySelector('.lesson-sidebar h2').textContent.split(' ')[0];
    const color = categoryColors[category];

    document.querySelectorAll('.lesson-link').forEach(link => {
        link.style.setProperty('--card-color', color); // Set color for hover
        link.addEventListener('click', (e) => {
            e.preventDefault();
            alert(`Loading lesson: ${link.textContent}`);
        });
    });
}