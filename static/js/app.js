let imagenes = [
    {
        "url": "img/Imagenes/imagen1.png",
        "descripcion": "Puede encontrar un monton de variedades de plantas"
    },
    {
        "url": "img/Imagenes/imagen2.png",
        "descripcion": "Distribuimos a diferentes partes del pais"
    },
    {
        "url": "img/Imagenes/imagen3.png",
        "descripcion": "Al mejor precio S/. "
    },
    {
        "url": "img/Imagenes/imagen4.png",
        "descripcion": "Y al menor tiempo posible"
    },
    {
        "url": "img/Imagenes/imagen5.png",
        "descripcion": "Elije Jardines Eden para tus decoraciones"
    }
];

let atras = document.getElementById('atras');
let adelante = document.getElementById('adelante');
let imagen = document.getElementById('img');
let puntos = document.getElementById('puntos');
 
let actual = 0;
posicionCarrusel();

atras.addEventListener('click', function(){
    actual -= 1;
    if (actual === -1){
        actual = imagenes.length - 1;
    }
    imagen.innerHTML = `
        <img class="img" src="${imagenes[actual].url}" alt="logo pagina" loading="lazy"></img>
        <div class="texto_imagen">
            <p>${imagenes[actual].descripcion}</p>
        </div>
    `;
    posicionCarrusel();
});  

adelante.addEventListener('click', function(){
    actual += 1;
    if (actual === imagenes.length){
        actual = 0;
    }
    imagen.innerHTML = `
        <img class="img" src="${imagenes[actual].url}" alt="logo pagina" loading="lazy"></img>
        <div class="texto_imagen">
            <p>${imagenes[actual].descripcion}</p>
        </div>
    `;
    posicionCarrusel();
});  

function posicionCarrusel() {
    puntos.innerHTML = "";
    for (var i = 0; i <imagenes.length; i++){
        if(i == actual){
            puntos.innerHTML += '<p class="bold">.<p>'
        }
        else{
            puntos.innerHTML += '<p>.<p>'
        }
    } 
}
