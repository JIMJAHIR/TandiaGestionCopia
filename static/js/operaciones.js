// Obtén referencias a los campos de entrada y al botón de envío 
const ruc = document.getElementById('ruc');
const validationMessage = document.getElementById('ruc-validation-message');
const submit_implementation = document.getElementById('submit_implementation');

// Agrega un evento de escucha para cada campo de entrada
ruc.addEventListener('input', validateForm);

async function validateForm() {
  const rucValue = ruc.value;

  if (rucValue.length >= 11) {
    const imp_exists = await validar_registro(rucValue);

    if (imp_exists) {
      validationMessage.textContent = 'RUC ya existe en la base de datos*';
      validationMessage.style.paddingTop = '5px'
    } else {
      const client_exists = await validar_client(rucValue);

      if (client_exists) {
        validationMessage.textContent = '';
        rucValid = true;
      } else {
        validationMessage.textContent = 'No existe un cliente con el RUC ingresado*';
        validationMessage.style.paddingTop = '5px'
      }
    }
  } else {
    validationMessage.textContent = 'Longitud Mínima 11 caracteres*';
    validationMessage.style.paddingTop = '5px'
    rucValid = false;
  }

  submit_implementation.disabled = !rucValid;
  submit_implementation.style.backgroundColor = rucValid ? 'rgba(37, 99, 235)' : '#ccc';
}

async function validar_registro(ruc) {
  const response = await fetch(`/verificar_ruc?ruc=${ruc}`);
  const data = await response.json();
  return data.exists;
}

async function validar_client(ruc) {
  const response = await fetch(`/validar_client?ruc=${ruc}`);
  const data = await response.json();
  return data.exists;
}

/* POPUP IMPLEMENTATION - REGISTRAR COMPAÑIA */
