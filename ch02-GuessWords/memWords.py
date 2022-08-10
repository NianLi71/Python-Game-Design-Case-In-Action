'''
功能:
1. 录入单词:
hello 你好
today 今天
2. 查找单词, 查中文, 查英文, 都支持
3. 随机测试, 显示5个英文, 用户输入中文, 并统计回答正确率
'''

import os
import random
from statistics import mean
from typing import Dict

debug = os.environ.get('DEBUG') == 'True'

preset_word_dict = {
    'hello': '你好',
    'today': '今天',
    'tomorrow': '明天',
    'food': '食物',
    'moon': '月亮',
    'China': '中国'
}

words_dict = preset_word_dict.copy()

def reverse_dict(d: Dict) -> Dict:
    '''
    return a new dict with keys as values and values as keys
    '''
    new_dict = {}
    for k, v in d.items():
        new_dict[v] = k
    return new_dict

rev_words_dict = reverse_dict(words_dict)


def save():
    keep_typing = True
    while(keep_typing):
        word_line = input("Input a English word and a Chinese meaning, separated by a space, for example: hello 你好. Leave a empty line to exit.\n")
        word_line = word_line.strip()
        if not word_line:
            keep_typing = False
        else:
            word, meaning = word_line.split(' ')
            words_dict[word] = meaning
            rev_words_dict[meaning] = word
    if debug:
        print(words_dict)
        print(rev_words_dict)

def search():
    keep_typing = True
    while(keep_typing):
        text = input('请输入希望查找的英文或者中文:')
        if not text:
            keep_typing = False
        elif text in set(words_dict.keys()):
            print(words_dict[text])
        elif text in set(rev_words_dict.keys()):
            print(rev_words_dict[text])
        else:
            print(f'找不到与"{text}"相关的单词')


def testing():
    print('测试开始, 每次测试5个单词, 请输入英文单词对应的中文意思.')

    pick_number = 5
    picked_words = random.sample(list(words_dict.items()), k=pick_number)
    if debug:
        print(picked_words)

    correct_count = 0
    for word, meaning in picked_words:
        user_typed_meaning = input(f'{word}:')
        if user_typed_meaning == meaning:
            correct_count += 1
    print(f'测试完毕, 正确率是: {float(correct_count)/pick_number*100}%')


if __name__ == '__main__':
    print("轻轻松松背单词!")
    while(True):
        print('\n功能列表:\n'
        '1.save words\n'
        '2.search word\n'
        '3.testing\n'
        '4.exit'
        )
        option = input("请输入功能对应序号:")
        function_map = {
            '1': save,
            '2': search,
            '3': testing,
            '4': lambda: ( print("Byebye~"), exit(0) )
        }

        if option in function_map:
            function_map[option]()
        else:
            print('输入的选项有误, 请重新输入')