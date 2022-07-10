from src.services.service import findresult
from flask import request, jsonify, make_response, request
from flask_restful import Resource, Api, abort, reqparse

parser = reqparse.RequestParser()
parser.add_argument('symbol', action='append')
parser.add_argument('date', action='append')
parser.add_argument('strikeType', action='append')
parser.add_argument('strikePrice', action='append')


class Nse(Resource):
    def post(self):
        response = {}
        data = {}
        args = parser.parse_args()
        result = findresult(args.symbol[0], args.date[0], args.strikeType[0], args.strikePrice[0])

        if result :
            response['message'] = "success"
            data['result'] = result
            response['data']= data
            return response, 200
        else :
            response['message'] = "Invalid inputs"
            return response, 400


    
    