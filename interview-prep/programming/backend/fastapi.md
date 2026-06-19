# FastAPI Questions

## What is FastAPI and what makes it different from other Python web frameworks?

**FastAPI** is a modern, high-performance Python web framework for building APIs. It is built on top of **Starlette** (for the web layer) and **Pydantic** (for data validation), and it is fully async-capable.

Key differentiators from Flask or Django:

| Feature | FastAPI | Flask | Django |
|:---|:---|:---|:---|
| **Performance** | Very high (async, Starlette-based) | Moderate (sync by default) | Moderate |
| **Type hints** | First-class, drives validation | Optional | Optional |
| **Auto docs** | Built-in (Swagger + ReDoc) | Third-party | Third-party |
| **Data validation** | Pydantic (automatic) | Manual | Forms/DRF |
| **Async support** | Native | Limited (extensions) | Partial (3.1+) |

FastAPI's defining feature is that it uses Python type hints to automatically handle request validation, serialization, and documentation generation — you write the types once and get all three for free.

---

## How does request validation work in FastAPI?

FastAPI uses **Pydantic models** to validate incoming data. When a request comes in, FastAPI automatically parses the body, validates it against the model's field types and constraints, and returns a `422 Unprocessable Entity` response with a detailed error if validation fails.

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

class UserCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    age: int = Field(ge=18, le=120)  # ge = greater or equal, le = less or equal

@app.post("/users")
async def create_user(user: UserCreate):
    # 'user' is already validated — if we reach here, all fields are correct
    return {"message": f"Created user {user.name}"}
```

If you POST `{"name": "", "email": "not-an-email", "age": 15}`, FastAPI automatically returns:
```json
{
  "detail": [
    {"loc": ["body", "name"], "msg": "String should have at least 1 character"},
    {"loc": ["body", "email"], "msg": "value is not a valid email address"},
    {"loc": ["body", "age"], "msg": "Input should be greater than or equal to 18"}
  ]
}
```

---

## What are path parameters, query parameters, and request bodies?

FastAPI infers where a parameter comes from based on its declaration:

- **Path parameter** — part of the URL path, declared in the route string with `{}`.
- **Query parameter** — after the `?` in the URL, declared as a plain function argument.
- **Request body** — the JSON body, declared as a Pydantic model argument.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ItemUpdate(BaseModel):
    name: str
    price: float

@app.put("/items/{item_id}")
async def update_item(
    item_id: int,           # path parameter — from /items/42
    published: bool = True, # query parameter — from ?published=true
    body: ItemUpdate = None, # request body — from JSON payload
):
    return {"item_id": item_id, "published": published, "body": body}
```

A request to `PUT /items/42?published=false` with body `{"name": "Widget", "price": 9.99}` maps each value automatically.

---

## What is dependency injection in FastAPI?

FastAPI has a built-in **dependency injection system** using the `Depends()` function. A dependency is any callable (function or class) whose result FastAPI will compute and inject into your route handler. Dependencies can themselves have dependencies, forming a tree.

Common uses: authentication, database sessions, shared configuration, rate limiting.

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    if token != "valid-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )
    return {"user": "alice"}

@app.get("/me")
async def read_profile(current_user: dict = Depends(get_current_user)):
    return current_user
```

Dependencies run before the route handler and their result is passed in. They also handle cleanup — a dependency that uses `yield` will run its teardown code after the response is sent:

```python
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db        # injected into the route
    finally:
        db.close()      # guaranteed cleanup after response

@app.get("/users/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.id == user_id).first()
```

---

## How does FastAPI handle async code?

FastAPI is built on **Starlette**, which uses an ASGI server (like **Uvicorn** or **Hypercorn**) and Python's `asyncio`. Route handlers can be either `async def` or plain `def`:

- **`async def`** — runs on the event loop directly. Use this when your handler does async I/O (awaiting database queries, HTTP calls, etc.).
- **`def`** — FastAPI runs it in a thread pool executor so it doesn't block the event loop.

```python
import asyncio
import httpx

@app.get("/async-example")
async def async_route():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.example.com/data")
    return response.json()

@app.get("/sync-example")
def sync_route():
    # This runs in a threadpool — OK for blocking calls
    import time
    time.sleep(1)
    return {"done": True}
```

The key rule: **never call blocking I/O inside an `async def` route without `await`** — it will block the entire event loop and eliminate the concurrency benefit.

---

## What are FastAPI routers and how do you structure a large application?

**`APIRouter`** lets you split route definitions across multiple files and group them under a shared prefix or set of dependencies, similar to Flask Blueprints.

```
app/
├── main.py
├── routers/
│   ├── users.py
│   └── items.py
└── dependencies.py
```

`routers/users.py`:
```python
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
async def list_users():
    return [{"id": 1, "name": "Alice"}]

@router.get("/{user_id}")
async def get_user(user_id: int):
    return {"id": user_id}
```

`main.py`:
```python
from fastapi import FastAPI
from app.routers import users, items

app = FastAPI()
app.include_router(users.router)
app.include_router(items.router)
```

The `prefix`, `tags`, and `dependencies` set on `include_router()` apply to all routes in that router, avoiding repetition.

---

## How do you handle authentication in FastAPI?

FastAPI provides built-in security utilities in `fastapi.security`. The most common patterns:

**OAuth2 with JWT tokens** — the industry standard for stateless API auth:

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

def create_access_token(data: dict) -> str:
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if not username:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        return username
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

@app.post("/token")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    # validate form.username / form.password against your DB here
    token = create_access_token({"sub": form.username})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/protected")
async def protected_route(user: str = Depends(get_current_user)):
    return {"hello": user}
```

**API Key** — simpler alternative for server-to-server communication:

```python
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(name="X-API-Key")

def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != "expected-key":
        raise HTTPException(status_code=403, detail="Invalid API key")
```

---

## What is middleware in FastAPI and how do you add it?

**Middleware** is a function that wraps every request/response cycle. It runs before the route handler processes the request and after it produces the response. Common uses: logging, CORS, request timing, adding response headers.

```python
import time
from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def add_timing_header(request: Request, call_next):
    start = time.time()
    response = await call_next(request)  # run the actual route handler
    duration = time.time() - start
    response.headers["X-Process-Time"] = str(duration)
    return response
```

**CORS middleware** is the most commonly needed, allowing browsers from other origins to call your API:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://myfrontend.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## What is the difference between `response_model` and returning a Pydantic model directly?

Both control what gets serialized in the response, but `response_model` gives you additional filtering and documentation benefits.

- **Returning a model directly** — FastAPI serializes whatever the route returns. If you return an ORM object or a dict with extra fields, those leak through.
- **`response_model`** — FastAPI filters the output to only include fields defined in the model, regardless of what the route returns. It also drives the OpenAPI documentation.

```python
class UserPublic(BaseModel):
    id: int
    name: str
    # no 'password_hash' field

class UserInternal(BaseModel):
    id: int
    name: str
    password_hash: str  # sensitive — must not be sent to clients

@app.get("/users/{user_id}", response_model=UserPublic)
async def get_user(user_id: int):
    # Even if we return a UserInternal, 'password_hash' is stripped
    return UserInternal(id=user_id, name="Alice", password_hash="secret")
```

`response_model` is the safe, explicit way to control your API's public contract.

---

## How does background task processing work in FastAPI?

FastAPI provides `BackgroundTasks` for running work after the response has been sent to the client — useful for things like sending emails or writing audit logs without making the user wait.

```python
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def send_email(email: str, message: str):
    # Runs after the response is already sent
    print(f"Sending email to {email}: {message}")

@app.post("/register")
async def register(email: str, tasks: BackgroundTasks):
    # ... create the user in the DB ...
    tasks.add_task(send_email, email, "Welcome!")
    return {"message": "Registered successfully"}
```

For heavier workloads (long-running jobs, retries, scheduling), use a dedicated task queue like **Celery** with Redis/RabbitMQ, or **ARQ** for async-native queues. `BackgroundTasks` is not a replacement — it runs in the same process and will be killed if the server restarts.

---

## How do you handle errors and custom exception handlers?

FastAPI uses `HTTPException` for expected errors. For global error handling, you can register exception handlers on the app.

```python
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Custom exception class
class ItemNotFoundError(Exception):
    def __init__(self, item_id: int):
        self.item_id = item_id

# Register a handler for it
@app.exception_handler(ItemNotFoundError)
async def item_not_found_handler(request: Request, exc: ItemNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"detail": f"Item {exc.item_id} not found"},
    )

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id > 100:
        raise ItemNotFoundError(item_id)  # triggers the handler above
    return {"id": item_id}
```

You can also override the default `RequestValidationError` handler to customize the 422 response format.

---

## How do you test a FastAPI application?

FastAPI integrates with `pytest` via **`TestClient`** (synchronous, wraps `httpx`) or `AsyncClient` for async tests.

```python
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get("/items/{item_id}")
def get_item(item_id: int, q: str | None = None):
    return {"id": item_id, "q": q}

client = TestClient(app)

def test_get_item():
    response = client.get("/items/42?q=hello")
    assert response.status_code == 200
    assert response.json() == {"id": 42, "q": "hello"}

def test_validation_error():
    response = client.get("/items/not-an-int")
    assert response.status_code == 422
```

For async routes or when you need async test utilities, use `httpx.AsyncClient` with `asgi_transport`:

```python
import pytest
import httpx

@pytest.mark.asyncio
async def test_async():
    async with httpx.AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/items/1")
    assert response.status_code == 200
```

Override dependencies in tests using `app.dependency_overrides` to swap out databases or auth:

```python
def override_get_db():
    yield test_db_session  # use an in-memory or test database

app.dependency_overrides[get_db] = override_get_db
```
