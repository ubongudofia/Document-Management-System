

// =================== SIDE BAR ACTIVE =========================================

// Sidebar item click handler
const sidebarItems = document.querySelectorAll('.sidebar-item');

sidebarItems.forEach(item => {
    item.addEventListener('click', function () {
        // Remove active class from all items
        sidebarItems.forEach(i => i.classList.remove('active'));

        // Add active class to clicked item
        this.classList.add('active');
    });
});


// Initialize Lucide icons
lucide.createIcons();


document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll('.sidebar-item[data-page]').forEach(item => {
        item.addEventListener('click', function () {
            const page = this.getAttribute('data-page');

            // Optional: Highlight active
            document.querySelectorAll('.sidebar-item').forEach(el => el.classList.remove('active'));
            this.classList.add('active');

            // Load content into .main-content
            fetch(page)
                .then(response => response.text())
                .then(html => {
                    document.querySelector('.main-content').innerHTML = html;
                })
                .catch(error => {
                    console.error('Error loading page:', error);
                });
        });
    });
});