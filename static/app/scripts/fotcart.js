let cartItems = [];
function addToCart(item) {
    // Проверяем, есть ли уже такой товар в корзине
    let existingItem = cartItems.find((i) => i.id === item.id);
    if (existingItem) {
        // Если есть, увеличиваем количество
        existingItem.quantity++;
    } else {
        // Если нет, добавляем новый товар в корзину
        cartItems.push({ ...item, quantity: 1 });
    }
    // Обновляем список товаров в корзине
    updateCart();
}
function updateCart() {
    let cartList = document.getElementById("cart-items");
    let total = 0;
    cartList.innerHTML = "";
    cartItems.forEach((item) => {
        let li = document.createElement("li");
        li.innerText = ${ item.title } x ${ item.quantity } = ${ item.price * item.quantity } руб.;
        cartList.appendChild(li);
        total += item.price * item.quantity;
    });
    let totalLi = document.createElement("li");
    totalLi.innerText = Итого: ${ total } руб.;
    cartList.appendChild(totalLi);
}
function sendOrder() {
    let order = {
        items: cartItems,
        total: getTotal(),
        date: new Date(),
    };
    fetch("https://my-server.com/orders", {
        method: "POST",
        body: JSON.stringify(order),
    })
        .then((response) => response.json())
        .then((data) => {
            // Очищаем корзину
            cartItems = [];
            updateCart();
            alert("Заказ успешно оформлен!");
        })
        .catch((error) => {
            alert("Ошибка при оформлении заказа!");
        });
}
function getTotal() {
    let total = 0;
    cartItems.forEach((item) => {
        total += item.price * item.quantity;
    });
    return total;
}
