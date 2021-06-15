from app.app import create_app

if __name__ == '__main__':
	env_name = "development"
	app = create_app(env_name)
	app.debug=True
	#run app
	app.run()