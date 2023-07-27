# Keywords

keywords: DDD, SOLID, Hexagonal architecture  

- DDD, define the service boundaries   
- Hexagonal architecture, implement interfaces of the domain   
  - Hexagonal architecture is a subset of SOLID principles, especially D of “Dependency inversion” and L of “Liskov substitution”.    


Tonces segun, teniendo una entidad y un repository definido ya tenemos el primer hexagono.
Donde va la logica? 
    En la entidad.


Hasta este punto el proyecto es una implementación basica de hexagonal architecture, tomada de https://douwevandermeij.medium.com/hexagonal-architecture-in-python-7468c2606b63

Pero la estructura del proyecto puede evolucionar a algo asi, tomado de https://github.com/serfer2/flask-hexagonal-architecture-api.
Los en domain/ se pueden separar las entidades(o modelos) de los repositories, en diferentes carpetas.
En controller podriamos agregar otra capa me imagino yo, de pronto un CLI en vez de una API.

```
.
├── application
│   ├── exceptions.py
│   ├── __init__.py
│   └── services
│       ├── acquire_pdf_file.py
│       ├── anonymize_txt_file.py
│       └── __init__.py
├── controller
│   ├── app.py ---------------> API entry point
│   ├── exceptions.py
│   ├── __init__.py
│   └── utils.py
├── Dockerfile
├── domain
│   ├── __init__.py
│   ├── models
│   │   ├── __init__.py
│   │   └── report.py
│   └── repositories
│       ├── __init__.py
│       └── report_repository_interface.py
├── infrastructure
│   ├── database.py
│   ├── __init__.py
│   └── repositories
│       ├── base_repository.py
│       ├── __init__.py
│       └── report_repository.py
├── lint.sh
├── requirements.txt
└── test
    ├── application
    │   ├── __init__.py
    │   └── test_services.py
    ├── base_test_case.py
    ├── controller
    │   ├── __init__.py
    │   └── test_app.py
    ├── infrastructure
    │   ├── __init__.py
    │   └── test_repositories.py
    └── __init__.py
```