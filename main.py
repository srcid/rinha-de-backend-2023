import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "rinha_de_backend_2023.main:app", host="0.0.0.0", port=9999, reload=True
    )
