function handleLogin(event) {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    fetch('/users/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'), // CSRF token untuk Django
        },
        body: JSON.stringify({ email: email, password: password }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = 'landing.html'; // Redirect jika login berhasil
        } else {
            alert('Login gagal. Periksa email dan password Anda.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}