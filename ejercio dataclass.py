# Objetivo: integrar varios conceptos: dataclass con field(), __post_init__, valores por defecto, y usar una clase contenedora normal que gestione una lista de dataclasses.

# Enunciado
# Parte A — Dataclass Tarea
# Crea una dataclass Tarea con los siguientes campos:

# id: int
# titulo: str
# descripcion: str
# completada: bool — valor por defecto False
# Validaciones en __post_init__:

# titulo no puede estar vacío
# id debe ser mayor a 0
# Método adicional:

# marcar_completada(self) -> None — cambia completada a True.
# Parte B — Clase GestorTareas
# Crea una clase normal (no dataclass) llamada GestorTareas con:

# Atributo: tareas: list[Tarea] (inicia como lista vacía)

# Métodos:

# agregar(tarea: Tarea) -> None — agrega una tarea. Si ya existe una tarea con el mismo id, lanza ValueError.
# eliminar(id_tarea: int) -> None — elimina la tarea con ese id. Si no existe, lanza ValueError.
# pendientes() -> list[Tarea] — retorna una lista con las tareas donde completada == False.
# completadas() -> list[Tarea] — retorna una lista con las tareas donde completada == True.
# buscar(id_tarea: int) -> Tarea — retorna la tarea con ese id. Si no existe, lanza ValueError.
# Dunder: __repr__ que muestre algo como "GestorTareas(3 tareas)".

from dataclasses import dataclass
@dataclass
class Tarea:
    id: int
    titulo: str
    descripcion: str
    completada: bool = False

    def __post_init__(self):
        if not self.titulo.strip():
            return "titulo vacio, no valido"
        if not self.edad >0:
            return "el id debe ser mayor que 0"
    def marcar_completada(self) -> None:
        self.completada = True
    
class  GestorTareas:
    def __init__(self) -> None:
        self.tareas: list[Tarea] = []

    def agregar(self,tarea: Tarea) -> None:
        if tarea.id not in self.tareas:
            self.tareas.append(tarea)
        return "id duplicado"
    
    def eliminar(self,id_tarea: int) -> None:
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                self.tareas.remove(tarea.id)
    
    def pendientes(self) -> list[Tarea]:
       
        return  [tarea for tarea in self.tareas if not tarea.completada]
    
    def completadas(self) -> list[Tarea]:
        return [tarea for tarea in self.tareas if tarea.completada]
    
    def buscar(self,id_tarea: int) -> Tarea:
        for tarea in self.tareas:
            if tarea.id == id_tarea:
             return tarea
    
    def __repr__(self) -> str:
        return f"GestorTareas{len(self.tareas) +'tareas'}"
            
    


