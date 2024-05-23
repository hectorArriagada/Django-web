/*

window.addEventListener("DOMContentLoaded", () => {
    showLoader();
  })
  
  window.addEventListener("load", () => {
    setTimeout(() => {
        hideLoader();
      }, 5000);
  })
  
  
  const loader = Comparador.getElementById("loaderPagina");
  const showLoader = () => {
   loader.classList.add("show_loader");
  }
  const hideLoader = () => {
    loader.classList.remove("show_loader");
  } 

  
   

  function mostrarLoader() {
    var loader = document.getElementById("loader");
    loader.classList.add("show_loader");
}

function ocultarLoader() {
    var loader = document.getElementById("loader");
    loader.classList.remove("show_loader");
} */

function mostrarLoader() {
  var loader = document.getElementById('loader');
  loader.style.display = 'block'; // Muestra el loader

  // Después de unos segundos (por ejemplo, 3 segundos), oculta el loader
  setTimeout(ocultarLoader, 3000);
}

function ocultarLoader() {
  var loader = document.getElementById('loader');
  loader.style.display = 'none'; // Oculta el loader
}

// Muestra el loader al cargar la página
document.addEventListener('DOMContentLoaded', function() {
  mostrarLoader();
});