class AudioManifest:
    MANIFEST = {
    "@context": "http://iiif.io/api/presentation/3/context.json",
    "id": "http://localhost:8080/api/iiif/presentation/v3/2032438/manifest.json",
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
                    "김소월(기타)"
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
                    "--------"
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
                    "랜드소프트 [제작]"
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
                    "<img src=\"/resource/templete/manpa/img/common/img_ccl_opentype06.png\" alt=\"6 유형\" style=\"height:50px;margin:5px;\" class=\"img_ccl\">"
                ]
            }
        }
    ],
    "items": [
        {
            "id": "http://localhost:8080/api/iiif/presentation/v3/2032438/canvas/p1",
            "type": "Canvas",
            "items": [
                {
                    "id": "http://localhost:8080/api/iiif/presentation/v3/2032438/canvas/p1/page/p1",
                    "type": "AnnotationPage",
                    "items": [
                        {
                            "id": "http://localhost:8080/api/iiif/presentation/v3/2032438/canvas/p1/annotation/p1",
                            "type": "Annotation",
                            "motivation": "painting",
                            "body": {
                                "id": "http://localhost:8080/viewer/f20240206EJEr.mp3",
                                "type": "Sound",
                                "format": "audio/mp3"
                            },
                            "target": "http://localhost:8080/api/iiif/presentation/v3/2032438/canvas/p1"
                        }
                    ]
                }
            ]
        }
    ]
}