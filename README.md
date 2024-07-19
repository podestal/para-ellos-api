# Trajano API

Trajano is an online store API built with Django and Django Rest Framework (DRF). This API allows managing customers, products, categories, orders, and carts.

## Table of Contents

- Models
- Endpoints
- License

## Models

### Customer
```

user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
address = models.CharField(max_length=255)
phone = models.CharField(max_length=20)

```

### Category
```

name = models.CharField(max_length=255)
description = models.TextField(blank=True, null=True)
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)

```

### Product

```

name = models.CharField(max_length=255)
description = models.TextField()
price = models.DecimalField(max_digits=10, decimal_places=2)
stock = models.IntegerField()
image = models.TextField()
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
category = models.ForeignKey(Category, on_delete=models.PROTECT)

```

### Order

```

customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default='pending'
)

```

### OrderItem

```

order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
product = models.ForeignKey(Product, on_delete=models.CASCADE)
quantity = models.IntegerField()
price = models.DecimalField(max_digits=10, decimal_places=2)

```

### Cart

```

id = models.UUIDField(primary_key=True, default=uuid4)
created_at = models.DateTimeField(auto_now_add=True)

```

### CartItem

```

cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
product = models.ForeignKey(Product, on_delete=models.CASCADE)
quantity = models.PositiveSmallIntegerField()

```

![texto](https://i.ibb.co/LR8Pp7m/Screen-Shot-2024-07-19-at-11-37-26-AM.png)

## Endpoints

