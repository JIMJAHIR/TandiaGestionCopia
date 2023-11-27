// Variables para el control de la paginación
let currentPage = 1; // Página actual
const itemsPerPage = 12; // Cantidad de elementos por página
const tableRows = document.querySelectorAll('.clientes tbody tr'); // Filas de la tabla
const prevPageButton = document.getElementById('prevPage');
const nextPageButton = document.getElementById('nextPage');
const prevPageNumberButton = document.getElementById('prevPageNumber');
const nextPageNumberButton = document.getElementById('nextPageNumber');
const currentPageSpan = document.getElementById('currentPage');
let totalPages = Math.ceil(tableRows.length / itemsPerPage);

// Función para mostrar los elementos de la página actual
function showPage(page) {
  const startIndex = (page - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;

  tableRows.forEach((row, index) => {
    if (index >= startIndex && index < endIndex) {
      row.style.display = 'table-row';
    } else {
      row.style.display = 'none';
    }
  });

  // Actualiza la información de la página actual
  currentPageSpan.textContent = currentPage;
  prevPageNumberButton.textContent = currentPage - 1;
  nextPageNumberButton.textContent = currentPage + 1;

  // Actualiza la visibilidad de los botones Anterior y Siguiente
  prevPageButton.disabled = currentPage === 1;
  nextPageButton.disabled = currentPage === totalPages;

  // Actualiza la visibilidad de los botones de número de página
  prevPageNumberButton.style.display = currentPage === 1 ? 'none' : 'inline-block';
  nextPageNumberButton.style.display = currentPage === totalPages ? 'none' : 'inline-block';
}

// Función para ir a la página anterior
prevPageButton.addEventListener('click', () => {
  if (currentPage > 1) {
    currentPage--;
    showPage(currentPage);
  }
});

// Función para ir a la página siguiente
nextPageButton.addEventListener('click', () => {
  if (currentPage < totalPages) {
    currentPage++;
    showPage(currentPage);
  }
});

// Función para ir a una página específica
function goToPage(page) {
  if (page >= 1 && page <= totalPages) {
    currentPage = page;
    showPage(currentPage);
  }
}

// Botones para ir a las páginas anteriores y siguientes
prevPageNumberButton.addEventListener('click', () => {
  goToPage(currentPage - 1);
});

nextPageNumberButton.addEventListener('click', () => {
  goToPage(currentPage + 1);
});

// Mostrar la página inicial
showPage(currentPage);



function habilitarSeccionesImp() {
  var checkBox = document.getElementById("implementadorCheckbox");
  var secciones = document.querySelectorAll(".seccion-implementador");

  for (var i = 0; i < secciones.length; i++) {
    secciones[i].style.display = checkBox.checked ? "block" : "none";
  }
}

function habilitarSecciones() {
  var checkBox = document.getElementById("pass_sun_boolean");
  var secciones = document.querySelectorAll(".seccion-implementador");

  for (var i = 0; i < secciones.length; i++) {
    secciones[i].style.display = checkBox.checked ? "block" : "none";
  }
}
