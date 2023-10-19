## BAB II Python Virtual Enviroment dan Flask
### Untuk menjalankan projek
1. Clone project ini atau download manual.
2. Buka terminal/command prompt pada direktori projek ini.
3. Inisiasi virtual environment python dengan perintah: 
    ```shell
    virtual env
    # Atau jika perintah diatas tidak berhasil
    py -m venv env
    ```
4. Aktifkan virtual enviroment dengan perintah:
    ```shell
    env\scripts\activate
    ```
5. Install library `flask` dengan perintah:
    ```shell
    pip install flask
    # Atau jika perintah diatas tidak berhasil
    pip3 install flask
    ```
6. Jalankan file `app.py` pada vscode atau dapat melalui command prompt dengan perintah:
    ```shell
    flask run
    # Atau Jika perintah diatas tidak berhasil
    py app.py 
    ```