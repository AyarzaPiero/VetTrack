from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..services.pet_service import create_pet, get_all_pets, get_pet_by_id, update_pet, delete_pet

pet_bp = Blueprint("pet_bp", __name__)

@pet_bp.route("/")
def index():
    """Ruta principal que muestra todas las mascotas"""
    pets = get_all_pets()
    return render_template("index.html", pets=pets)

@pet_bp.route("/register", methods=["GET", "POST"])
def register():
    """Ruta para registrar una nueva mascota"""
    if request.method == "POST":
        pet_data = {
            'name': request.form.get('name'),
            'owner': request.form.get('owner'),
            'species': request.form.get('species'),
            'breed': request.form.get('breed'),
            'age': request.form.get('age') if request.form.get('age') else None,
            'gender': request.form.get('gender'),
            'color': request.form.get('color'),
            'notes': request.form.get('notes'),
            'vaccinated': request.form.get('vaccinated')
        }
        
        try:
            pet = create_pet(pet_data)
            flash(f"Mascota '{pet.name}' registrada exitosamente", "success")
            return redirect(url_for("pet_bp.index"))
        except Exception as e:
            flash(f"Error al registrar la mascota: {str(e)}", "danger")
    
    return render_template("register.html")

@pet_bp.route("/pet/<int:pet_id>")
def pet_details(pet_id):
    """Ruta para ver los detalles de una mascota"""
    pet = get_pet_by_id(pet_id)
    
    if not pet:
        flash("Mascota no encontrada", "warning")
        return redirect(url_for("pet_bp.index"))
    
    return render_template("pet_details.html", pet=pet)

@pet_bp.route("/pet/<int:pet_id>/edit", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Ruta para editar una mascota existente"""
    pet = get_pet_by_id(pet_id)
    
    if not pet:
        flash("Mascota no encontrada", "warning")
        return redirect(url_for("pet_bp.index"))
    
    if request.method == "POST":
        pet_data = {
            'name': request.form.get('name'),
            'owner': request.form.get('owner'),
            'species': request.form.get('species'),
            'breed': request.form.get('breed'),
            'age': request.form.get('age') if request.form.get('age') else None,
            'gender': request.form.get('gender'),
            'color': request.form.get('color'),
            'notes': request.form.get('notes'),
            'vaccinated': request.form.get('vaccinated')
        }
        
        try:
            update_pet(pet_id, pet_data)
            flash(f"Mascota '{pet.name}' actualizada exitosamente", "success")
            return redirect(url_for("pet_bp.pet_details", pet_id=pet_id))
        except Exception as e:
            flash(f"Error al actualizar la mascota: {str(e)}", "danger")
    
    return render_template("edit_pet.html", pet=pet)

@pet_bp.route("/pet/<int:pet_id>/delete", methods=["POST"])
def delete_pet_route(pet_id):
    """Ruta para eliminar una mascota"""
    pet = get_pet_by_id(pet_id)
    
    if not pet:
        flash("Mascota no encontrada", "warning")
        return redirect(url_for("pet_bp.index"))
    
    pet_name = pet.name
    
    if delete_pet(pet_id):
        flash(f"Mascota '{pet_name}' eliminada exitosamente", "success")
    else:
        flash("Error al eliminar la mascota", "danger")
    
    return redirect(url_for("pet_bp.index"))