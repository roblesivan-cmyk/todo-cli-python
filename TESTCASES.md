# Test Cases – ToDo CLI App (Consola)

**Sistema:** ToDo CLI App (Python)  
**Alcance:** Agregar, Mostrar, Editar, Eliminar, Completar, Buscar, Filtrar  
**Notas:** Se valida persistencia en `tareas.json` cuando aplique.

---

## Módulo: Agregar tarea

| TC-ID | Título | Precondiciones | Datos de prueba | Pasos | Resultado esperado | Tipo |
|------|--------|----------------|-----------------|------|-------------------|------|
| TC-001 | Agregar tarea válida (pendiente) | App abierta | ID=1, Desc="Estudiar Python", Estado="pendiente" | 1) Elegir opción Agregar 2) Capturar datos | Se agrega la tarea y aparece en Mostrar; se guarda en JSON | Funcional |
| TC-002 | Agregar tarea válida (completada) | App abierta | ID=2, Desc="Hacer ejercicio", Estado="completada" | 1) Agregar 2) Capturar datos | Se agrega correctamente y se guarda en JSON | Funcional |
| TC-003 | ID duplicado | Existe tarea con ID=1 | ID=1, Desc="Otra", Estado="pendiente" | 1) Agregar 2) Capturar datos | Muestra mensaje de ID duplicado; no agrega; JSON no cambia | Negativo |
| TC-004 | ID no numérico | App abierta | ID="abc" | 1) Agregar 2) Capturar ID inválido | Muestra mensaje de error; no agrega | Negativo |
| TC-005 | Descripción vacía | App abierta | Desc="" (Enter) | 1) Agregar 2) Dejar descripción vacía | Muestra validación “no puede ir vacía”; no agrega | Validación |
| TC-006 | Estado inválido | App abierta | Estado="terminada" | 1) Agregar 2) Capturar estado inválido | Muestra validación; no agrega | Negativo |

---

## Módulo: Mostrar tareas

| TC-ID | Título | Precondiciones | Datos | Pasos | Resultado esperado | Tipo |
|------|--------|----------------|------|------|-------------------|------|
| TC-007 | Mostrar con tareas existentes | Hay 1+ tareas | - | 1) Elegir Mostrar | Lista tareas con formato ID/desc/estado | Funcional |
| TC-008 | Mostrar sin tareas | Lista vacía | - | 1) Elegir Mostrar | Muestra “No hay tareas para mostrar” | Funcional |

---

## Módulo: Editar tarea

| TC-ID | Título | Precondiciones | Datos | Pasos | Resultado esperado | Tipo |
|------|--------|----------------|------|------|-------------------|------|
| TC-009 | Editar desc y estado | Existe ID=1 | Desc nueva + Estado="completada" | 1) Editar 2) ID=1 3) Capturar cambios | Actualiza ambos campos y guarda en JSON | Funcional |
| TC-010 | Editar solo descripción | Existe ID=1 | Desc nueva, Estado="" (Enter) | 1) Editar 2) ID=1 3) Cambiar desc | Solo cambia descripción; estado se conserva | Funcional |
| TC-011 | Editar solo estado | Existe ID=1 | Desc="" (Enter), Estado="pendiente" | 1) Editar 2) ID=1 3) Cambiar estado | Solo cambia estado; descripción se conserva | Funcional |
| TC-012 | Editar con ID inexistente | No existe ID=99 | ID=99 | 1) Editar 2) Capturar ID inexistente | Mensaje “No se encontró…”; no cambia JSON | Negativo |
| TC-013 | Editar con estado inválido | Existe ID=1 | Estado="x" | 1) Editar 2) ID=1 3) Estado inválido | Muestra validación; no aplica cambios | Negativo |

---

## Módulo: Eliminar tarea

| TC-ID | Título | Precondiciones | Datos | Pasos | Resultado esperado | Tipo |
|------|--------|----------------|------|------|-------------------|------|
| TC-014 | Eliminar tarea existente | Existe ID=1 | ID=1 | 1) Eliminar 2) Capturar ID | Se elimina de lista y se guarda en JSON | Funcional |
| TC-015 | Eliminar ID inexistente | No existe ID=99 | ID=99 | 1) Eliminar 2) Capturar ID | Mensaje “No se encontró…”; no cambia JSON | Negativo |
| TC-016 | Eliminar ID no numérico | App abierta | ID="a" | 1) Eliminar 2) Capturar ID inválido | Mensaje de error; no cambia nada | Validación |

---

## Módulo: Completar tarea

| TC-ID | Título | Precondiciones | Datos | Pasos | Resultado esperado | Tipo |
|------|--------|----------------|------|------|-------------------|------|
| TC-017 | Completar tarea pendiente | Existe ID=2 en pendiente | ID=2 | 1) Completar 2) Capturar ID | Cambia a completada y guarda en JSON | Funcional |
| TC-018 | Completar tarea ya completada | Existe ID=2 completada | ID=2 | 1) Completar 2) Capturar ID | Mensaje “ya está completada”; no cambia | Funcional |
| TC-019 | Completar con ID inexistente | No existe ID=99 | ID=99 | 1) Completar 2) Capturar ID | Mensaje “No se encontró…” | Negativo |

---

## Módulo: Buscar / Filtrar

| TC-ID | Título | Precondiciones | Datos | Pasos | Resultado esperado | Tipo |
|------|--------|----------------|------|------|-------------------|------|
| TC-020 | Buscar por palabra (case-insensitive) | Existe tarea “Estudiar Python” | Buscar="python" | 1) Buscar 2) Capturar texto | Encuentra la tarea aunque cambie mayúsculas | Funcional |
| TC-021 | Buscar sin resultados | Hay tareas | Buscar="zzz" | 1) Buscar 2) Capturar texto | Mensaje “No se encontraron…” | Funcional |
| TC-022 | Buscar vacío | App abierta | Buscar="" | 1) Buscar 2) Enter | Mensaje “Búsqueda vacía” | Validación |
| TC-023 | Filtrar por pendiente | Hay pendientes y completadas | Estado="pendiente" | 1) Filtrar 2) Capturar estado | Solo muestra pendientes | Funcional |
| TC-024 | Filtrar por completada | Hay pendientes y completadas | Estado="completada" | 1) Filtrar 2) Capturar estado | Solo muestra completadas | Funcional |
| TC-025 | Filtrar con estado inválido | App abierta | Estado="done" | 1) Filtrar 2) Capturar estado inválido | Mensaje de validación | Negativo |
