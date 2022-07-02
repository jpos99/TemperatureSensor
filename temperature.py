from app import app
import os

port = int(os.environ.get("PORT", 15000))

if __name__ == "__main__":
	# app.run(port=port)
	app.run(port=port)
