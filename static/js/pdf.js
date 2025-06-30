function descargarPDF() {
    const element = document.getElementById("recibo");
    const inputCarritoJson = document.getElementById("carrito-json");
    const inputFechaEnvio = document.getElementById("input-fecha_envio");
    const inputTotal = document.getElementById("input-total");

    let carrito = JSON.parse(localStorage.getItem("carrito")) || [];

    if (carrito.length === 0) {
        alert("Tu carrito está vacío.");
        return;
    }

    // Asegurarse de que cada item tenga el campo subtotal
    carrito = carrito.map(item => {
        return {
            ...item,
            subtotal: item.precio * item.cantidad
        };
    });

    inputCarritoJson.value = JSON.stringify(carrito);

    const total = carrito.reduce((sum, item) => sum + item.subtotal, 0);
    inputTotal.value = total.toFixed(2);

    const fechaTexto = new Date().toLocaleDateString('es-PE', {
        day: '2-digit', month: 'long', year: 'numeric'
    });
    inputFechaEnvio.value = fechaTexto;

    const options = {
        margin: [0.5, 0.2, 0.5, 0.8],
        filename: `recibo_temp.pdf`,
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2, scrollY: 0 },
        jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
    };

    html2pdf().set(options).from(element).save().then(() => {
        // Vaciar el carrito después de guardar PDF
        localStorage.removeItem("carrito");

        // Enviar formulario
        document.getElementById("form-pago").submit();
    });
}
