document.addEventListener("DOMContentLoaded", () => {
    const productItems = document.querySelectorAll(".product-item");
    const selectedItems = document.querySelectorAll(".selected-item");

    productItems.forEach(item => {
        item.addEventListener("dragstart", (e) => {
            e.dataTransfer.setData("id", item.getAttribute("data-id"));
            e.dataTransfer.setData("category", item.getAttribute("data-category"));
        });
    });

    selectedItems.forEach(item => {
        item.addEventListener("dragover", (e) => {
            e.preventDefault();
        });

        item.addEventListener("drop", (e) => {
            e.preventDefault();
            const id = e.dataTransfer.getData("id");
            const category = e.dataTransfer.getData("category");
            const targetCategory = item.getAttribute("data-category");

            if (category === targetCategory) {
                window.location.href = `/configurator/configurator/${category}/${id}`;
            } else {
                alert("This product cannot be placed in this category.");
            }
        });
    });

    document.querySelectorAll(".btn-delete").forEach(button => {
    button.addEventListener("click", (e) => {
        e.preventDefault(); // Предотвращаем стандартное поведение ссылки

        const category = button.getAttribute("data-category"); // Категория продукта
        const productId = button.getAttribute("data-id"); // ID продукта

        if (category && productId) {
            // Формируем URL с категорией и ID
            const url = `/configurator/configurator/${category}/${productId}/?delete=True`;
            window.location.href = url;
        } else {
            alert("Error: Product ID or category is missing.");
        }
    });
});
});
