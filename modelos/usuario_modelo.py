from app import app, db   #,ma

# defino las tablas
class Usuario(db.Model):   # la clase Usuario hereda de db.Model    
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    email=db.Column(db.String(100))
    password=db.Column(db.String(10))
    rol=db.Column(db.Integer, db.ForeignKey("rol.id"), nullable=False)
   
    def __init__(self,email,password,rol):   #crea el  constructor de la clase
        self.email=email   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.passsword=password
        self.rol=rol
        

with app.app_context():
    db.create_all()  # aqui crea todas las tablas
#  ************************************************************
