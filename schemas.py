"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

# Example schemas (you can extend these as needed):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Email address")
    address: Optional[str] = Field(None, description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")
    image: Optional[str] = Field(None, description="Primary image URL")
    rating: Optional[float] = Field(4.5, ge=0, le=5, description="Average rating")
    tags: List[str] = Field(default_factory=list, description="Searchable tags")
    trending: bool = Field(False, description="Whether this product is currently trending/viral")

class CartItem(BaseModel):
    product_id: str = Field(..., description="ID of the product")
    title: str = Field(...)
    price: float = Field(..., ge=0)
    quantity: int = Field(..., ge=1)
    image: Optional[str] = None

class CustomerInfo(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    address_line1: str
    address_line2: Optional[str] = None
    city: str
    state: str
    postal_code: str
    country: str

class Order(BaseModel):
    """
    Orders collection schema
    Collection name: "order"
    """
    items: List[CartItem]
    subtotal: float = Field(..., ge=0)
    shipping: float = Field(0, ge=0)
    total: float = Field(..., ge=0)
    customer: CustomerInfo
    status: str = Field("received", description="Order status")

# Note: The Flames database viewer can read these via the /schema endpoint.
