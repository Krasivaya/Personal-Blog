from app import create_app,db
from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand
from app.models import User,Article


app = create_app('production')

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('db',MigrateCommand)
manager.add_command('server',Server)

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner(verbosity=5).run(tests)

@manager.shell
def make_shell_context():
    return {'db' : db,'User':User , 'Article':Article}


if __name__ == "__main__":
    manager.run()