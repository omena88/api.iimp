# API de Recepción de Datos IIMP

Este es un servicio FastAPI que proporciona un endpoint para recibir datos de usuarios.

## Requisitos

- Python 3.8+
- Dependencias listadas en `requirements.txt`

## Instalación (Local)

1.  Clonar el repositorio
2.  Crear un entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```
3.  Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso (Local)

1.  Iniciar el servidor:
    ```bash
    uvicorn main:app --reload
    ```

2.  El servidor estará disponible en `http://localhost:8000`

## Endpoints

### 1. Recibir Datos

-   **URL**: `/datos/`
-   **Método**: `POST`
-   **Body**:
    ```json
    {
        "whatsapp phone": "123456789",
        "source": "web",
        "nombre completo": "Juan Perez",
        "dni": "12345678"
    }
    ```
-   **Salida**: Mensaje de confirmación.
    ```json
    {
        "status": "success",
        "message": "Datos recibidos de Juan Perez con DNI: 12345678"
    }
    ```

### 2. Health Check

-   **URL**: `/`
-   **Método**: `GET`
-   **Salida**:
    ```json
    {
        "status": "ok",
        "message": "API funcionando correctamente."
    }
    ```

## Documentación de la API

La documentación interactiva de la API (Swagger UI) generada por FastAPI está disponible en `/docs`

La documentación alternativa (ReDoc) está en `/redoc` 