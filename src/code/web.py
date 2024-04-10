# from starlette.applications import Starlette
# from starlette.responses import JSONResponse
# from starlette.routing import Route
# from maas.huggingface import HuggingFace
# import os
# import json

# TOKEN = os.getenv("TOKEN")
# MODEL_ID = os.getenv("MODEL_ID") or "openai/whisper-base"
# SERVICE_URL = os.getenv("SERVICE_URL")
# async def homepage(request):
#     if "token" not in request.headers or request.headers["token"] != TOKEN:
#         return JSONResponse({"err_msg": "Invalid token"}, status_code=401)
    
#     payload = await request.body()
#     body = payload.decode("utf-8")
#     output = HuggingFace(MODEL_ID, service_url=SERVICE_URL).invoke(json.loads(body))
#     return JSONResponse(output)


# app = Starlette(
#     routes=[
#         Route("/", homepage, methods=["POST"]),
#     ],
# )

from flask import Flask, request, jsonify
from maas.huggingface import HuggingFace
import os
import json

TOKEN = os.getenv("TOKEN")
MODEL_ID = os.getenv("MODEL_ID") or "openai/whisper-base"
SERVICE_URL = os.getenv("SERVICE_URL")

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_data():
    if "token" not in request.headers or request.headers["token"] != TOKEN:
        return jsonify({"err_msg": "Invalid token"})
    payload = request.data
    output = HuggingFace(MODEL_ID, service_url=SERVICE_URL).invoke(json.loads(payload))
    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
