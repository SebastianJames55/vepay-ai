from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
from io import BytesIO

app = Flask(__name__)

# Load the model
model = tf.saved_model.load('EfficientNet')
classes = ["Fake", "Genuine"]


def predict(file_content):
    img = Image.open(BytesIO(file_content)).convert('RGB')
    img = img.resize((300, 300 * img.size[1] // img.size[0]), Image.BICUBIC)
    inp_numpy = np.array(img)[None]
    inp = tf.constant(inp_numpy, dtype='float32')
    class_scores = model(inp)[0].numpy()
    return classes[class_scores.argmax()]


@app.route('/predict', methods=['POST'])
def predict_logo():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    result = predict(file.read())
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
