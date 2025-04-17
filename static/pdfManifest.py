class PdfManifest:
    MANIFEST = {
    "@context": "http://iiif.io/api/presentation/3/context.json",
    "id": "http://localhost:8080/api/iiif/presentation/v3/2033403/manifest.json",
    "type": "Manifest",
    "label": {
        "@none": [
            "『이어령의 序』 전시도록"
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
                    "『이어령의 序』 전시도록"
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
                    "국립중앙도서관(기타)"
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
                    "20230423"
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
                    "국립중앙도서관"
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
            "id": "http://localhost:8080/api/iiif/presentation/v3/2033403/canvas/p1",
            "type": "Canvas",
            "items": [
                {
                    "id": "http://localhost:8080/api/iiif/presentation/v3/2033403/canvas/p1/page/p1",
                    "type": "AnnotationPage",
                    "items": [
                        {
                            "id": "http://localhost:8080/api/iiif/presentation/v3/2033403/canvas/p1/annotation/p1",
                            "type": "Annotation",
                            "motivation": "painting",
                            "body": {
                                "id": "http://localhost:8080/viewer/f202403055QFx.pdf",
                                "type": "PDF",
                                "format": "application/pdf"
                            },
                            "target": "http://localhost:8080/api/iiif/presentation/v3/2033403/canvas/p1"
                        }
                    ]
                }
            ]
        }
    ]
}