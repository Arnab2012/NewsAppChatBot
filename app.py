import flask
from flask import Flask, request, jsonify
import requests
import random
import streamlit as st
app = Flask(__name__)

st.header("App is working..")
@app.route('/',method=['POST'])
def home():
    data=request.get_json()
    # return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
