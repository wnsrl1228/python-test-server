class VideoManifest:
    MANIFEST = {
    "@context": [
      "http://wellcomelibrary.org/ld/ixif/0/context.json",
      "http://iiif.io/api/presentation/2/context.json"
    ],
    "@id": "http://localhost:8080/api/iiif/v2/kmManifests/2031015/manifest.json",
    "@type": "sc:Manifest",
    "label": "",
    "metadata": [
      {
        "label": "제목",
        "value": ""
      },
      {
        "label": "발행자",
        "value": ""
      },
      {
        "label": "설명",
        "value": ""
      },
      {
        "label": "발행일자",
        "value": "2023.11.21"
      }
    ],
    "sequences": [
      
    ],
    "mediaSequences": [
      {
        "@id": "http://localhost:8080/api/iiif/v2/manifests/2031015/xsequence/s0",
        "@type": "ixif:MediaSequence",
        "elements": [
          {
            "@id": "http://localhost:8080/viewer/f20231121mlJC.mp4",
            "@type": "dctypes:MovingImage",
            "format": "video/mp4",
            "thumbnail": "http://localhost:8080/api/iiif/v2/kmImages/Ojpjb2xsZWN0aW9uOjpmMjAyMzExMjFFaWxOLnBuZzo67J207IOBX-uPmeyYgeyDgV_sjbjrhKTsnbwucG5n/full/max/0/default.jpg",
            "rendering": {
              "@id": "http://localhost:8080/viewer/f20231121mlJC.mp4",
              "format": "video/mp4"
            }
          }
        ]
      }
    ]
  }