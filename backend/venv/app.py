from flask import Flask, request, jsonify # type: ignore
from werkzeug.utils import secure_filename # type: ignore
import os
import logging

# Flask Application Setup
app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'txt'}

# Create the upload directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def allowed_file(filename):
    """
    Check if a file's extension is allowed.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Handle file upload and process form data.
    """
    try:
        # Validate presence of required fields
        if 'name' not in request.form or 'age' not in request.form:
            return jsonify({'error': 'Missing name or age fields'}), 400
        
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400

        name = request.form['name']
        age = request.form['age']
        file = request.files['file']

        # Validate file
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            logging.info(f"File '{filename}' saved successfully.")
        else:
            return jsonify({'error': 'Invalid file format'}), 400

        # Log received data
        logging.info(f"Data received: name={name}, age={age}")

        return jsonify({'message': 'Data received successfully!', 'name': name, 'age': age}), 200
    except KeyError as ke:
        logging.error(f"KeyError occurred: {ke}")
        return jsonify({'error': f'Missing field: {ke}'}), 400
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
        return jsonify({'error': 'An internal server error occurred'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5000)
