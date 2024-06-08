# Text to mp4 convertor

## To run

### Build docker image

```commandline
docker build . -t convertor
```

### Run docker image

```commandline
docker run -d -p 8000:8000 convertor
```

## How to use

To convert text to mp4, go to `http://127.0.0.1:8000/text_to_mp4/` and pass the following parameters:

1. text - text which must be converted.
2. duration (optional) - the duration of the output video. DEFAULT = 2
3. rect_size (optional) - the resolution of the output video. DEFAULT = 100
