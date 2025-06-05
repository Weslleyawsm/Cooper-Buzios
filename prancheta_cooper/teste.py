from database import DatabaseManager

db = DatabaseManager()
db.debug_completo()

# Teste também a função listar_todos_registros
print("\n🔍 Testando listar_todos_registros:")
todos = db.listar_todos_registros()
print(f"Resultado: {todos}")