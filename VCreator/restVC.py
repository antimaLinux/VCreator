#!/usr/bin/env python
# -*- coding: utf-8 -*-


#from gevent import monkey; monkey.patch_all()
from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import json
from VCreator import *
import subprocess
import os


#####################################################################################
############################## CONFIGURATION ########################################
#####################################################################################

DEBUG = True
SECRET_KEY = 'development-key'


#####################################################################################
################################# INIT ##############################################
#####################################################################################

app = Flask(__name__)
app.config.from_object(__name__)
api=Api(app)

#####################################################################################
############################### CLASSES #############################################
#####################################################################################


class Creator(Resource):
    def get(self):
        base_string='python VCreator.py -j'
        arg_string=base_string
        parser=reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('gender')
        parser.add_argument('region')
        parser.add_argument('clan')
        parser.add_argument('darkFlag')
        args=parser.parse_args()
        if (args['name'] is not None):
            arg_string+=' --name={0}'.format(args['name'].title())
        if (args['gender'] is not None):
            arg_string+=' --gender={0}'.format(args['gender'])
        if (args['region'] is not None):
            #Controllo regione no cina, giappone, romania, grecia
            arg_string+=' --region={0}'.format(args['region'].title())
        if (args['clan'] is not None):
            arg_string+=' --clan={0}'.format(args['clan'].title())
        if (args['darkFlag'] is not None):
            if (args['darkFlag'].title() == 'True'):
                arg_string+=' --dark'
            else:
                pass
        proc=subprocess.Popen([arg_string, ''], stdout=subprocess.PIPE, shell=True)
        (data, err)=proc.communicate()
        print(err)
        data_loaded=json.loads(data, encoding='utf-8')
        #print(getStringWithDecodedUnicode(jsonify(data_loaded).data))
        if (err):
            return "An error occured"
        else:
            return jsonify(data_loaded)

#####################################################################################
################################# ROUTES ############################################
#####################################################################################

api.add_resource(Creator, '/')

#####################################################################################
################################## MAIN #############################################
#####################################################################################

if __name__ == '__main__':
    app.run()
    # from gevent.wsgi import WSGIServer
    # WSGIServer(('', 5000), app).serve_forever()
