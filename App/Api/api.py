import json, os, re, requests
from flask import Flask, current_app, request, jsonify, Blueprint, render_template
from flask_restful import Resource , Api 
from App.Api import apiBp
from random import randint
from .Process import Process

process = Process()
api = Api(apiBp)

class Init(Resource):
    def get(self):
        data = process.create_init()
        return jsonify({
            'sender':data['sender']
        })
api.add_resource(Init,'/apis/init')