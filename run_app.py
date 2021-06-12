from App import app
from App.Api import apiBp
app.register_blueprint(apiBp)

if __name__ == '__main__':
    app.run()