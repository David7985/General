const botonesDiv = document.getElementById('botones');
const infoDiv = document.getElementById('info');

// Fetch al PHP para obtener el JSON
fetch('multiplicadores.php')
  .then(res => res.json())
  .then(data => {
    data.forEach(m => {
      const btn = document.createElement('button');
      btn.textContent = m.nombre;

      btn.addEventListener('mouseover', () => {
        infoDiv.innerHTML = `
          <p><strong>Nombre:</strong> ${m.nombre}</p>
          <p><strong>Categoría:</strong> ${m.categoria}</p>
          <p><strong>Descripción:</strong> ${m.descripcion}</p>
        `;
      });

      botonesDiv.appendChild(btn);
    });
  })
  .catch(err => {
    infoDiv.innerHTML = "Error al cargar los multiplicadores";
    console.error(err);
  });
