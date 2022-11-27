# from draw_text import watermark_text

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def watermark_text(input_file, output_file, text, pos, f_font=None, f_size=100, show=True, save=False):
    image = Image.open(input_file)
    drawing = ImageDraw.Draw(image)
    color = (12, 8, 125)
    font = ImageFont.truetype(f_font, f_size)

    for i in range(len(text)):
        drawing.text(pos[i], text[i], fill=color, font=font)

    if show:
        image.show()
    if save:
        image.save(output_file)

if __name__ == '__main__':
    img = 'Shablon_gramoty.jpg'
    watermark_text(img, 'out.jpg', text='Test!', pos=(200, 300))

def gramota(input_file, output_file, name, full_name, best_in, date, Who, f_font='Шрифт.otf', f_size=50, show=True, save=False):
    text = ['Награждается', f'{name} {full_name}', 'В наминации', best_in,    'Дата',    date,      'Подписал', Who]
    pos =  [(200, 300),     (200, 350),             (200, 450),   (150, 500), (80, 800), (80, 850), (400, 800), (400, 850)]
    watermark_text(input_file, output_file, text=text, pos=pos, f_font=f_font, f_size=50, show=show, save=save)