# Схемы для валидации

get_single_user_schema = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "email": {"type": "string"},
                "first_name": {"type": "string"},
                "last_name": {"type": "string"},
                "avatar": {"type": "string"}
            },
            "required": ["id", "email", "first_name", "last_name", "avatar"]
        },
        "support": {"type": "object"}
    },
    "required": ["data", "support"]
}

create_user_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "id": {"type": "string"},
        "createdAt": {"type": "string"}
    },
    "required": ["name", "job", "id", "createdAt"]
}

update_user_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "updatedAt": {"type": "string"}
    },
    "required": ["name", "job", "updatedAt"]
}

error_schema = {
    "type": "object",
    "properties": {
        "error": {"type": "string"}
    },
    "required": ["error"]
}