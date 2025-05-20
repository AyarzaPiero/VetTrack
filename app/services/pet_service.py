from ..models.pet_model import Pet
from ..db import db

def create_pet(pet_data):
    """
    Crea un nuevo registro de mascota con los datos proporcionados
    
    Args:
        pet_data (dict): Diccionario con los datos de la mascota
        
    Returns:
        Pet: Objeto de la mascota creada
    """
    pet = Pet(
        name=pet_data.get('name'),
        owner=pet_data.get('owner'),
        species=pet_data.get('species'),
        breed=pet_data.get('breed'),
        age=pet_data.get('age'),
        gender=pet_data.get('gender'),
        color=pet_data.get('color'),
        notes=pet_data.get('notes'),
        vaccinated=True if pet_data.get('vaccinated') else False
    )
    
    db.session.add(pet)
    db.session.commit()
    return pet

def get_all_pets():
    """
    Obtiene todas las mascotas registradas
    
    Returns:
        list: Lista de objetos Pet
    """
    return Pet.query.order_by(Pet.created_at.desc()).all()

def get_pet_by_id(pet_id):
    """
    Obtiene una mascota por su ID
    
    Args:
        pet_id (int): ID de la mascota
        
    Returns:
        Pet: Objeto de la mascota o None si no existe
    """
    return Pet.query.get(pet_id)

def update_pet(pet_id, pet_data):
    """
    Actualiza los datos de una mascota existente
    
    Args:
        pet_id (int): ID de la mascota a actualizar
        pet_data (dict): Diccionario con los nuevos datos
        
    Returns:
        Pet: Objeto de la mascota actualizada o None si no existe
    """
    pet = Pet.query.get(pet_id)
    
    if pet:
        pet.name = pet_data.get('name', pet.name)
        pet.owner = pet_data.get('owner', pet.owner)
        pet.species = pet_data.get('species', pet.species)
        pet.breed = pet_data.get('breed', pet.breed)
        pet.age = pet_data.get('age', pet.age)
        pet.gender = pet_data.get('gender', pet.gender)
        pet.color = pet_data.get('color', pet.color)
        pet.notes = pet_data.get('notes', pet.notes)
        pet.vaccinated = True if pet_data.get('vaccinated') else False
        
        db.session.commit()
    
    return pet

def delete_pet(pet_id):
    """
    Elimina una mascota por su ID
    
    Args:
        pet_id (int): ID de la mascota a eliminar
        
    Returns:
        bool: True si se eliminó correctamente, False si no
    """
    pet = Pet.query.get(pet_id)
    
    if pet:
        db.session.delete(pet)
        db.session.commit()
        return True
    
    return False