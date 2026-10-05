document.addEventListener("DOMContentLoaded", function() {
    const inventarioPasteles = [
    {"nombre": "Manjar Nuez", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "pasteles.html", "precio": "$25.000"},
    {"nombre": "Manjar Piña", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "pasteles.html", "precio": "$25.000"},
    {"nombre": "Francisca", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "pasteles.html", "precio": "$25.000"},
    {"nombre": "Torta Mixta", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "pasteles.html", "precio": "$25.000"},
    {"nombre": "Chocolate", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "pasteles.html", "precio": "$25.000"},
    {"nombre": "Torta de Manjarate", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "pasteles.html", "precio": "$25.000"},
    {"nombre": "Turrón De Nuez", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "pasteles.html", "precio": "$25.000"},
    {"nombre": "Torta Oreo", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "pasteles.html", "precio": "$25.000"},
    {"nombre": "Tres leches", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "pasteles.html", "precio": "$25.000"},
    {"nombre": "Pompadour", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "pasteles.html", "precio": "$25.000"},
    {"nombre": "Dulce Margarita", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "pasteles.html", "precio": "$25.000"},
    {"nombre": "Cuatro leches", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "pasteles.html", "precio": "$25.000"},
    {"nombre": "Danesa", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "pasteles.html", "precio": "$25.000"},
    {"nombre": "Cielo", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "pasteles.html", "precio": "$25.000"},
    {"nombre": "Chifón", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "pasteles.html", "precio": "$25.000"},
    {"nombre": "Torta helada", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "pasteles.html", "precio": "$25.000"},
    {"nombre": "Papaya a la crema", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "pasteles.html", "precio": "$25.000"},
    {"nombre": "Torta de durazno", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "pasteles.html", "precio": "$25.000"},
    {"nombre": "Tentación", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "premium.html", "precio": "$30.000"},
    {"nombre": "Caluga (vainilla o chocolate)", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "premium.html", "precio": "$30.000"},
    {"nombre": "Alejandra", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "premium.html", "precio": "$30.000"},
    {"nombre": "Amapola", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "premium.html", "precio": "$30.000"},
    {"nombre": "Encanto", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "premium.html", "precio": "$30.000"},
    {"nombre": "Torta panqueques", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "premium.html", "precio": "$30.000"},
    {"nombre": "Cinco leches", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "premium.html", "precio": "$30.000"},
    {"nombre": "Silvia", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "premium.html", "precio": "$30.000"},
    {"nombre": "Oreo frambuesa", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "premium.html", "precio": "$30.000"},
    {"nombre": "Crocante de Nuez", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "premium.html", "precio": "$30.000"},
    {"nombre": "Torta Amapola", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "premium.html", "precio": "$30.000"},
    {"nombre": "Torta Tres Leches Pastelera Frambuesa", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "premium.html", "precio": "$30.000"},
    {"nombre": "Pastelitos para coctel", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "dulces.html", "precio": "$15.000"},
    {"nombre": "Tartaletas Variedades", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "dulces.html", "precio": "$15.000"},
    {"nombre": "Queque Variedades", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "dulces.html", "precio": "$15.000"},
    {"nombre": "Pie Variedades", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&q=80", "url": "dulces.html", "precio": "$15.000"}
];

    const isInProductos = window.location.pathname.includes('/productos/');
    const prefix = isInProductos ? '../' : '';

    const overlay = document.createElement("div");
    overlay.id = "overlay-buscador";
    overlay.style.display = "none";
    overlay.style.position = "fixed";
    overlay.style.top = "0";
    overlay.style.left = "0";
    overlay.style.width = "100%";
    overlay.style.height = "100%";
    overlay.style.backgroundColor = "rgba(255, 255, 255, 0.97)";
    overlay.style.backdropFilter = "blur(5px)";
    overlay.style.zIndex = "9999";
    overlay.style.flexDirection = "column";
    overlay.style.alignItems = "center";
    overlay.style.paddingTop = "10vh";
    overlay.style.overflowY = "auto";

        overlay.innerHTML = `
            <span id="cerrar-buscador" style="position: absolute; top: 30px; right: 50px; font-size: 3rem; cursor: pointer; color: #4a2c2a; line-height: 1;">&times;</span>
            <h2 style="font-family: 'Playfair Display', serif; font-size: 2.5rem; color: #4a2c2a; margin-bottom: 30px;">Descubrir Pasteles</h2>
            <input type="text" id="input-buscador-overlay" placeholder="Buscar por nombre, ej. Chocolate..." autocomplete="off" style="width: 80%; max-width: 600px; padding: 15px 20px; font-size: 1.5rem; border: none; border-bottom: 2px solid #e8869a; background: transparent; outline: none; text-align: center; font-family: 'Montserrat', sans-serif; color: #4a2c2a;">
            <div id="resultados-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 40px; width: 90%; max-width: 1200px; margin-top: 60px; padding-bottom: 60px;"></div>
        `;

        document.body.appendChild(overlay);

        const inputOverlay = document.getElementById("input-buscador-overlay");
        const grid = document.getElementById("resultados-grid");
        const btnAbrir = document.getElementById("abrir-buscador");
        const btnCerrar = document.getElementById("cerrar-buscador");

        let resultadosActuales = [];

        if(btnAbrir) {
            btnAbrir.addEventListener("click", function() {
                overlay.style.display = "flex";
                inputOverlay.value = "";
                grid.innerHTML = "";
                setTimeout(() => inputOverlay.focus(), 100);
                document.body.style.overflow = "hidden";
            
});
        }

        if(btnCerrar) {
            btnCerrar.addEventListener("click", function() {
                overlay.style.display = "none";
                document.body.style.overflow = "auto";
            });
        }

        if(inputOverlay) {
            inputOverlay.addEventListener("input", function() {
                const query = this.value.toLowerCase().trim();
                grid.innerHTML = "";
                
                if (query.length === 0) {
                    resultadosActuales = [];
                    return;
                }

                resultadosActuales = inventarioPasteles.filter(r => r.nombre.toLowerCase().includes(query));
                
                if (resultadosActuales.length > 0) {
                    resultadosActuales.forEach(pastel => {
                        const card = document.createElement("div");
                        card.className = "pastel-card";
                        
                        card.style.display = "flex";
                        card.style.flexDirection = "column";
                        card.style.justifyContent = "space-between";
                        card.style.width = "100%";
                        card.style.height = "100%";
                        
                        card.innerHTML = `
                            <img src="${pastel.img}" alt="${pastel.nombre}" style="width: 100%; height: 200px; object-fit: cover;">
                            <div style="padding: 15px; display: flex; flex-direction: column; flex-grow: 1;">
                                <h3 style="margin-bottom: 5px;">${pastel.nombre}</h3>
                                <p style="font-weight: bold; margin-top: 10px;">${pastel.precio}</p>
                                <button class="btn-oscuro" style="margin-top: 15px;">Comprar Ahora</button>
                            </div>
                        `;
                        grid.appendChild(card);
                    });
                } else {
                grid.innerHTML = `<div style="grid-column: 1 / -1; text-align: center; color: #777; font-size: 1.1rem; padding: 40px;">No encontramos ninguna pieza con ese nombre.</div>`;
            }
        });

        inputOverlay.addEventListener("keydown", function(e) {
            if (e.key === "Enter") {
                e.preventDefault();
                if (resultadosActuales.length > 0) {
                    window.location.href = prefix + resultadosActuales[0].url;
                }
            }
        });
    }
    
    document.addEventListener("keydown", function(e) {
        if (e.key === "Escape" && overlay.style.display === "flex") {
            overlay.style.display = "none";
            document.body.style.overflow = "auto";
        }
    });

    // Close overlay when adding to cart
    document.addEventListener("click", function(e) {
        if (e.target.closest("button.btn-oscuro") && overlay.style.display === "flex") {
            overlay.style.display = "none";
            document.body.style.overflow = "auto";
        }
    });
});
