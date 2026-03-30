const CART_KEY = 'the_royal_court_cart';

const cartUtil = {
    getCart() {
        const cart = localStorage.getItem(CART_KEY);
        return cart ? JSON.parse(cart) : [];
    },
    
    saveCart(cart) {
        localStorage.setItem(CART_KEY, JSON.stringify(cart));
        this.updateNavBadge();
        // Dispatch custom event for pages that need to reactive to cart changes
        window.dispatchEvent(new CustomEvent('cartUpdated', { detail: cart }));
    },
    
    addToCart(product) {
        const cart = this.getCart();
        const existing = cart.find(item => item.id === product.id);
        
        if (existing) {
            existing.quantity += 1;
        } else {
            cart.push({
                id: product.id,
                name: product.name,
                price: product.price,
                image: product.image,
                category: product.category,
                quantity: 1
            });
        }
        
        this.saveCart(cart);
        this.showToast(`${product.name} added to cart`);
    },
    
    removeFromCart(productId) {
        const cart = this.getCart().filter(item => item.id !== productId);
        this.saveCart(cart);
    },
    
    updateQuantity(productId, quantity) {
        if (quantity < 1) return this.removeFromCart(productId);
        
        const cart = this.getCart();
        const item = cart.find(item => item.id === productId);
        if (item) {
            item.quantity = quantity;
            this.saveCart(cart);
        }
    },
    
    getCartCount() {
        return this.getCart().reduce((sum, item) => sum + item.quantity, 0);
    },
    
    getCartTotal() {
        return this.getCart().reduce((sum, item) => sum + (item.price * item.quantity), 0);
    },
    
    updateNavBadge() {
        const count = this.getCartCount();
        const badges = document.querySelectorAll('.cart-badge');
        badges.forEach(badge => {
            if (count > 0) {
                badge.textContent = count;
                badge.classList.remove('hidden');
            } else {
                badge.classList.add('hidden');
            }
        });
    },
    
    formatCurrency(amount) {
        return new Intl.NumberFormat('en-IN', {
            style: 'currency',
            currency: 'INR',
            maximumFractionDigits: 0
        }).format(amount);
    },
    
    showToast(message) {
        let container = document.getElementById('toast-container');
        if (!container) {
            container = document.createElement('div');
            container.id = 'toast-container';
            container.className = 'fixed bottom-8 right-8 z-[100] flex flex-col gap-4 pointer-events-none';
            document.body.appendChild(container);
        }
        
        const toast = document.createElement('div');
        toast.className = 'flex items-center gap-4 px-6 py-4 bg-primary text-on-primary rounded-sm shadow-2xl translate-x-12 opacity-0 transition-all duration-500 border-l-4 border-tertiary-fixed-dim pointer-events-auto';
        toast.innerHTML = `<span class="material-symbols-outlined text-xl">shopping_bag</span><span class="font-label text-xs tracking-widest uppercase font-bold">${message}</span>`;
        container.appendChild(toast);
        
        requestAnimationFrame(() => toast.classList.remove('translate-x-12', 'opacity-0'));
        setTimeout(() => {
            toast.classList.add('translate-x-12', 'opacity-0');
            setTimeout(() => toast.remove(), 500);
        }, 3000);
    }
};

// Auto-update badge on load
document.addEventListener('DOMContentLoaded', () => cartUtil.updateNavBadge());
