# vepay-ai
Handles AI logic for VePay

- Efficient net pre-trained model loaded to use for identifying authentic vs fake logos

## API interaction
- Pass the path of an image in the file field below 
- Request: curl -X POST -F "file=@adidas-green.JPG" http://localhost:5000/predict
- Response: {"result":"Fake/Genuine"}
