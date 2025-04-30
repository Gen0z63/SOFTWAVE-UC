---
layout: default
title: "Inicio"
---

# Bienvenido a SOFTWAVE-UC 🚀

Somos un equipo enfocado en el desarrollo de soluciones digitales. Aquí encontrarás nuestros proyectos destacados, desarrollos bajo TDD y gestión de datos con ORM.

<h3>🔍 Buscar Proyecto</h3>
<input type="text" id="buscador" placeholder="Buscar por nombre o tecnología..." style="width: 100%; max-width: 400px; padding: 8px; margin-bottom: 1rem;">
<ul id="lista-filtrada"></ul>

<script>
  const buscador = document.getElementById("buscador");
  const contenedor = document.getElementById("lista-filtrada");

  async function cargarYBuscar() {
    const response = await fetch("{{ site.baseurl }}/assets/data/proyectos.json");
    const data = await response.json();

    function render(filtro = "") {
      contenedor.innerHTML = "";
      const resultados = data.filter(p =>
        p.nombre.toLowerCase().includes(filtro) ||
        p.tecnologias.join(', ').toLowerCase().includes(filtro)
      );

      resultados.forEach(p => {
        const li = document.createElement("li");
        li.innerHTML = `<strong>${p.nombre}</strong>: ${p.descripcion}<br><em>${p.tecnologias.join(', ')}</em><br><a href="${p.enlace}" target="_blank">Ver en GitHub</a><hr>`;
        contenedor.appendChild(li);
      });

      if (resultados.length === 0) {
        contenedor.innerHTML = "<li>No se encontraron proyectos.</li>";
      }
    }

    buscador.addEventListener("input", () => {
      render(buscador.value.toLowerCase());
    });

    render();
  }

  cargarYBuscar();
</script>
