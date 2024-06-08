import io
import tempfile

import numpy as np
from moviepy.config import change_settings
from moviepy.editor import TextClip, VideoClip

change_settings({"IMAGEMAGICK_BINARY": "/usr/bin/convert"})


def frame_maker_wrapper(text, video_width, video_height, duration):
    def make_frame(t):
        font_path = "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf"
        text_clip = TextClip(text, fontsize=24, font=font_path, color='white', bg_color='black')

        text_width = text_clip.w
        x = video_width - int((video_width + text_width) * (t / duration))
        y = video_height // 2

        frame = np.zeros((video_height, video_width, 3), dtype='uint8')

        if x < video_width and x + text_width > 0:
            text_frame = text_clip.get_frame(t)
            x_start = max(x, 0)
            x_end = min(x + text_width, video_width)
            frame_y_start = y - text_clip.h // 2
            frame_y_end = frame_y_start + text_clip.h

            text_x_start = max(0, -x)
            text_x_end = text_x_start + (x_end - x_start)

            if frame_y_start >= 0 and frame_y_end <= video_height:
                frame[frame_y_start:frame_y_end, x_start:x_end] = \
                    text_frame[:, text_x_start:text_x_end]
            elif frame_y_start < 0:
                frame[0:frame_y_end, x_start:x_end] = \
                    text_frame[-frame_y_start:frame_y_end, text_x_start:text_x_end]
            elif frame_y_end > video_height:
                frame[frame_y_start:video_height, x_start:x_end] = \
                    text_frame[0:video_height - frame_y_start, text_x_start:text_x_end]

        return frame

    return make_frame


def convert_text_to_mp4(text, duration, rect_size) -> io.BytesIO:
    fps = 24
    video = VideoClip(frame_maker_wrapper(text, rect_size, rect_size, duration), duration=duration)
    with tempfile.NamedTemporaryFile(suffix=".mp4") as temp_file:
        video.write_videofile(temp_file.name, fps=fps, codec='libx264')
        temp_file.seek(0)
        file = io.BytesIO(temp_file.read())
    file.seek(0)
    return file
