from dataclasses import dataclass, field
from uuid import UUID
import uuid

@dataclass
class Category:
    name: str
    description: str = ""
    is_active: bool = True
    id: UUID = field(default_factory=uuid.uuid4)
    # não poderia ser id: uuid.uuid4() pq assim ele criaria um valor usaria sempre o mesmo em todos os objetos
    # usando o field e default_factory, ele permite indicar a função que fornecerá o valor do campo a cada instanciação

    def __post_init__(self):
        self.validate()

    def validate(self):
        if len(self.name) > 255:
            raise ValueError("name cannot be longer than 255 characters")
        
        if not self.name: #checks for empty string or null object
            raise ValueError("name cannot be empty")

    
    def update_category(self, name, description):
        self.name = name
        self.description = description

        self.validate()

    def activate(self):
        self.is_active = True

        self.validate()

    def deactivate(self):
        self.is_active = False

        self.validate()
    
    def __str__(self): #returns when print(instance) is called in terminal
        return f"{self.name} - {self.description} ({self.is_active})"
    
    def __repr__(self): #returns when instance is called in terminal
        return f"<Category {self.name} - {self.description} ({self.is_active})>"

    def __eq__(self, other):
        if not isinstance(other, Category):
            return False
        return self.id == other.id