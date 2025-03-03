# Text to mp4 convertor

This is a simple web application that converts text to mp4.

## To run

```shell
docker compose up -d --build
```

## How to use

To convert text to mp4, go to `http://127.0.0.1:8000/text_to_mp4/` and pass
the following parameters:

1. text - text which must be converted.
2. duration (optional) - the duration of the output video. DEFAULT = 2
3. rect_size (optional) - the resolution of the output video. DEFAULT = 100

## Example

![Bot editor](https://github.com/Daniel-March-Portfolio/.github/blob/main/images/TextToMP4/mp4_example.mp4)
