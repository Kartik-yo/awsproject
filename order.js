const express = require('express');
const app = express();
app.use(express.json());

// Dummy database
let orders = [
    { id: 1, user_id: 1, product: "Laptop", quantity: 1 },
    { id: 2, user_id: 2, product: "Phone", quantity: 2 }
];

// Get all orders
app.get('/orders', (req, res) => {
    res.json(orders);
});

// Get order by ID
app.get('/orders/:id', (req, res) => {
    const order = orders.find(o => o.id === parseInt(req.params.id));
    if (order) return res.json(order);
    res.status(404).json({ error: "Order not found" });
});

// Create a new order
app.post('/orders', (req, res) => {
    const { user_id, product, quantity } = req.body;
    const newOrder = { id: orders.length + 1, user_id, product, quantity };
    orders.push(newOrder);
    res.status(201).json(newOrder);
});

app.listen(5001, () => console.log('Order Service running on port 5001'));


