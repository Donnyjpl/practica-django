// JavaScript personalizado para tu sitio web

document.addEventListener('DOMContentLoaded', (event) => {
    console.log('El documento está completamente cargado y analizado.');

    // Ejemplo de una función simple que muestra una alerta cuando se envía el formulario de contacto
    const contactForm = document.querySelector('form');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            alert('Tu mensaje ha sido enviado. ¡Gracias por contactarnos!');
            contactForm.reset();
        });
    }
});
