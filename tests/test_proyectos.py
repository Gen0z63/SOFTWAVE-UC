import json

def test_proyectos_json():
    with open('_data/proyectos.json', 'r', encoding='utf-8') as f:
        proyectos = json.load(f)
    assert isinstance(proyectos, list)
    for proyecto in proyectos:
        assert 'nombre' in proyecto
        assert 'descripcion' in proyecto
        assert 'tecnologias' in proyecto
        assert 'enlace' in proyecto
