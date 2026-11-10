from fastapi import FastAPI


app = FastAPI()

@app.get("/")  # decoratore function 
def hello():
  return {'message':'Hello world'}

#command : uvicorn main:app --reload 

@app.get('/about') #route for the second one
def about():
  return {'message':'this is an education platform to study'}

# to get the documentation of the request just type {/docs}

