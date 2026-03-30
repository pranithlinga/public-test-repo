# API Reference

## Endpoints

### GET /users
Returns all users.

### GET /products
Returns all products. Supports `?category=` filter.

### POST /orders
Create a new order. Requires `user_id`, `product_id`, `quantity`.

### GET /orders/:id
Get order details by ID.
