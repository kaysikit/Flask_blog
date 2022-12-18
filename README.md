# Start service
The service uses the poetry virtual environment. Therefore, if you do not have it installed, you need 
[to install](https://python-poetry.org/docs/)

1. Open bash and clone repository from github
```bash
$ git clone https://github.com/kaysikit/Flask_blog.git
```
2. Install Dependencies
```bash
poetry install
```
3. Copy example.env -> .env and replace value constants
4. Execute migration
```bash
pem migrate
```
5. Start app
```bash
poetry run python app.py
```