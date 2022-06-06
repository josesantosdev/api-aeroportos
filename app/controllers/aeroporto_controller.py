from flask import Blueprint, request, jsonify, make_response
from marshmallow import EXCLUDE
from app import db
from app.models.aeroporto import Aeroporto, AeroportoSchema

class AeroportoController:
    aeroporto_controller = Blueprint(name='aeroporto_controller', import_name=__name__)

    @aeroporto_controller.route('/aeroportos', methods=['GET'])
    def get_aeroportos():
        aeroporto_list = Aeroporto.query.all()
        aeroporto_schema = AeroportoSchema(many=True)
        aeroporto_json = aeroporto_schema.dump(aeroporto_list)
        return make_response(jsonify({"Aeroportos":aeroporto_json}), 200)

    @aeroporto_controller.route('/aeroportos/<String: iata>', methods=['GET'])
    def get_aeroporto(iata):
        aeroporto = Aeroporto.query.filter_by(codigo_iata=iata).first()
        if aeroporto:
            aeroporto_schema = AeroportoSchema()
            aeroporto_json = aeroporto_schema.dump(aeroporto)
            return make_response(jsonify({"Aeroporto":aeroporto_json}), 200)
        else:
            return make_response(jsonify({"Aeroporto":None}), 404)

    @aeroporto_controller.route('/aeroportos', methods=['POST'])
    def post_aeroporto():
        data = request.get_json()
        aeroporto_schema = AeroportoSchema(unknown=EXCLUDE)
        aeroporto = aeroporto_schema.load(data)
        result = aeroporto_schema.dump(aeroporto.create())
        return make_response(jsonify({"Aeroporto":result}), 201)

    @aeroporto_controller.route('/aeroportos/<String: iata>', methods=['PUT'])
    def put_aeroporto(iata):
        pass

    @aeroporto_controller.route('/aeroportos/<String: iata>', methods=['DELETE'])
    def delete_aeroporto(iata):
        pass
