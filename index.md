---
layout: default
title: "Inicio"
---

# Bienvenido a SOFTWAVE-UC 🚀

Somos un equipo enfocado en el desarrollo de soluciones digitales. Aquí encontrarás nuestros proyectos destacados, desarrollos bajo TDD y gestión de datos con ORM.

<h2>🔍 Buscar Proyecto</h2>
<input type="text" id="buscador" placeholder="Buscar por nombre o tecnología..." style="width: 100%; max-width: 400px; padding: 8px; margin-bottom: 1rem;">
<ul id="lista-filtrada"></ul>

<script>
  document.addEventListener("DOMContentLoaded", async () => {
    try {
      const response = await fetch("/SOFTWAVE-UC/assets/data/proyectos.json");
      const data = await response.json();
      const buscador = document.getElementById("buscador");
      const lista = document.getElementById("lista-filtrada");

      function render(filtro = "") {
        lista.innerHTML = "";
        const resultados = data.filter(p =>
          p.nombre.toLowerCase().includes(filtro) ||
          p.tecnologias.join(', ').toLowerCase().includes(filtro)
        );

        resultados.forEach(p => {
          const li = document.createElement("li");
          li.innerHTML = `<strong>${p.nombre}</strong>: ${p.descripcion}<br>
            <em>${p.tecnologias.join(', ')}</em><br>
            <a href="${p.enlace}" target="_blank">Ver en GitHub</a><hr>`;
          lista.appendChild(li);
        });

        if (resultados.length === 0) {
          lista.innerHTML = "<li>No se encontraron proyectos.</li>";
        }
      }

      buscador.addEventListener("input", () => {
        render(buscador.value.toLowerCase());
      });

      // Mostrar todo al inicio
      render();

    } catch (error) {
      console.error("Error al cargar proyectos:", error);
      document.getElementById("lista-filtrada").innerHTML = "<li>Error al cargar proyectos.</li>";
    }
  });
</script>
