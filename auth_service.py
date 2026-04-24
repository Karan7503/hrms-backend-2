from db import users_collection


DEMO_USERS = [
    {
        "email": "admin@iperitus.com",
        "password": "admin123",
        "name": "Admin",
        "role": "admin"
    },
    {
        "email": "employee@iperitus.com",
        "password": "emp123",
        "name": "Employee",
        "role": "employee"
    }
]


def seed_demo_users():
    """Seed default users if they don't exist."""
    for u in DEMO_USERS:
        if not users_collection.find_one({"email": u["email"]}):
            users_collection.insert_one(u.copy())
            print(f"[Auth] Seeded user: {u['email']}")
        else:
            print(f"[Auth] User already exists: {u['email']}")


def authenticate_user(email, password):
    user = users_collection.find_one({"email": email})

    if not user:
        return {"success": False, "message": "User not found"}

    if user["password"] == password:
        return {
            "success": True,
            "user": {
                "email": user["email"],
                "name": user["name"],
                "role": user.get("role", "employee")
            }
        }

    return {"success": False, "message": "Invalid credentials"}
