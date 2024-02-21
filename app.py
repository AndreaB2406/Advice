from flask import Flask, jsonify, request
from pydantic import ValidationError
from data.prize_data import PrizeData
from model.input_validator import InputData

app = Flask(__name__)

@app.route('/api/catalogs/<id_catalog>/prizes', methods=['GET'])
def list_prizes(id_catalog):

    try:
        # Obtaining parameters from query string
        filter_id = request.args.get('filter[id]')
        filter_description = request.args.get('filter[description]')
        page = request.args.get('pagination[page]')
        per_page = request.args.get('pagination[per_page]')

        filter = {
            'id': filter_id,
            'description': filter_description
        }

        pagination = {
            'page': page,
            'per_page': per_page
        }

        # Input validation
        validated_data = InputData(**{'id_catalog': id_catalog, 'filter': filter, 'pagination': pagination})
        validated_data = validated_data.dict(exclude_none=False)

    except ValidationError as e:
        return jsonify({'Validation error': str(e)}), 400
    
    except Exception as e:
        # Handling of other unforeseen exceptions
        return jsonify({'error': 'An unexpected error occurred.'}), 500


    try:
        prizes = PrizeData.get_prizes(validated_data['id_catalog'], validated_data['filter'], validated_data['pagination'])
        
        response = {
            'total': len(prizes),
            'prizes': prizes
        }

        return jsonify(response), 200
    
    except ValueError as e:
        # Exception handling and returning an error message
        return jsonify({'error': str(e)}), 400
    
    except FileNotFoundError:
        # Handling file not found exception
        return jsonify({'error': 'File not found'}), 404

    except Exception as e:
        # Handling of other unforeseen exceptions
        return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)
