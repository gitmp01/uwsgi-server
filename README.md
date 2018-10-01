Minimal working example using uwsgi.

Use virtualenv

```bash
pip install -r requirements.txt
```

Run with

```bash
uwsgi --ini conf.ini
```

Check with 

```python
import requests

request.post("http://localhost:8081", data="{'ciao':1}")
request.get("http://localhost:8081?ciao=1")
```

