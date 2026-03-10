// Admin Panel JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Flash message close functionality
    const flashCloseButtons = document.querySelectorAll('.flash-close');
    flashCloseButtons.forEach(button => {
        button.addEventListener('click', function() {
            this.parentElement.style.display = 'none';
        });
    });

    // Auto-hide flash messages after 5 seconds
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(message => {
        setTimeout(() => {
            message.style.opacity = '0';
            setTimeout(() => {
                message.style.display = 'none';
            }, 300);
        }, 5000);
    });

    // Confirm delete actions
    const deleteLinks = document.querySelectorAll('a[href*="delete"]');
    deleteLinks.forEach(link => {
        if (!link.onclick) {
            link.addEventListener('click', function(e) {
                if (!confirm('Are you sure you want to delete this item?')) {
                    e.preventDefault();
                }
            });
        }
    });

    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;

            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    field.style.borderColor = 'var(--error)';
                    isValid = false;
                } else {
                    field.style.borderColor = 'var(--border)';
                }
            });

            if (!isValid) {
                e.preventDefault();
                alert('Please fill in all required fields.');
            }
        });
    });

    // File upload preview
    const fileInputs = document.querySelectorAll('input[type="file"]');
    fileInputs.forEach(input => {
        input.addEventListener('change', function() {
            const file = this.files[0];
            if (file) {
                const fileSize = (file.size / 1024 / 1024).toFixed(2);
                const maxSize = 16; // MB
                
                if (fileSize > maxSize) {
                    alert(`File size (${fileSize}MB) exceeds the maximum allowed size of ${maxSize}MB.`);
                    this.value = '';
                    return;
                }

                // Show file info
                let infoDiv = this.parentElement.querySelector('.file-info');
                if (!infoDiv) {
                    infoDiv = document.createElement('div');
                    infoDiv.className = 'file-info';
                    infoDiv.style.cssText = 'margin-top: 8px; padding: 8px; background: var(--surface); border: 1px solid var(--border); font-size: 0.8rem; color: var(--muted);';
                    this.parentElement.appendChild(infoDiv);
                }
                
                infoDiv.innerHTML = `
                    📄 <strong>${file.name}</strong><br>
                    Size: ${fileSize}MB | Type: ${file.type || 'Unknown'}
                `;
            }
        });
    });

    // Sidebar active state
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });

    // Auto-save form data to localStorage (for long forms)
    const longForms = document.querySelectorAll('form[data-autosave]');
    longForms.forEach(form => {
        const formId = form.id || 'autosave-form';
        
        // Load saved data
        const savedData = localStorage.getItem(`admin-form-${formId}`);
        if (savedData) {
            try {
                const data = JSON.parse(savedData);
                Object.keys(data).forEach(key => {
                    const field = form.querySelector(`[name="${key}"]`);
                    if (field && field.type !== 'file') {
                        if (field.type === 'checkbox') {
                            field.checked = data[key];
                        } else {
                            field.value = data[key];
                        }
                    }
                });
            } catch (e) {
                console.warn('Failed to load saved form data:', e);
            }
        }

        // Save data on input
        form.addEventListener('input', function() {
            const formData = new FormData(form);
            const data = {};
            for (let [key, value] of formData.entries()) {
                if (form.querySelector(`[name="${key}"]`).type !== 'file') {
                    data[key] = value;
                }
            }
            localStorage.setItem(`admin-form-${formId}`, JSON.stringify(data));
        });

        // Clear saved data on successful submit
        form.addEventListener('submit', function() {
            localStorage.removeItem(`admin-form-${formId}`);
        });
    });

    // Statistics counter animation
    const statNumbers = document.querySelectorAll('.stat-number');
    statNumbers.forEach(stat => {
        const target = parseInt(stat.textContent);
        if (target && target > 0) {
            let current = 0;
            const increment = target / 50;
            const timer = setInterval(() => {
                current += increment;
                if (current >= target) {
                    current = target;
                    clearInterval(timer);
                }
                stat.textContent = Math.floor(current);
            }, 30);
        }
    });

    // Search functionality (if search input exists)
    const searchInput = document.querySelector('#search');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const query = this.value.toLowerCase();
            const rows = document.querySelectorAll('.table tbody tr');
            
            rows.forEach(row => {
                const text = row.textContent.toLowerCase();
                row.style.display = text.includes(query) ? '' : 'none';
            });
        });
    }

    // Keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        // Ctrl/Cmd + S to save form
        if ((e.ctrlKey || e.metaKey) && e.key === 's') {
            e.preventDefault();
            const form = document.querySelector('form');
            if (form) {
                form.submit();
            }
        }

        // Escape to close modals or go back
        if (e.key === 'Escape') {
            const backButton = document.querySelector('a[href*="back"], .btn-secondary');
            if (backButton && backButton.textContent.includes('Back')) {
                window.location.href = backButton.href;
            }
        }
    });
});

// Utility functions
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `flash-message flash-${type}`;
    notification.innerHTML = `
        ${message}
        <button class="flash-close">&times;</button>
    `;
    
    const container = document.querySelector('.flash-messages') || document.querySelector('.content-body');
    container.insertBefore(notification, container.firstChild);
    
    // Auto-hide
    setTimeout(() => {
        notification.style.opacity = '0';
        setTimeout(() => notification.remove(), 300);
    }, 5000);
}

function confirmAction(message, callback) {
    if (confirm(message)) {
        callback();
    }
}

// Export for use in other scripts
window.AdminUtils = {
    showNotification,
    confirmAction
};