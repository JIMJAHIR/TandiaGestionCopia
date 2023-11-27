let equipmentCount = 0; // Variable para mantener un seguimiento de los equipos agregados

// Función para agregar una nueva sección de equipo
function addEquipment() {
  equipmentCount++;

  var equipmentSection = document.createElement("div");
  equipmentSection.className = "conteiner-infoNewClient conteiner-infoNewClient-three";
  equipmentSection.id = "equipment-" + equipmentCount; // Asignar un ID único

  var equipmentSelect = document.createElement("div");
  equipmentSelect.className = "newInput-container";

  var selectLabel = document.createElement("label");
  selectLabel.className = "label-overlay";
  selectLabel.textContent = "Equipo";

  var selectElement = document.createElement("select");
  selectElement.className = "styled-input";
  selectElement.name = "nameE";

  var equipmentOptions = [
    "Impresora Azul Alámbrica",
    "Impresora Portátil",
    "Impresora de 80 MM",
    "Lector de Barras Alámbrico",
    "Lector de Barras Inalámbrico",
    "Gaveta de Dinero",
    "V2 - T-Portátil",
    "Lector Sunmi - 2",
    "Impresora de Código de Barras",
    "Otros"
  ];

  for (var i = 0; i < equipmentOptions.length; i++) {
    var option = document.createElement("option");
    option.value = equipmentOptions[i];
    option.text = equipmentOptions[i];
    selectElement.appendChild(option);
  }

  equipmentSelect.appendChild(selectLabel);
  equipmentSelect.appendChild(selectElement);

  var quantityInput = document.createElement("div");
  quantityInput.className = "newInput-container";

  var quantityLabel = document.createElement("label");
  quantityLabel.className = "label-overlay";
  quantityLabel.textContent = "Cantidad";

  var quantityElement = document.createElement("input");
  quantityElement.className = "styled-input";
  quantityElement.type = "number";
  quantityElement.name = "quantityE";
  quantityElement.value = "1";
  quantityElement.min = "1";
  quantityElement.max = "10";
  quantityElement.step = "1";
  quantityElement.required = true;

  quantityInput.appendChild(quantityLabel);
  quantityInput.appendChild(quantityElement);

  equipmentSection.appendChild(equipmentSelect);
  equipmentSection.appendChild(quantityInput);

  // Crear un botón "Quitar" para esta sección de equipo
  var removeButton = document.createElement("button");
  removeButton.textContent = "Eliminar";
  removeButton.className = "styled-input remove-button";
  removeButton.addEventListener("click", function () {
    removeEquipment(equipmentSection.id); // Llamar a la función para quitar esta sección
  });

  equipmentSection.appendChild(removeButton);

  // Obtener el elemento de referencia con la clase "conteiner-reference"
  var referenceElement = document.querySelector(".conteiner-reference");

  // Insertar la nueva sección de equipo antes del elemento de referencia
  if (referenceElement) {
    referenceElement.parentNode.insertBefore(equipmentSection, referenceElement);
  } else {
    // Si no se encuentra el elemento de referencia, simplemente agrégalo al final
    document.querySelector(".conteiner-new").appendChild(equipmentSection);
  }
}

// Función para quitar una sección de equipo
function removeEquipment(equipmentId) {
  var equipmentToRemove = document.getElementById(equipmentId);
  if (equipmentToRemove) {
    equipmentToRemove.remove(); // Eliminar la sección de equipo
  }
}

// Obtén referencias a los campos de entrada y al botón de envío Nuevo Cliente
const ruc = document.getElementById('ruc');
const validationMessage = document.getElementById('ruc-validation-message');
const submit_newClient = document.getElementById('submit_newClient');

// Agrega un evento de escucha para cada campo de entrada
ruc.addEventListener('input', validateForm);

async function validateForm() {
  const rucValue = ruc.value;

  if (rucValue.length >= 11) {
    const client_exists = await validar_client(rucValue);

    if (client_exists) {
      validationMessage.textContent = 'Ya existe un cliente con el RUC ingresado*';
      validationMessage.style.paddingTop = '5px'
    } else {
      validationMessage.textContent = '';
      rucValid = true;
    }
  } else {
    validationMessage.textContent = 'Longitud Mínima 11 caracteres*';
    validationMessage.style.paddingTop = '5px'
    rucValid = false;
  }

  submit_newClient.disabled = !rucValid;
  submit_newClient.style.backgroundColor = rucValid ? 'rgba(37, 99, 235)' : '#ccc';

}

async function validar_client(ruc) {
  const response = await fetch(`/validar_client?ruc=${ruc}`);
  const data = await response.json();
  return data.exists;
}

