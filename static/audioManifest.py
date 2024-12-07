class AudioManifest:
    MANIFEST = {
    "@context": [
      "http://wellcomelibrary.org/ld/ixif/0/context.json",
      "http://iiif.io/api/presentation/2/context.json"
    ],
    "@id": "http://localhost:8080/api/iiif/v2/kmManifests/2032438/manifest.json",
    "@type": "sc:Manifest",
    "label": "",
    "metadata": [
      {
        "label": "제목",
        "value": ""
      },
      {
        "label": "발행자",
        "value": "랜드소프트 [제작]"
      },
      {
        "label": "설명",
        "value": "김소월 시 『개미』를 낭송한 음원자료"
      },
      {
        "label": "발행일자",
        "value": "--------"
      }
    ],
    "sequences": [
      
    ],
    "mediaSequences": [
      {
        "@id": "http://localhost:8080/api/iiif/v2/manifests/2032438/xsequence/s0",
        "@type": "ixif:MediaSequence",
        "elements": [
          {
            "@id": "http://localhost:8080/viewer/f20240206EJEr.mp3",
            "@type": "dctypes:Sound",
            "format": "audio/mp3",
            "thumbnail": "http://localhost:8080/api/iiif/v2/kmImages/Ojpjb2xsZWN0aW9uOjpmMjAyNDAyMTZHUWY1LmpwZzo67J2M7ISxX-yNuOuEpOydvF8wMV_qsJzrr7guanBn/full/max/0/default.jpg",
            "rendering": {
              "@id": "http://localhost:8080/viewer/f20240206EJEr.mp3",
              "format": "audio/mp3"
            }
          }
        ]
      }
    ]
  }