//form validation
document
  .getElementById("submitButton")
  .addEventListener("click", function (event) {
    event.preventDefault();
    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const phone = document.getElementById("phone").value.trim();
    const msg = document.getElementById("message").value;
    let errors = false;

    document.querySelectorAll(".error-message").forEach(function (element) {
      element.textContent = "";
    });

    if (name.length < 2) {
      document.getElementById("nameError").textContent =
        "Il nome deve contenere almeno due caratteri";
      errors = true;
    }

    var emailRegex = /^[a-zA-Z0-9_-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,4}$/;
    if (!emailRegex.test(email)) {
      document.getElementById("emailError").textContent =
        "indirizzo email non valido";
      errors = true;
    }

    var phoneRegex = /^\d{10}$/;
    if (!phoneRegex.test(phone)) {
      document.getElementById("phoneError").textContent =
        "Il numero di telefono deve contenere dieci numeri";
      errors = true;
    }

    if (!errors) {
      document.getElementById("contactForm").reset();
      document.getElementById("contactForm").style.display = "none";
      document
        .getElementById("submitSuccessMessage")
        .classList.remove("d-none");

      fetch("http://127.0.0.1:5000/api/v1/createMessage", {
        method: "POST",
        body: JSON.stringify({
          name: name,
          email: email,
          phone: phone,
          message: msg,
        }),
        headers: {
          "Content-type": "application/json; charset=UTF-8",
          "X-Api-Token": "OrqQfyXOUGIXigjfCHhgTCVNewZWAXEe",
        },
      });

      //Ritorna al top della pagina
      window.scrollTo({ top: 0, behavior: "smooth" });
    }
  });