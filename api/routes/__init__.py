import os
import importlib
from flask import Flask

def register_blueprints(app):
    # Caminho da pasta onde os arquivos de blueprint estão localizados
    routes_path = os.path.dirname(__file__)
    
    # Listar todos os arquivos na pasta
    for filename in os.listdir(routes_path):
        # Verificar se o arquivo termina com '_routes.py'
        if filename.endswith('_routes.py'):
            # Nome do módulo (sem a extensão .py)
            module_name = f'routes.{filename[:-3]}'
            
            # Importar o módulo dinamicamente
            module = importlib.import_module(module_name)
            
            # Verificar se o módulo tem um atributo 'bp' (blueprint)
            if hasattr(module, 'bp'):
                # Registrar o blueprint
                app.register_blueprint(module.bp)
    
    return app

# from flask import Flask
# from routes.user_routes import user_bp

# def register_blueprints(app):
#     app.register_blueprint(user_bp)
#     return app