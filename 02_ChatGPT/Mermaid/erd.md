<!-- 쇼핑몰 사이트 ERD 다이어그램 mermaid로 그려줘 -->

```mermaid
erDiagram
    MEMBER ||--o{ CART : "보유"
    MEMBER ||--o{ ORDER : "주문"
    MEMBER ||--o{ REVIEW : "작성"

    PRODUCT ||--o{ CART_ITEM : "포함"
    PRODUCT ||--o{ ORDER_ITEM : "주문됨"
    PRODUCT ||--o{ REVIEW : "리뷰대상"

    CART ||--o{ CART_ITEM : "포함"
    ORDER ||--o{ ORDER_ITEM : "포함"
    ORDER ||--|{ PAYMENT : "결제정보"
    ORDER ||--|{ DELIVERY : "배송정보"

    MEMBER {
        int member_id PK
        string username
        string password
        string email
        string phone
        datetime join_date
    }

    PRODUCT {
        int product_id PK
        string name
        string description
        float price
        int stock
        datetime reg_date
    }

    CART {
        int cart_id PK
        int member_id FK
        datetime created_at
    }

    CART_ITEM {
        int cart_item_id PK
        int cart_id FK
        int product_id FK
        int quantity
    }

    ORDER {
        int order_id PK
        int member_id FK
        datetime order_date
        string status
        float total_amount
    }

    ORDER_ITEM {
        int order_item_id PK
        int order_id FK
        int product_id FK
        int quantity
        float price
    }

    PAYMENT {
        int payment_id PK
        int order_id FK
        string method
        string status
        datetime payment_date
    }

    DELIVERY {
        int delivery_id PK
        int order_id FK
        string address
        string status
        datetime shipped_date
    }

    REVIEW {
        int review_id PK
        int member_id FK
        int product_id FK
        int rating
        string comment
        datetime created_at
    }
```