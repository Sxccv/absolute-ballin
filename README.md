### Website: https://randuichi-touya-absoluteballin.pbp.cs.ui.ac.id/
### Repo: https://github.com/Sxccv/absolute-ballin/

# Checklist

## 1. 
```mermaid
graph TD
    A[Client (Browser)] -->|HTTP Request| B[urls.py<br>(URL Dispatcher)]
    B -->|Match URL pattern| C[views.py<br>(View Function)]
    C -->|Optional: Query DB| D[models.py<br>(Database Models)]
    D -->|Return data| C
    C -->|Pass context| E[templates/<br>HTML Files]
    E -->|Render HTML| C
    C -->|HTTP Response| F[Client (Browser)]
```