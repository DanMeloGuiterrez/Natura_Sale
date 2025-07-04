const productos = JSON.parse(document.getElementById('productos-data').dataset.productos);

function mostrarProductos(productosFiltrados) {
    const contenedorProductos = document.getElementById('raiz');
    if (productosFiltrados.length === 0) {
        contenedorProductos.innerHTML = '<p>No se encontraron productos.</p>';
        return;
    }
    contenedorProductos.innerHTML = productosFiltrados.map(p => `
        <div class="box producto">
            <div class="img-box">
                <img src="/static/img/${p.imagen}" class="images" alt="${p.nombre_producto}">
            </div>
            <div class="bottom">
                <h2 class="nombre-producto">${p.nombre_producto}</h2>
                <div class="columna-precio">
                    <h2>S/${p.precio}</h2>
                </div>
                <p>Stock: ${p.stock}</p>
                <div class="cantidad">
                    <label for="cantidad-${p.nombre_producto}">Cantidad:</label>
                    <input type="number" id="cantidad-${p.nombre_producto}" class="input-cantidad" value="1" min="1" max="${p.stock}">
                </div> <br>
                <button class="agregar-carrito" data-id="${p.id_producto}">Agregar al carrito</button>
            </div>
        </div>
    `).join('');
}

function filtrarProductos() {
    const textBusqueda = document.getElementById('barraBusqueda').value.toLowerCase()
        .normalize("NFD").replace(/[\u0300-\u036f]/g, ""); // Para que cuando escriba el producto con o sin tilde se vea igual
    const productosFiltrados = productos.filter(producto =>
        producto.nombre_producto.toLowerCase()
            .normalize("NFD").replace(/[\u0300-\u036f]/g, "") // Para que cuando escriba el producto con o sin tilde se vea igual
            .includes(textBusqueda)
    );
    mostrarProductos(productosFiltrados);
}

document.getElementById('barraBusqueda').addEventListener('input', filtrarProductos);

// Mostrar todos los productos al inicio
mostrarProductos(productos);