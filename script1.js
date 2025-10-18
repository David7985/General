const selectCiudad = document.getElementById('ciudadSelect');
const divClima = document.getElementById('clima');

selectCiudad.addEventListener('change', () => {
    const codigo = selectCiudad.value;
    if (!codigo) {
        divClima.innerHTML = 'Selecciona una ciudad para ver el clima';
        return;
    }

    fetch(`https://api.gael.cloud/general/public/clima/${codigo}`)
        .then(response => response.json())
        .then(data => {
            divClima.innerHTML = `
                <p><strong>Ciudad:</strong> ${data.Estacion}</p>
                <p><strong>Temperatura:</strong> ${data.Temp} °C</p>
                <p><strong>Humedad:</strong> ${data.Humedad} %</p>
                <p><strong>Estado:</strong> ${data.Estado}</p>
            `;
        })
        .catch(err => {
          divClima.innerHTML = 'Error al obtener el clima';
          console.error(err);
        });
});