```python
   from flask import Flask

app = Flask(___name___)


@app.route("/")
def hello()
    return "Hellow Woeld!"


if ___name___ == "___main___":
    app.run(host="0.0.0.0")
```