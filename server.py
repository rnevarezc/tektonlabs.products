import os
from src.main import app

if __name__ == "__main__":
    import uvicorn
    server_port = int(os.environ.get('PORT', 8000))
    uvicorn.run(app, host="0.0.0.0", port=server_port)