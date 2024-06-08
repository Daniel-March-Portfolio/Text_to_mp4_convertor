from django.http import FileResponse
from django.core.exceptions import ValidationError, BadRequest
from TextToMP4.models import TextToMP4Requests
from TextToMP4.utils.text_to_mp4 import convert_text_to_mp4


def index(request):
    params = parse_params(request)
    TextToMP4Requests.objects.create(**params)
    file = convert_text_to_mp4(**params)
    return FileResponse(file, filename="converted.mp4")


def parse_params(request):
    text = request.GET.get("text", None)
    duration = request.GET.get("duration", "2")
    rect_size = request.GET.get("rect_size", "100")

    if not text:
        raise BadRequest("No text provided")
    if not duration.isdigit():
        raise ValidationError("Duration must be a number")
    if not rect_size.isdigit():
        raise ValidationError("Rect size must be a number")

    return {"text": text, "duration": int(duration), "rect_size": int(rect_size)}
