## 환경 세팅

1. 파이썬 설치
    - https://dotiromoook.tistory.com/32
2. vs code의 marketplace에서 python 설치
3. pip install flask flask-cors
4. pip install pillow

## 사용법 

본인 UV 프로젝트에 아래 URL만 추가하면 됩니다.

ex) 
``` html
     var uv = UV.init(
        "uv",
        {
            manifestUri: "이곳에 보고 싶은 아래 url 추가",
            configUri: "/resource/uv/config.json",
        },
    );
```

- 단일 이미지 : http://localhost:8080/api/iiif/v2/kmManifests/1839984/manifest.json
- 복수 이미지 : http://localhost:8080/api/iiif/v2/kmManifests/2078933/manifest.json

- 단일 pdf : http://localhost:8080/api/iiif/v2/kmManifests/2033403/manifest.json
- 복수 pdf : http://localhost:8080/api/iiif/v2/kmManifests/1734727/manifest.json

- 음원 : http://localhost:8080/api/iiif/v2/kmManifests/2032438/manifest.json
- 영상 : http://localhost:8080/api/iiif/v2/kmManifests/2031015/manifest.json
