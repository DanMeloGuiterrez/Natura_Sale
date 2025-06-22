function descargarPDF() {
    const element = document.getElementById("recibo");
    const numeroRecibo = document.getElementById("numero-recibo");

    if (!element || !numeroRecibo) {
        alert("No se encontró el contenido del recibo.");
        return;
    }

    // Generar número aleatorio de 6 dígitos
    const numero = Math.floor(100000 + Math.random() * 900000);
    numeroRecibo.textContent = numero;

    // Espera para que el número aparezca en pantalla antes de generar el PDF
    setTimeout(() => {
        const options = {
            margin:       [0.5, 0.2, 0.5, 0.8], // márgenes en pulgadas
            filename:     `recibo_${numero}.pdf`,
            image:        { type: 'jpeg', quality: 0.98 },
            html2canvas:  { scale: 2, scrollY: 0 },
            jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }
        };

        html2pdf().set(options).from(element).save();
    }, 200);
}
