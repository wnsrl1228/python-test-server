class VideoManifest:
    MANIFEST = {
    "@context": "http://iiif.io/api/presentation/3/context.json",
    "id": "http://localhost:8080/api/iiif/presentation/v3/2031015/manifest.json",
    "type": "Manifest",
    "label": {
        "@none": [
            ""
        ]
    },
    "metadata": [
        {
            "label": {
                "@none": [
                    "서명"
                ]
            },
            "value": {
                "@none": [
                    ""
                ]
            }
        },
        {
            "label": {
                "@none": [
                    "저자"
                ]
            },
            "value": {
                "@none": [
                    "국립중앙도서관.디지털기획과(기타)"
                ]
            }
        },
        {
            "label": {
                "@none": [
                    "발행일"
                ]
            },
            "value": {
                "@none": [
                    "2023.11.21"
                ]
            }
        },
        {
            "label": {
                "@none": [
                    "발행자"
                ]
            },
            "value": {
                "@none": [
                    ""
                ]
            }
        },
        {
            "label": {
                "@none": [
                    "저작권유형"
                ]
            },
            "value": {
                "@none": [
                    "<img src=\"/resource/templete/manpa/img/common/img_big_opentype04.png\" alt=\"4 유형\" style=\"height:50px;margin:5px;\" class=\"img_nuri\">"
                ]
            }
        }
    ],
    "items": [
        {
            "id": "http://localhost:8080/api/iiif/presentation/v3/2031015/canvas/p1",
            "type": "Canvas",
            "items": [
                {
                    "id": "http://localhost:8080/api/iiif/presentation/v3/2031015/canvas/p1/page/p1",
                    "type": "AnnotationPage",
                    "items": [
                        {
                            "id": "http://localhost:8080/api/iiif/presentation/v3/2031015/canvas/p1/annotation/p1",
                            "type": "Annotation",
                            "motivation": "painting",
                            "body": {
                                "id": "http://localhost:8080/viewer/f20231121mlJC.mp4",
                                "type": "Video",
                                "format": "video/mp4"
                            },
                            "target": "http://localhost:8080/api/iiif/presentation/v3/2031015/canvas/p1"
                        }
                    ]
                }
            ]
        }
    ]
}