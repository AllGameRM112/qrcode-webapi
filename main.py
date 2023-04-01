from flask import Flask, request, make_response
import qrcode
import io

app = Flask(__name__)

@app.route('/api/v1/generate_qr_code', methods=['GET'])
def generate_qr_code():
    data = request.args.get('data', '')
    img = qrcode.make(data)
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    response = make_response(img_io.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
