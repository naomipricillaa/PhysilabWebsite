function handleSignup(event) {
    // Ambil nilai email, password, dan konfirmasi password
    const email = document.getElementById('signup-email').value;
    const password = document.getElementById('signup-password').value;
    const confirmPassword = document.getElementById('confirm-password').value;

    // Validasi password dan konfirmasi password
    if (!validateSignup(password, confirmPassword)) {
        event.preventDefault(); // Mencegah submit hanya jika validasi gagal
        alert('Password dan konfirmasi password tidak cocok.');
    }
}

function validateSignup(password, confirmPassword) {
    return password === confirmPassword; // Mengembalikan true jika password cocok
}

// Tambahkan event listener ke form untuk validasi
document.getElementById('signup-form').addEventListener('submit', handleSignup);
