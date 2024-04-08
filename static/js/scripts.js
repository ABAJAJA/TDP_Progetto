window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0;
    const mainNav = document.getElementById('mainNav');
    const headerHeight = mainNav.clientHeight;
    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1;
        if ( currentTop < scrollPos) {
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible');
            } else {
                mainNav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            mainNav.classList.remove(['is-visible']);
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed');
            }
        }
        scrollPos = currentTop;
    });
})

document.getElementById("submitButton").addEventListener("click", function(event) {
    event.preventDefault();
    var name = document.getElementById("name").value.trim();
    var email = document.getElementById("email").value.trim();
    var phone = document.getElementById("phone").value.trim();
    var errors = false;

    
    document.querySelectorAll(".error-message").forEach(function(element) {
        element.textContent = "";
    });

   
    if (name.length < 2) {
        document.getElementById("nameError").textContent = "Il nome deve contenere almeno due caratteri";
        errors = true;
    }

    
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        document.getElementById("emailError").textContent = "indirizzo email non valido";
        errors = true;
    }

    
    var phoneRegex = /^\d{10,}$/;
    if (!phoneRegex.test(phone)) {
        document.getElementById("phoneError").textContent = "Il numero di telefono deve contenere almeno dieci cifre";
        errors = true;
    }

    if (!errors) {
        
        document.getElementById("contactForm").reset(); 
        document.getElementById("contactForm").style.display = "none";
        document.getElementById("submitSuccessMessage").classList.remove("d-none");
    }
});