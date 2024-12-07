class ImageManifest:
    MANIFEST = {
    "@context": "http://iiif.io/api/presentation/2/context.json",
    "@id": "http://localhost:8080/api/iiif/v2/kmManifests/1839984/manifest.json",
    "@type": "sc:Manifest",
    "label": "(강소천 동화집) 조그만 사진첩",
    "metadata": [
      {
        "label": "제목",
        "value": "(강소천 동화집) 조그만 사진첩"
      },
      {
        "label": "발행자",
        "value": "南鄕文化社"
      },
      {
        "label": "설명",
        "value": ""
      },
      {
        "label": "발행일자",
        "value": "19540401"
      }
    ],
    "sequences": [
      {
        "@id": "http://localhost:8080/api/iiif/v2/manifests/1839984/sequence/s0",
        "@type": "sc:Sequence",
        "viewingHint": "paged",
        "canvases": [
          {
            "@id": "http://localhost:8080/api/iiif/v2/manifests/1839984/canvas/p1",
            "@type": "sc:Canvas",
            "label": "1",
            "thumbnail": {
              "@id": "http://localhost:8080/api/iiif/v2/kmImages/OjppdGVtOjpmMjAyNDA2MjE5TWhiLmpwZzo6KOqwleyGjOyynCDrj5ntmZTsp5EpIOyhsOq3uOunjCDsgqzsp4TssqkuanBn/full/max/0/default.jpg",
              "@type": "dctypes:Image",
              "height": 2048,
              "width": 1254
            },
            "height": 2048,
            "width": 1254,
            "images": [
              {
                "@id": "http://localhost:8080/api/iiif/v2/manifests/1839984/canvas/p1/painting/anno",
                "@type": "oa:Annotation",
                "motivation": "sc:painting",
                "resource": {
                  "@id": "http://localhost:8080/api/iiif/v2/kmImages/OjppdGVtOjpmMjAyNDA2MjE5TWhiLmpwZzo6KOqwleyGjOyynCDrj5ntmZTsp5EpIOyhsOq3uOunjCDsgqzsp4TssqkuanBn/full/max/0/default.jpg",
                  "@type": "dctypes:Image",
                  "format": "image/jpeg",
                  "service": {
                    "@context": "http://iiif.io/api/image/2/context.json",
                    "@id": "http://localhost:8080/api/iiif/v2/kmImages/OjppdGVtOjpmMjAyNDA2MjE5TWhiLmpwZzo6KOqwleyGjOyynCDrj5ntmZTsp5EpIOyhsOq3uOunjCDsgqzsp4TssqkuanBn",
                    "profile": "http://iiif.io/api/image/2/level0.json"
                  },
                  "height": 2048,
                  "width": 1254
                },
                "on": "http://localhost:8080/api/iiif/v2/manifests/1839984/canvas/p1"
              }
            ]
          }
        ]
      }
    ]
  }