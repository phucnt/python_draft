from flask.ext.script import Server, Manager, prompt_bool
# from myapp import app
from apps import app

manager = Manager(app)
manager.add_command("runserver", Server('0.0.0.0', port=5001))
app.run(host='0.0.0.0', port=5001, debug=True)

if __name__ == "__main__":
    manager.run()