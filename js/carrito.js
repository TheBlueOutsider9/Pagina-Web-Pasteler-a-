document.addEventListener("DOMContentLoaded", function() {
    try {
        const isInProductos = window.location.pathname.includes('/productos/');
        const prefix = isInProductos ? '../' : '';

        const carritoHTML = `
        <div id="carrito-panel" class="carrito-panel">
            <div class="carrito-header">
                <h2 style="font-family: 'Inter', sans-serif; color: var(--texto); margin: 0; font-weight: 300; letter-spacing: 1px;">Tu Carrito</h2>
                <span class="cerrar-carrito" id="cerrar-carrito" style="cursor: pointer; font-size: 2rem; line-height: 1; color: var(--texto);">&times;</span>
            </div>
            <div id="carrito-items" style="flex: 1; display: flex; flex-direction: column; gap: 15px; margin-bottom: 20px;">
            </div>
            <div class="carrito-footer" style="border-top: 1px solid var(--borde); padding-top: 20px;">
                <div style="display: flex; justify-content: space-between; font-weight: bold; font-size: 1.2rem; color: var(--texto); margin-bottom: 20px;">
                    <span>Total:</span>
                    <span id="carrito-total">.00</span>
                </div>
                <button id="btn-comprar-carrito-final" class="btn-oscuro" style="width: 100%; padding: 15px; font-size: 1rem; font-weight: bold;">PROCEDER AL PAGO</button>
            </div>
        </div>
        <div id="carrito-overlay" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 999;"></div>
        `;
        
        document.body.insertAdjacentHTML('beforeend', carritoHTML);

        const panel = document.getElementById("carrito-panel");
        const overlay = document.getElementById("carrito-overlay");
        const btnCerrar = document.getElementById("cerrar-carrito");
        const itemsContainer = document.getElementById("carrito-items");
        const totalElement = document.getElementById("carrito-total");
        const btnComprarFinal = document.getElementById("btn-comprar-carrito-final");

        // Safely attach to cart icon (using ID to avoid innerText crashes on SVGs)
        const navCartBtn = document.getElementById('btn-carrito');
        if(navCartBtn) {
            navCartBtn.style.cursor = "pointer";
            navCartBtn.style.position = "relative";
            
            const badge = document.createElement("span");
            badge.className = "carrito-badge-js";
            badge.style.position = "absolute";
            badge.style.top = "-8px";
            badge.style.right = "-12px";
            badge.style.backgroundColor = "var(--acento)";
            badge.style.color = "#fff";
            badge.style.fontSize = "0.7rem";
            badge.style.fontWeight = "bold";
            badge.style.borderRadius = "50%";
            badge.style.padding = "2px 6px";
            badge.style.display = "none";
            badge.style.boxShadow = "0 2px 4px rgba(0,0,0,0.2)";
            
            navCartBtn.appendChild(badge);
            navCartBtn.addEventListener("click", function() { if(window.abrirCarrito) window.abrirCarrito(); });
        }
        
        function actualizarBadges() {
            let totalItems = 0;
            carrito.forEach(item => totalItems += item.cantidad);
            
            const badges = document.querySelectorAll('.carrito-badge-js');
            badges.forEach(badge => {
                if (totalItems > 0) {
                    badge.textContent = totalItems;
                    badge.style.display = "inline-block";
                } else {
                    badge.style.display = "none";
                }
            });
        }

        window.abrirCarrito = function() {
            panel.classList.add("abierto");
            overlay.style.display = "block";
            window.renderCarrito();
        }

        function cerrarCarrito() {
            panel.classList.remove("abierto");
            overlay.style.display = "none";
        }

        if(btnCerrar) btnCerrar.addEventListener("click", function(){ cerrarCarrito(); });
        if(overlay) overlay.addEventListener("click", function(){ cerrarCarrito(); });

        let carrito = JSON.parse(localStorage.getItem('zafiro_carrito')) || [];

        function guardarCarrito() {
            localStorage.setItem('zafiro_carrito', JSON.stringify(carrito));
        }

        function parsePrecio(precioStr) {
            if(!precioStr) return 0;
            // Handle any backticks or weird spaces
            let cleanStr = precioStr.replace(/[^0-9,.]/g, '');
            return parseFloat(cleanStr.replace('.', '').replace(',', '.'));
        }
        function formatPrecio(precioNum) {
            if(isNaN(precioNum)) return "";
            return '$' + Math.round(precioNum).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
        }

        window.modificarCantidad = function(nombre, delta) {
            const item = carrito.find(i => i.nombre === nombre);
            if (item) {
                item.cantidad += delta;
                if (item.cantidad <= 0) {
                    carrito = carrito.filter(i => i.nombre !== nombre);
                }
                guardarCarrito();
                window.renderCarrito();
            }
        };

        window.eliminarItem = function(nombre) {
            carrito = carrito.filter(i => i.nombre !== nombre);
            guardarCarrito();
            window.renderCarrito();
        };

        window.renderCarrito = function() {
            itemsContainer.innerHTML = "";
            let total = 0;

            if (carrito.length === 0) {
                itemsContainer.innerHTML = "<p style='text-align: center; color: #777; margin-top: 50px;'>Tu carrito está vacío.</p>";
                totalElement.textContent = "";
                actualizarBadges();
                return;
            }

            carrito.forEach(item => {
                const subtotal = item.precioNum * item.cantidad;
                total += subtotal;

                const div = document.createElement("div");
                div.style.display = "flex";
                div.style.alignItems = "center";
                div.style.gap = "15px";
                div.style.borderBottom = "1px solid var(--borde)";
                div.style.paddingBottom = "15px";

                let imgSrc = item.img;
                if(imgSrc && !imgSrc.startsWith('http') && prefix) {
                    imgSrc = prefix + imgSrc;
                }

                div.innerHTML = `
                    <img src="${imgSrc}" style="width: 60px; height: 60px; object-fit: cover; border-radius: 4px; border: 1px solid var(--borde);">
                    <div style="flex: 1;">
                        <div style="font-weight: bold; font-family: 'Inter', sans-serif; color: var(--texto); font-size: 0.95rem;">${item.nombre}</div>
                        <div style="color: var(--acento); font-size: 0.85rem; margin-bottom: 8px;">${formatPrecio(item.precioNum)}</div>
                        <div style="display: flex; align-items: center; gap: 10px;">
                            <button onclick="modificarCantidad('${item.nombre}', -1)" style="border: 1px solid #ccc; background: transparent; width: 25px; height: 25px; cursor: pointer; border-radius: 50%; display: flex; align-items: center; justify-content: center;">-</button>
                            <span style="font-size: 0.9rem; font-weight: bold;">${item.cantidad}</span>
                            <button onclick="modificarCantidad('${item.nombre}', 1)" style="border: 1px solid #ccc; background: transparent; width: 25px; height: 25px; cursor: pointer; border-radius: 50%; display: flex; align-items: center; justify-content: center;">+</button>
                        </div>
                    </div>
                    <button onclick="eliminarItem('${item.nombre}')" style="background: transparent; border: none; font-size: 1.2rem; color: #999; cursor: pointer; padding: 5px;">&times;</button>
                `;
                itemsContainer.appendChild(div);
            });

            
            

            
            // Cálculo de costo de envío según la comuna
            let costoEnvio = 0;
            let comunaEnvio = "";
            const tarifasDelivery = {
                "Machali": 1500,
                "Rancagua": 2500
            };

            carrito.forEach(item => {
                const match = item.nombre.match(/Delivery: (Machali|Rancagua)/);
                if (match) {
                    comunaEnvio = match[1];
                    costoEnvio = tarifasDelivery[comunaEnvio];
                }
            });

            if (costoEnvio > 0) {
                total += costoEnvio;
                const divEnvio = document.createElement("div");
                divEnvio.style.display = "flex";
                divEnvio.style.alignItems = "center";
                divEnvio.style.gap = "15px";
                divEnvio.style.borderBottom = "1px solid var(--borde)";
                divEnvio.style.paddingBottom = "15px";
                
                divEnvio.innerHTML = `
                    <div style="width: 60px; height: 60px; border-radius: 4px; display: flex; align-items: center; justify-content: center; background: var(--borde);">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--texto)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="3" width="15" height="13"></rect><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"></polygon><circle cx="5.5" cy="18.5" r="2.5"></circle><circle cx="18.5" cy="18.5" r="2.5"></circle></svg>
                    </div>
                    <div style="flex: 1;">
                        <p style="font-weight: bold; margin: 0; font-size: 0.95rem; color: var(--texto);">Despacho a Domicilio</p>
                        <p style="margin: 3px 0 0 0; font-size: 0.85rem; color: #666;">Comuna: ${comunaEnvio}</p>
                    </div>
                    <div style="font-weight: bold; color: var(--acento);">
                        ${formatPrecio(costoEnvio)}
                    </div>
                `;
                itemsContainer.appendChild(divEnvio);
            }

            totalElement.textContent = formatPrecio(total);
            actualizarBadges();
        }

        if(btnComprarFinal) {
            btnComprarFinal.addEventListener("click", function() {
                if (carrito.length === 0) {
                    alert("Tu carrito está vacío. Agrega una pieza antes de proceder al pago.");
                    return;
                }
                
                const numeroWhatsApp = '56986235441'; 
                let mensaje = "Hola, me gustaría concretar la compra de los siguientes artículos:\n\n";
                let totalCarrito = 0;
                
                carrito.forEach(item => {
                    const subtotal = item.precioNum * item.cantidad;
                    totalCarrito += subtotal;
                    mensaje += `- ${item.nombre} x ${item.cantidad} (${formatPrecio(subtotal)})\n`;
                });
                
                mensaje += `\n*Total a pagar: ${formatPrecio(totalCarrito)}*\n\nQuedo atento a las instrucciones para el pago y envío.`;
                
                const urlWhatsApp = `https://wa.me/${numeroWhatsApp}?text=${encodeURIComponent(mensaje)}`;
                window.open(urlWhatsApp, '_blank');
                
                carrito = [];
                guardarCarrito();
                window.renderCarrito();
                cerrarCarrito();
            });
        }

        
        window.agregarItemAlCarritoPersonalizado = function(nombre, precioNum, img) {
            const itemExistente = carrito.find(i => i.nombre === nombre);
            if (itemExistente) {
                itemExistente.cantidad++;
            } else {
                carrito.push({ nombre, precioNum, img, cantidad: 1 });
            }
            guardarCarrito();
            actualizarBadges();
            window.renderCarrito();
            window.abrirCarrito();
        };
        
        // AGREGAR AL CARRITO EVENT DELEGATION: THE BULLETPROOF WAY
        document.addEventListener('click', function(e) {
            // Only trigger if clicking a button with .btn-oscuro (which are all our "Comprar Ahora" buttons)
            const btn = e.target.closest('button.btn-oscuro');
            if (!btn) return;
            
            // Ignore the "PROCEDER AL PAGO" button in the cart
            if(btn.id === 'btn-comprar-carrito-final') return;

            e.preventDefault();

            let card = btn.closest('.pastel-card');
            let nombre, precioStr, img;

            // Scenario 1: Catalog View (.pastel-card exists)
            if (card) {
                const h3 = card.querySelector('h3');
                if (h3) nombre = h3.textContent.trim();
                
                const pTags = card.querySelectorAll('p');
                pTags.forEach(p => { 
                    if(p.textContent.includes('$')) precioStr = p.textContent.trim(); 
                });
                
                const imgEl = card.querySelector('img');
                if (imgEl) {
                    img = imgEl.getAttribute('src');
                    if (img && img.startsWith('../')) img = img.substring(3);
                }
            } 
            // Scenario 2: Individual Product Page
            else {
                const h1 = document.querySelector('h1');
                if(h1) nombre = h1.textContent.trim();
                
                const pTags = document.querySelectorAll('p');
                pTags.forEach(p => { 
                    if(p.textContent.includes('$')) precioStr = p.textContent.trim(); 
                });
                
                const imgTag = document.querySelector('section img');
                if(imgTag) {
                    img = imgTag.getAttribute('src');
                    if (img && img.startsWith('../')) img = img.substring(3);
                }
            }

            if (nombre && precioStr && img) {
                const precioNum = parsePrecio(precioStr);
                const itemExistente = carrito.find(i => i.nombre === nombre);
                if (itemExistente) {
                    itemExistente.cantidad++;
                } else {
                    carrito.push({ nombre, precioNum, img, cantidad: 1 });
                }
                
                guardarCarrito();
                actualizarBadges();
                window.abrirCarrito();
                
                // Visual Feedback
                const txtOriginal = btn.textContent;
                btn.textContent = "¡AÑADIDO!";
                btn.style.backgroundColor = "var(--texto)";
                setTimeout(() => {
                    btn.textContent = txtOriginal;
                    btn.style.backgroundColor = "";
                }, 1500);
            } else {
                console.error("No se pudo agregar el producto. Faltan datos:", {nombre, precioStr, img});
                alert("Error al añadir el producto. Faltan datos en la página.");
            }
        });
        
        actualizarBadges();
    } catch(err) {
        console.error("Error inicializando carrito:", err);
    }
});