## BAB X JSON Web Token (JWT)

### Untuk menjalankan project
1. Clone Repository ini atau download manual dengan format zip.
2. Extract folder BAB X, kemudian buka vscode pada direktori folder tersebut.
3. Buka terminal vscode.
4. Inisiasi *Virtual Environtment*, dengan perintah:
    ```shell
    virtualenv env
    # atau jika perintah diatas tidak berhasil
    py -m venv env 
    # atau
    python -m venv env
    # atau
    python3 -m venv env
    ```
5. Jika pada direktori projek terdapat folder env, maka python *Virtual Environtment* berhasil di inisiasi.
6. Mengaktifkan *Virtual Environtment*, pada terminal ketikkan perintah:
    ```shell
    env\scripts\activate
    # Jika tidak berhasil, coba gantikan terminal dari powershell menjadi command prompt.
    ```
7. Install Library `flask`, `python-dotenv`, `flask-sqlalchemy`, `flask-migrate`, `pymysql` dan `flask-jwt-extended`  dengan perintah pada terminal:
    ```shell
    pip install flask python-dotenv flask-sqlalchemy flask-migrate pymysql flask-jwt-extended
    # atau jika gagal
    pip3 install flask python-dotenv flask-sqlalchemy flask-migrate pymysql flask-jwt-extended
    ```

8. Apply Migrasi database.
    - Pastikan telah membuat database dengan nama sesuai pada variabel `DB_DATABASE` di file environment `.flaskenv`
    - Apply Migrations untuk membuat tabel users dan todos dengan ketikkan perintah `flask db upgrade` pada terminal.

9. Jalankan server dengan mengetikkan perintah `flask run --debug` pada terminal.



###### Bacalah
- Rute yang terproteksi adalah rute mengambil data todos berdasarkan id user (`/todos?user_id=<user_id>`) dengan nama fungsi index() pada file UserController.py
- Silahkan Proteksi rute lainnya dengan menambah decorator @jwt_required diatas definisi/nama fungsi.