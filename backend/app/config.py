from os import environ as env

class Config:
    
    PORT = int(env.get('PORT', 5000))