from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

from rest_framework.parsers import JSONParser

from cat_images.models import CatImage
from cat_images.serializers import ModelImageSerializer
from cat_images.fix_width import arrange_image

import random


# 优化过后的版本, 减少了数据库的损耗
@csrf_exempt
def cat_images_list(request):
    if request.method == 'GET':
        phone_width = int(request.GET.get('phone_width', 375))
        sort_map = {'0': '-like_nums', '1': '-created', '2': '?'}
        # pixel = int(request.GET.get('pixel', 2))
        width = phone_width
        current = int(request.GET.get('index', '0'))
        sort = sort_map[request.GET.get('order', '0')]  # 通过字典映射得到sort代表的值
        if sort == '?':
            cat_images = [_ for _ in CatImage.objects.all()]
            random.shuffle(cat_images)
            cat_images = cat_images[0: 20]
            # cat_images = cat_images[0:20]
        else:
            cat_images = CatImage.objects.all().order_by(sort)
            if current == 0:
                current = cat_images[0].id
            i = CatImage.objects.get(id=current)
            all_list = [_ for _ in cat_images]
            index = all_list.index(i)
            cat_images = cat_images[index + 1: index + 21] if current != 5778 else cat_images[index: index + 20]
        all_data = ModelImageSerializer(cat_images, many=True).data
        all_data = arrange_image(all_data, width=width)
        current = cat_images[-1].id
        return JsonResponse(dict(data=all_data, index=current), safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ModelImageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def cat_image_detail(request, pk):
    cat_image = get_object_or_404(CatImage, id=pk)

    if request.method == "GET":
        serializer = ModelImageSerializer(cat_image)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ModelImageSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        cat_image.delete()
        return HttpResponse('删除成功', status=204)


# 调试的时候删掉不想要的
# def delete(request):
#     try:
#         id = int(request.GET.get('id'))
#         a = CatImage.objects.get(id=id)
#         a.delete()
#     except:
#         pass
#     return HttpResponse('')


@csrf_exempt
def upload_images(request):
    from PIL import Image
    image = request.FILES['file']
    title = request.POST['name'] if request.POST.get('name', '') else '网友很懒, 还没上传标题'
    image_instance = CatImage()
    image_instance.title = title
    image_instance.image = image
    pil_image = Image.open(image.file)
    image_instance.width, image_instance.height = pil_image.size
    image_instance.save()
    image_instance.save_zip()
    return JsonResponse({}, status=200)