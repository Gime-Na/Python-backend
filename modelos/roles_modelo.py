from app import app, db   #,ma

# defino las tabla ROL
class Rol(db.Model):   # la clase Roles hereda de db.Model    
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    nombre=db.Column(db.String(100))
    
   
    def __init__(self,nombre):   #crea el  constructor de la clase
        self.id=id  # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.nombre=nombre
        
        

with app.app_context():
    db.create_all()  # aqui crea todas las tablas
#  ************************************************************
