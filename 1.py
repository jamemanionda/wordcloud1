import random

import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

frequency_d = {
    '모르핀':12323,
    '메스암페타민':11112,
    '엑스터시':10018,
    '암페타민':3522,
    '너바나':2098,
    '바이오디젤':1989,
    '클로나제팜':1304,
    '세로토닌':1288,
    '클로로포름':932,
    '케타민':919,
    '니코틴':900,
    '디아제팜':891,
    '미생물':811,
    '그로잉':511,
    '구연산':503,
    '과산화수소':487,
    '밀반입':412,
    '그로우':398,
    '물갈이':351,
    '극소량':330
}
def my_tf_color_func(dictionary):
  def my_tf_color_func_inner(word, font_size, position, orientation, random_state=None, **kwargs):
      return ("hsl({:d},{:d}%, {:d}%)".format(np.random.randint(120, 333), np.random.randint(20, 32),
                                              np.random.randint(35, 80)))
  return my_tf_color_func_inner

wc = WordCloud(width=1100, height=600, background_color="white", random_state=0, font_path=r'c:\Windows\Fonts\malgun.ttf', prefer_horizontal=1, color_func=my_tf_color_func(frequency_d))
plt.imshow(wc.generate_from_frequencies(frequency_d))
plt.axis("off")
plt.show()
plt.savefig('network.png')