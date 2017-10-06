import random


def arrange_image(images, width=None): # images 是包含Image对象的列表
    processed_images = []
    for i in generate_lst(images):
        new_images = calculate_height(i, p_width=width)
        processed_images.append(new_images)
    return processed_images


# 将传递进来的图像列表调整成统一的高度
def calculate_height(images, p_width=None): # images是介于1, 3的随机Image对象的列表
    width = 0
    for i in images:
        width += float(i['width']) / i['height']
    height = 1 / width    # ip6 height = WIDTH / width
    # scale = i.width * height / i.height 是缩放比例
    images = [i for i in images if not process_scale(i, height, p_width)]
    return images


def process_scale(i, h, w):
    width, height = i['width'], i['height']
    i['width'] = width * h / height * 100
    i['height'] = h * w


def generate_lst(lst):
    yield [lst[0]]
    lst = lst[1:]
    while len(lst) > 3:
        p = random.random()
        if p < 0.5:
            r = 2
        else: r = 3 if p > 0.75 else 1
        yield lst[0: r]
        lst = lst[r:]
    yield lst


# print(arrange_image(images))
# t2 = datetime.now()
# print(t2 - t1)

