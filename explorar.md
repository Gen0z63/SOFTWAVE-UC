---
layout: default
title: "Explorar Proyectos"
---

<h1>Explorar Proyectos 🚀</h1>

<input type="text" id="buscador" placeholder="Buscar por nombre o tecnología...">
<ul id="lista-proyectos"></ul>

<script>
  async function cargarProyectos() {
    const response = await fetch("{{ site.baseurl }}/assets/data/proyectos.json");
    const data = await response.json();
    const lista = document.getElementById("lista-proyectos");
    const buscador = document.getElementById("buscador");

    function renderizar(filtro = "") {
      lista.innerHTML = "";
      const resultados = data.filter(p =>
        p.nombre.toLowerCase().includes(filtro) ||
        p.tecnologias.join(', ').toLowerCase().includes(filtro)
      );
      resultados.forEach(p => {
        const li = document.createElement("li");
        li.innerHTML = `<strong>${p.nombre}</strong> - ${p.descripcion} <br><em>${p.tecnologias.join(', ')}</em>`;
        lista.appendChild(li);
      });
    }

    buscador.addEventListener("input", () => {
      renderizar(buscador.value.toLowerCase());
    });

    renderizar();
  }

  cargarProyectos();
</script>

