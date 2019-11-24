from converter import Converter
c = Converter()

info = c.probe('test1.ogg')

conv = c.convert('test1.ogg', '/tmp/output.mkv', {
    'format': 'mkv',
    'audio': {
        'codec': 'wav',
        'samplerate': 11025,
        'channels': 2
    },
    'video': {
        'codec': 'h264',
        'width': 720,
        'height': 400,
        'fps': 15
    }})


