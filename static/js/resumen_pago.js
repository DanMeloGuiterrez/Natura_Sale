document.addEventListener('DOMContentLoaded', function () {
    const resumenBody = document.getElementById('resumen-body');
    const totalPago = document.getElementById('total-pago');

    const carrito = JSON.parse(localStorage.getItem('carrito')) || [];
    let total = 0;

    carrito.forEach(producto => {
        const subtotal = parseFloat(producto.precio) * parseInt(producto.cantidad);
        total += subtotal;

        const row = document.createElement('tr');
        row.innerHTML = `
            <td><img src="${producto.imagen}" width="80"></td>
            <td>${producto.nombre}</td>
            <td>S/ ${producto.precio}</td>
            <td>${producto.cantidad}</td>
            <td>S/ ${subtotal.toFixed(2)}</td>
        `;
        resumenBody.appendChild(row);
    });

    totalPago.textContent = total.toFixed(2);
});
