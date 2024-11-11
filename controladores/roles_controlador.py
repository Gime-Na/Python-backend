from flask import  jsonify,request  #,Flask# del modulo flask importar la clase Flask y los métodos jsonify,request
from app import app, db,ma
from modelos.roles_modelo import *

class RolSchema(ma.Schema):
    class Meta:
        fields=('id','nombre')

rol_schema=RolSchema()            # El objeto tipoproducto_schema es para traer un tipoproducto
roles_schema=RolSchema(many=True)  # El objeto tipoproductos_schema es para traer multiples registros de tipoproducto

# crea los endpoint o rutas (json)
@app.route('/roles',methods=['GET'])
def get_Roles():
    all_roles=Rol.query.all() 
    # el metodo query.all() lo hereda de db.Model
    result=roles_schema.dump(all_roles)  # el metodo dump() lo hereda de ma.schema y
                                               # trae todos los registros de la tabla
    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla

@app.route('/roles/<id>',methods=['GET'])
def get_rol(id):
    rol=Rol.query.get(id)
    return rol_schema.jsonify(rol)   # retorna el JSON de un tipoproducto recibido como parametro

@app.route('/roles/<id>',methods=['DELETE'])
def delete_rol(id):
    rol=Rol.query.get(id)
    db.session.delete(rol)#nombre
    db.session.commit()
    return rol_schema.jsonify(rol)   # me devuelve un json con el registro eliminado

@app.route('/roles', methods=['POST']) # crea ruta o endpoint
def create_rol():
    nombre=request.json['nombre']    
    new_rol=Rol(nombre)
    db.session.add(new_rol)
    db.session.commit()
    return rol_schema.jsonify(new_rol)

'''@app.route('/usuarios', methods=['POST']) # crea ruta o endpoint
def create_usuario():
    #print(request.json)  # request.json contiene el json que envio el cliente
    email=request.json['email']
    password=request.json['password']
    rol=request.json['rol']
    new_usuario=Usuario(email,password,rol)
    db.session.add(new_usuario)
    db.session.commit()
    return usuario_schema.jsonify(new_usuario)'''





@app.route('/roles/<id>' ,methods=['PUT'])
def update_rol(id):
    rol=Rol.query.get(id)
    rol.nombre=request.json['nombre']
    
    db.session.commit()
    return rol_schema.jsonify(rol)


  