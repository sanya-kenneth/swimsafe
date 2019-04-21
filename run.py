from api import create_app


app = create_app('Development')
# Entry point into the api
if __name__=='__main__':
    app.run()