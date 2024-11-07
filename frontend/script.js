
async function displayProducts() {
    try {
        const response = await fetch('http://localhost:3000/api/products');
        const products = await response.json();

        const productContainer = document.getElementById('product-container');
        productContainer.innerHTML = '';

        products.forEach(product => {
            const productElement = document.createElement('div');
            productElement.className = 'product';

            productElement.innerHTML = `
                <h2>${product.name}</h2>
                <p>${product.description}</p>
                <p>Preço: $${product.Preço}</p>
                ${product.imageURL ? `<img src="${product.imageURL}" alt="${product.name}" />` : ''}
            `;

            productContainer.appendChild(productElement);
        });
    } catch (error) {
        console.error('Error fetching products:', error);
    }
}

async function displayProducts() {
    try {
        const response = await fetch('http://localhost:3000/api/products');
        const products = await response.json();

        const productContainer = document.getElementById('product-container');

        productContainer.innerHTML = '';
        products.forEach(product => {
            const productElement = document.createElement('div');
            productElement.className = 'product';
            productElement.innerHTML = `
                <h2>${product.name}</h2>
                <p>${product.description}</p>
                <p>Preço: $${product.Preço}</p>
                ${product.imageURL ? `<img src="${product.imageURL}" alt="${product.name}" />` : ''}
                <button onclick="addToCart(${product.id})">Adicionar ao Carrinho</button>
            `;

            productContainer.appendChild(productElement);
        });
    } catch (error) {
        console.error('Error fetching products:', error);
    }
}

function addToCart(productId) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    const existingProduct = cart.find(item => item.id === productId);

    if (existingProduct) {
        existingProduct.quantity += 1;
    } else {
        cart.push({ id: productId, quantity: 1 });
    }

    localStorage.setItem('cart', JSON.stringify(cart));

    showPopup("Item adicionado ao carrinho!");

    displayCartItems();
    updateCartCount();
}

async function displayCartItems() {
    const cartContainer = document.getElementById('cart-items');
    cartContainer.innerHTML = ''; // Clear existing content

    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    if (cart.length === 0) {
        cartContainer.innerHTML = '<p>Seu carrinho esta vazio!</p>';
        document.getElementById('cart-total').textContent = '';
        return;
    }

    const response = await fetch('http://localhost:3000/api/products');
    const products = await response.json();

    let total = 0;
    cart.forEach(cartItem => {
        const product = products.find(p => p.id === cartItem.id);
        const itemTotal = product.Preço * cartItem.quantity;
        total += itemTotal;

        const cartItemElement = document.createElement('div');
        cartItemElement.className = 'cart-item';

        cartItemElement.innerHTML = `
            <h3>${product.name}</h3>
            <p>Preço: $${product.Preço}</p>
            <p>Quantity: ${cartItem.quantity}</p>
            <p>Subtotal: $${itemTotal.toFixed(2)}</p>
            <button onclick="removeFromCart(${product.id})">Remover</button>
        `;

        cartContainer.appendChild(cartItemElement);
    });

    document.getElementById('cart-total').textContent = `Total: $${total.toFixed(2)}`;
}

function removeFromCart(productId) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];

    const productIndex = cart.findIndex(item => item.id === productId);

    if (productIndex !== -1) {
        if (cart[productIndex].quantity > 1) {
            cart[productIndex].quantity -= 1;
        } else {
            cart.splice(productIndex, 1);
        }
    }

    localStorage.setItem('cart', JSON.stringify(cart));

    displayCartItems();
    updateCartCount();
}

function updateCartCount() {
    
    const cart = JSON.parse(localStorage.getItem('cart')) || [];

    const itemCount = cart.reduce((total, item) => total + item.quantity, 0);

    const cartCountElement = document.getElementById('cart-count');
    cartCountElement.textContent = itemCount;
}

function toggleCart() {
    const cartTab = document.getElementById('cart-tab');
    cartTab.classList.toggle('open');
    if (cartTab.classList.contains('open')) {
        displayCartItems();
    }
}

function showPopup(message) {
    const popup = document.getElementById('popup');
    popup.textContent = message;
    popup.classList.add('show');

    
    setTimeout(() => {
        popup.classList.remove('show');
    }, 2000);
}



displayProducts();
viewCart();
updateCartCount();
