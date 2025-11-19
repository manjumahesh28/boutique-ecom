// Example: Add to cart via fetch API
document.querySelectorAll('a[href*="add_to_cart"]').forEach(link => {
    link.addEventListener('click', async (e) => {
        e.preventDefault();
        const response = await fetch(link.href, { method: 'POST', headers: {'X-CSRFToken': getCookie('csrftoken')} });
        if (response.ok) { alert('Added to cart!'); }
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}