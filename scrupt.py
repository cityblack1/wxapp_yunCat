import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yun_cat.settings")
django.setup()
from cat_images.models import CatImage


a = r"""
出现错误
cat/萌猫(●ω/.jpeg
出现错误
cat/家有萌猫练就/.jpeg
出现错误
cat/泰国老虎发春困 笼中打盹似/.jpg
出现错误
cat/陛下这是今日的萌猫动图_这条件反射有点怪怪的.gif
出现错误
cat/遇见萌猫咖啡馆偷得浮生半日闲.jpg
出现错误
cat/电脑壁纸 萌猫壁纸 可爱小猫桌面壁纸下载   (8/10_小箭头图标亲快.jpg
出现错误
cat/笔记本壁纸 萌猫壁纸 暹罗猫高清桌面壁纸下载   (2/9_上一组图_下一.jpeg
出现错误
cat/平板壁纸 动物 萌猫 可爱小猫高清壁纸   (8/10_1024x1024____壁纸.jpg
出现错误
cat/先随海报网编编来看看这只/.jpg
出现错误
cat/萌猫们的/.jpg
出现错误
cat/萌猫合集(18/19.jpg
出现错误
cat/网友称之为/.jpg
出现错误
cat/.jpg
出现错误
cat/美萌猫遭恶搞上演另类/.jpg
出现错误
cat/台一公司养/.jpg
出现错误
cat/日本萌猫表情/.jpg
出现错误
cat/萌猫/.jpg
出现错误
cat/萌猫/.jpg_BApd0fX
出现错误
cat/萌宠猫咪来袭;/n.jpg
出现错误
cat/外边的猫(12)——长着/.jpg
出现错误
cat/创意/.jpg
出现错误
cat/澳大利亚萌猫/.jpg
出现错误
cat/.jpg_hEYXN9u
出现错误
cat/帅男与萌猫的俏皮模仿(15/25.jpg
出现错误
cat/故宫有只小萌猫 网友起名/.jpg
出现错误
cat/外边的猫(12)——长着/.jpg_lOtozL2
出现错误
cat/电脑壁纸 萌猫壁纸 高清猫咪桌面壁纸图片下载   (3/10_小箭头图标亲.jpg
出现错误
cat/外边的猫(12)——长着/.jpg_Yu7n1BA
出现错误
cat/日本萌猫表情/.jpg_fmGaXgu
出现错误
cat/外边的猫(12)——长着/.jpg_8t5JJ7j
出现错误
cat/.jpg_j2OcflO
出现错误
cat/.jpg_97mpRYH
出现错误
cat/台北一公司养/.jpg
出现错误
cat/外边的猫(12)——长着/.jpg_rFdebhK
出现错误
cat/澳萌猫/.jpg
出现错误
cat/台一公司养/.jpg_yi0KySB
出现错误
cat/电脑壁纸 萌猫壁纸 暹罗猫高清桌面壁纸下载   (3/9_小箭头图标亲快.jpeg
出现错误
cat/日本萌猫/.jpg_EEVurzI
出现错误
cat/萌猫/.jpeg
出现错误
cat/澳萌猫/.jpg_VJJDk1t
出现错误
cat/澳萌猫/.jpg_fSNFYM7
出现错误
cat/澳萌猫/.jpg_CjkJVbx
出现错误
cat/14双/.jpg
出现错误
cat/美萌猫遭恶搞上演另类/.jpg_7TvwYXJ
出现错误
cat/我家萌猫/.jpeg
出现错误
cat/外边的猫(12)——长着/.jpg_5z3mdVh
出现错误
cat/40天小萌猫闺中待嫁有喜欢的来喽.jpg
出现错误
cat/4只小萌猫求领养.jpg
出现错误
cat/.jpg_iF3OFcM
出现错误
cat/美国波特兰猫展 众萌猫/.jpg
出现错误
cat/这些萌猫把下水道当成游乐园,还玩起了/.jpg
出现错误
cat/.jpg_Eh0jgC9
出现错误
cat/100多只世界名猫,萌猫空降现场,现场包含/.jpg
出现错误
cat/外边的猫(11) 长着/.jpg
出现错误
cat/外边的猫(12)——长着/.jpg_lsP4tDo
出现错误
cat/共30张宠物图片_萌猫囧态()/30p.jpg
出现错误
cat/看萌猫萌狗练瑜伽(组图) (12/17.jpg
出现错误
cat/《喵星人》天降萌猫 古天乐,马丽双双变身/.jpg
出现错误
cat/南京出现/.jpg
出现错误
cat/一只萌猫暖翻特警/.jpg
出现错误
cat/与网络当红萌猫红小胖一起/.jpg
出现错误
cat/家有萌猫-锁屏精灵.jpg
出现错误
cat/共9张宠物图片大全_萌猫兄弟(索尼 - a500)/9p.jpg
出现错误
cat/.jpg_hJJ4Py5
出现错误
cat/帅男与萌猫的俏皮模仿(14/25.jpg
出现错误
cat/40天小萌猫闺中待嫁有喜欢的来喽_HP9UbDD.jpg
出现错误
cat/回答 喵星人档案 网络爆红的萌猫/.jpg
出现错误
cat/萌猫卡在纸巾盒大秀/.jpg
"""

a = a.split('出现错误')
b = [x.strip() for x in a if x]
c = [x for x in b if x]
all_pic = CatImage.objects.all()
for d in c:
    e = all_pic.get(image=d)
    e.delete()