
document.addEventListener('DOMContentLoaded', (event) => {
    console.log('El documento está completamente cargado y analizado.');

    // Ejemplo de una función simple que muestra una alerta cuando se envía el formulario de contacto
    const contactForm = document.querySelector('#id_boton');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            alert('Tu mensaje ha sido enviado. ¡Gracias por contactarnos!');
            contactForm.reset();
        });
    }

    // Función para manejar el mensaje de éxito al guardar un auto
    function mostrarMensajeGuardado() {
        alert('El auto se ha guardado correctamente.');
    }

    // Ejemplo de cómo podrías detectar el guardado del auto y llamar a la función
    // Supongamos que aquí tienes alguna lógica que te permita detectar cuándo se guarda un auto

    // Por ejemplo, podrías simularlo si tienes un botón en tu formulario de agregar auto:
    const botonGuardar = document.querySelector('#id_boton_guardar');  // Asegúrate de que este selector sea el correcto
    if (botonGuardar) {
        botonGuardar.addEventListener('click', () => {
            mostrarMensajeGuardado();
        });
    }
});

