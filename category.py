import uuid

class Category:
    def __init__(
        self,
        name,
        id = "",
        description = "",
        is_active = True
    ):
        self.id = id or uuid.uuid4()
        self.name = name
        self.description = description
        self.is_active = is_active

        if len(self.name) > 255 :
            raise TypeError("name must have less than 256 characters")

    def __str__(self): #returns when print(instance) is called in terminal
        return f"{self.name} - {self.description} ({self.is_active})"
    
    def __repr_(self): #returns when instance is called in terminal
        return f"<Category {self.name} - {self.description} ({self.is_active})>"