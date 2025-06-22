// Obtener elementos del DOM
const carrito = document.getElementById('carrito'); 
const listaProductos = document.querySelector('.nav_fondo_categoria');
const lista = document.querySelector('#lista-carrito tbody');
const vaciarCarrito = document.getElementById('vaciar-carrito');

// Cargar eventos
cargarEventListeners();

function cargarEventListeners() {
    if (listaProductos) {
        listaProductos.addEventListener('click', comprarElemento);
    }

    if (carrito) {
        carrito.addEventListener('click', eliminarElemento);
    }

    if (vaciarCarrito) {
        vaciarCarrito.addEventListener('click', vaciarCarritoFuncion);
    }

    // Al cargar la página, recuperar productos guardados
    document.addEventListener('DOMContentLoaded', function () {
        manejarBotonesCantidad();
        cargarCarritoDesdeLocalStorage();
    });
}

// Agregar producto al carrito
function comprarElemento(e) {
    e.preventDefault();
    if (e.target.classList.contains('agregar-carrito')) {
        const elemento = e.target.closest('.producto');
        leerDatosElemento(elemento);
    }
}

// Leer los datos del producto
function leerDatosElemento(elemento) {
    const infoElemento = {
        imagen: elemento.querySelector('img').src,
        nombre: elemento.querySelector('h2').textContent,
        precio: elemento.querySelector('.columna-precio h2').textContent.replace('S/', '').trim(),
        cantidad: parseInt(elemento.querySelector('.input-cantidad').value),
        id: elemento.querySelector('.agregar-carrito').getAttribute('data-id')
    };
    insertarCarrito(infoElemento);
}

// Insertar en el carrito (HTML)
function insertarCarrito(producto) {
    const row = document.createElement('tr');
    row.innerHTML = `
        <td><img src="${producto.imagen}" width="100"></td>
        <td>${producto.nombre}</td>
        <td>${producto.precio}</td>
        <td>${producto.cantidad}</td>
        <td><a href="#" class="borrar" data-id="${producto.id}">X</a></td>
    `;
    lista.appendChild(row);

    // Guardar en localStorage
    guardarCarritoEnLocalStorage();
}

// Eliminar producto
function eliminarElemento(e) {
    if (e.target.classList.contains('borrar')) {
        e.preventDefault();  
        e.target.closest('tr').remove();
        guardarCarritoEnLocalStorage();
    }
}

// Vaciar todo el carrito
function vaciarCarritoFuncion() {
    while (lista.firstChild) {
        lista.removeChild(lista.firstChild);
    }
    localStorage.removeItem('carrito');
    return false;
}

// Guardar el carrito actual en localStorage
function guardarCarritoEnLocalStorage() {
    const productos = [];

    lista.querySelectorAll('tr').forEach(fila => {
        const imagen = fila.querySelector('img').src;
        const nombre = fila.querySelector('td:nth-child(2)').textContent;
        const precio = fila.querySelector('td:nth-child(3)').textContent;
        const cantidad = fila.querySelector('td:nth-child(4)').textContent;
        const id = fila.querySelector('.borrar').getAttribute('data-id');

        productos.push({ imagen, nombre, precio, cantidad, id });
    });

    localStorage.setItem('carrito', JSON.stringify(productos));
}

// Cargar productos guardados al recargar la página
function cargarCarritoDesdeLocalStorage() {
    const productos = JSON.parse(localStorage.getItem('carrito')) || [];

    productos.forEach(producto => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td><img src="${producto.imagen}" width="100"></td>
            <td>${producto.nombre}</td>
            <td>${producto.precio}</td>
            <td>${producto.cantidad}</td>
            <td><a href="#" class="borrar" data-id="${producto.id}">X</a></td>
        `;
        lista.appendChild(row);
    });
}

// Manejo de botones de cantidad
function manejarBotonesCantidad() {
    document.querySelectorAll('.producto').forEach(producto => {
        const btnMenos = producto.querySelector('.btn-menos');
        const btnMas = producto.querySelector('.btn-mas');
        const inputCantidad = producto.querySelector('.input-cantidad');

        if (btnMenos && btnMas && inputCantidad) {
            btnMenos.addEventListener('click', () => {
                let cantidad = parseInt(inputCantidad.value);
                if (cantidad > 1) {
                    inputCantidad.value = cantidad - 1;
                }
            });

            btnMas.addEventListener('click', () => {
                let cantidad = parseInt(inputCantidad.value);
                inputCantidad.value = cantidad + 1;
            });
        }
    });
}

