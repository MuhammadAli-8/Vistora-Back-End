# Django API Project

This project provides a RESTful API for managing a variety of models,
including `Product`, `Review`, `SuppliesOrder`, `Supplier`, `Shipping`, and `Payment`. It uses Django REST Framework (
DRF) to create flexible and extensible APIs.

## Features

- CRUD operations for all models.
- Relationship management between models.
- API endpoints implemented using `ModelViewSet`.
- JSON serialization and validation with DRF serializers.

---

## Requirements

### Prerequisites

- Python 3.8+
- Django 4.x
- Django REST Framework 3.x

### Install Dependencies

```bash
pip install django djangorestframework
```

---

## Models

### Product

Manages information about products.
Fields:

- `id` (Primary Key)
- `name`
- `description`
- `price`
- `stock_quantity`

### Review

Manages user reviews for products.
Fields:

- `id` (Primary Key)
- `user` (ForeignKey to `User`)
- `product` (ForeignKey to `Product`)
- `rating`
- `comment`

### SuppliesOrder

Manages orders placed by users.
Fields:

- `id` (Primary Key)
- `user` (ForeignKey to `User`)
- `order_date`
- `order_status`

### Shipping

Tracks shipping information.
Fields:

- `id` (Primary Key)
- `order` (ForeignKey to `SuppliesOrder`)
- `shipping_date`
- `delivery_date`
- `tracking_number`
- `provider_name`

### Payment

Tracks payment details.
Fields:

- `payment_id` (Primary Key)
- `order` (ForeignKey to `SuppliesOrder`)
- `payment_status`
- `payment_date`
- `amount`

---

## API Endpoints

### Base URL

```
http://<your-server>/api/
```

### Endpoints

| Endpoint          | HTTP Methods     | Description                            |
|-------------------|------------------|----------------------------------------|
| `/products/`      | GET, POST        | List and create products               |
| `/products/<id>/` | GET, PUT, DELETE | Retrieve, update, delete product       |
| `/reviews/`       | GET, POST        | List and create reviews                |
| `/reviews/<id>/`  | GET, PUT, DELETE | Retrieve, update, delete review        |
| `/orders/`        | GET, POST        | List and create orders                 |
| `/orders/<id>/`   | GET, PUT, DELETE | Retrieve, update, delete order         |
| `/shipping/`      | GET, POST        | List and create shipping info          |
| `/shipping/<id>/` | GET, PUT, DELETE | Retrieve, update, delete shipping info |
| `/payments/`      | GET, POST        | List and create payments               |
| `/payments/<id>/` | GET, PUT, DELETE | Retrieve, update, delete payment       |

---

## Installation

1. **Clone the Repository**

```bash
git clone https://github.com/MuhammadAli-8/SWE
cd <repository-folder>
```

2. **Set Up the Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Apply Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Run the Server**

```bash
python manage.py runserver
```

---

## Usage

- Use an API testing tool like Postman or cURL to interact with the API.
- Example request to create a product:

```bash
POST /api/products/
Content-Type: application/json

{
  "name": "Example Product",
  "description": "A sample product.",
  "price": 100.00,
  "stock_quantity": 50
}
```

---

## Testing

To run tests:

```bash
python manage.py test
```

---

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---
