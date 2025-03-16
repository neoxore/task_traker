<img src="https://www.animatedimages.org/data/media/562/animated-line-image-0184.gif" width="1920" height=0.4/>
# 🚀 TaskFlow – Asynchronous Task Tracker

TaskFlow is a powerful task tracker designed for efficient task management. The project is built on modern technologies, ensuring high performance and flexibility.

## 🔥 Key Features
- ✅ **Asynchronous** – High-speed request processing with FastAPI and asyncio
- ✅ **FastAPI** – Modern and fast web framework for building APIs
- ✅ **PostgreSQL** – Reliable data storage with transaction support
- ✅ **Migrations** – Convenient database change management with Alembic
- ✅ **Clean Architecture** – Well-structured code for easy maintenance and scaling

## 🚀 Installation and Setup

1. **Clone the repository**
```bash
git clone https://github.com/neoxore/task_traker
cd task_tracker
```

2. **Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate    # For Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables** (create a `.env` file and specify database settings)
```
DATABASE_URL=postgresql+asyncpg://user:password@localhost/taskflow_db
```

5. **Apply migrations**
```bash
alembic upgrade head
```

6. **Run the server**
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

7. **Open API Documentation**
Once the server is running, access the documentation at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 📌 TODO
- [ ] Add authentication
- [ ] Implement user roles
- [ ] Add WebSockets support

💡 Development is ongoing – join the project and contribute! 🚀
<img src="https://www.animatedimages.org/data/media/562/animated-line-image-0184.gif" width="1920" height=0.4/>
