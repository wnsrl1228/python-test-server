"""
    - 사용법 - 
    var uv = UV.init(
        "uv",
        {
            manifestUri: "{이곳에 아래 url 추가}",
            configUri: "/resource/uv/config.json",
        },
    );

    단일 이미지 : http://localhost:8080/api/iiif/v2/kmManifests/1839984/manifest.json
    복수 이미지 : http://localhost:8080/api/iiif/v2/kmManifests/2078933/manifest.json

    단일 pdf : http://localhost:8080/api/iiif/v2/kmManifests/2033403/manifest.json
    복수 pdf : http://localhost:8080/api/iiif/v2/kmManifests/1734727/manifest.json

    음원 : http://localhost:8080/api/iiif/v2/kmManifests/2032438/manifest.json
    영상 : http://localhost:8080/api/iiif/v2/kmManifests/2031015/manifest.json
"""
from flask import Flask, request, jsonify, redirect, send_file
import os
from flask_cors import CORS
import base64
from PIL import Image
import logging
import sys

# static 폴더 경로를 sys.path에 추가
sys.path.append(os.path.join(os.path.dirname(__file__), 'static'))
# 로깅 설정
logging.basicConfig(level=logging.DEBUG)  # 디버그 레벨 로그 출력

# 이제 static/images-manifest.py에서 ImagesManifest 클래스 사용 가능
from imagesManifest import ImagesManifest
from imageManifest import ImageManifest

from pdfsManifest import PdfsManifest
from pdfManifest import PdfManifest

from audioManifest import AudioManifest
from videoManifest import VideoManifest

app = Flask(__name__)
CORS(app)  # CORS 설정 추가

# manifest 요청
@app.route('/api/iiif/v2/kmManifests/<string:identifier>/manifest.json', methods=['GET'])
def request_km_manifest(identifier):
    
    json_data = ''
    if identifier == '1839984':  # 단일 이미지
        json_data = ImageManifest.MANIFEST
    elif identifier == '2078933': # 복수 이미지
        json_data = ImagesManifest.MANIFEST
    elif identifier == '2033403': # 단일 pdf
        json_data = PdfManifest.MANIFEST
    elif identifier == '1734727': # 복수 pdf
        json_data = PdfsManifest.MANIFEST
    elif identifier == '2032438': # 음원
        json_data = AudioManifest.MANIFEST
    elif identifier == '2031015': # 영상
        json_data = VideoManifest.MANIFEST


    ###############################################
    # 직접 manifest.json 값 지정하고 싶으면        #
    # 아래 json_data에 값 넣으면 됩니다.            #
    ###############################################
    # json_data = ''
    
    response = jsonify(json_data)
    response.headers.set("Content-Type", "application/json;charset=UTF-8")

    return response

# 이미지 요청
@app.route('/api/iiif/v2/kmImages/<string:identifier>/<string:region>/<string:size>/<string:rotation>/<string:quality>.<string:format>', methods=['GET'])
def iiif_view_km_image(identifier, region, size, rotation, quality, format):

    f = safe_decode(identifier)
    arr_file = f.split("::")

    down_index, down_folder, down_file_name, org_file_name = arr_file
    file_path = os.path.join("./", 'item', down_file_name)

    # 파일 존재 여부 확인
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # 파일 확장자 추출
    format_code = os.path.splitext(file_path)[1].lstrip('.')

    # Content-Type 설정
    mime_type = "image/"+format_code
    print("===")
    print(down_file_name)
    print(down_folder)
    # 이미지 파일을 반환
    return send_file(file_path, mimetype=mime_type)

# pdf, 음원, 영상 요청
@app.route('/viewer/<string:identifier>', methods=['GET'])
def iiif_view_km_file(identifier):

    f = safe_decode(identifier)
    arr_file = f.split("::")

    down_index, down_folder, down_file_name, org_file_name = arr_file
    file_path = os.path.join("./", 'item', down_file_name)

    # 파일 존재 여부 확인
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # 파일 확장자 추출
    format_code = os.path.splitext(file_path)[1].lstrip('.')

    # Content-Type 설정
    mime_type = "image/"+format_code
    print("===")
    print(down_file_name)
    print(down_folder)
    # 이미지 파일을 반환
    return send_file(file_path, mimetype=mime_type)


# 첫 번째 요청 - Redirect 처리 : 이미지 정보 요청
@app.route('/api/iiif/v2/kmImages/<string:identifier>', methods=['GET'])
def redirect_image_info(identifier):
    domain = request.host_url.rstrip('/')
    redirect_url = f"{domain}{request.path}/info.json"
    return redirect(redirect_url, code=303)  # HTTP 303 See Other

# 두 번째 요청 - Image Info 처리 : 이미지 정보 요청
@app.route('/api/iiif/v2/kmImages/<string:identifier>/info.json', methods=['GET'])
def iiif_view_km_image_info(identifier):
    # 실제 처리 로직 추가 필요
    
    f = safe_decode(identifier)
    arr_file = f.split("::")

    down_index, down_folder, down_file_name, org_file_name = arr_file
    file_path = os.path.join("./", down_folder, down_file_name)

    # 파일 존재 여부 확인
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # 파일 확장자 추출
    format_code = os.path.splitext(file_path)[1].lstrip('.')
    
    # 이미지 너비와 높이 추출
    try:
        with Image.open(file_path) as img:
            width, height = img.size
    except Exception as e:
        raise ValueError(f"Failed to get image dimensions: {e}")



    data = {
        "@context": "http://iiif.io/api/image/2/context.json",
        "@id": "http://localhost:8080/api/iiif/v2/kmImages/OjppdGVtOjpmMjAyNDExMjdteFNRLnBuZzo67Iqk7YGs66aw7IO3IDIwMjMtMDMtMDYgMDAyOTA0LnBuZw==",
        "@type": "iiif:Image",
        "protocol": "http://iiif.io/api/image",
        "profile": [
            "http://iiif.io/api/image/2/level0.json",
            {
            "formats": [
                format_code
            ],
            "qualities": [
                "default"
            ],
            "supports": [
                "sizeByWhListed",
                "baseUriRedirect",
                "cors",
                "jsonldMediaType"
            ]
            }
        ],
        "sizes": [
            {
            "width": width,
            "height": height
            }
        ],
        "width": width,
        "height": height
    }
    return jsonify(data)  # JSON 형태로 응답




def safe_decode(encoded_str):
    """
    URL-safe Base64로 인코딩된 문자열을 디코딩합니다.
    :param encoded_str: URL-safe Base64로 인코딩된 문자열
    :return: 디코딩된 문자열
    """
    decoded_bytes = base64.urlsafe_b64decode(encoded_str)
    return decoded_bytes.decode('utf-8')


if __name__ == '__main__':
    app.run(debug=True, port=8080)
    # app.run(debug=True,  port=5000)