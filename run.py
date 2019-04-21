from api import create_app


app = create_app('Production')
# Entry point into the api
if __name__=='__main__':
    app.run()