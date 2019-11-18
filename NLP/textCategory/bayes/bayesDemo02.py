# -*- coding:utf-8 -*-

import random
import jieba
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer, HashingVectorizer, CountVectorizer
from sklearn import metrics
from sklearn.naive_bayes import BernoulliNB

'''
    贝叶斯：文本分类
'''

jieba.load_userdict("../atomic.txt")    # 不可切分词

'''
    加载数据集：最原始文本集
'''
def get_dataset():
    data = []
    with open("../原始例句.txt", encoding="utf-8", errors="ignore") as fo:
        for line in fo.readlines():
            arr = line.strip().split("\t")
            data.append((get_words(arr[0]), arr[1]))
    random.shuffle(data)    # 随机打乱
    return data

'''
    加载数据集：分离出的关键字对应材料
'''
def load_dataset():
    data = []
    with open("../keywords_intention.txt", encoding="utf-8", errors="ignore") as fo:
        for line in fo.readlines():
            arr = line.strip().split("\t")
            data.append((arr[0].replace(",", " "), arr[1]))
    random.shuffle(data)    # 随机打乱
    return data


def getWordList(filepath):
    keySet = []
    with open(filepath, encoding="utf-8", errors="ignore") as fo:
        for line in fo.readlines():
            keySet.append(line.strip())
    return set(keySet)

zhuhai_c = getWordList("../zhuhai.txt")
others = getWordList("../others.txt")

'''
    获取所有关键字
'''
def getAllKeywords(zhuhai_c, others):
    keywords = []
    with open("../keywords_intention.txt", encoding="utf-8") as fo:
        lines = fo.readlines()
        for line in lines:
            arr = line.strip().split("\t")
            for k in arr[0].strip().split(","):
                if k in zhuhai_c:
                    keywords.append("地名1")
                elif k in others:
                    keywords.append("地名2")
                else:
                    keywords.append(k)
    return set(keywords)

keywords = getAllKeywords(zhuhai_c, others)


'''
    获取文档中的关键词
'''
def get_words(line):
    s = ""
    arr = jieba.cut(line)
    for a in arr:
        if a in zhuhai_c:
            a = "地名1"
        elif a in others:
            a = "地名2"
        elif a in keywords:
            a = a
        else:
            a = ""
        if len(a)>0:
            s = s + a + " "
    return s.strip(" ")


'''
    划分训练集和测试集
'''
def split_train_and_test_set(data):
    filesize = int(0.7 * len(data))    # 训练集:测试集=7:3

    train_set = [each[0] for each in data[:filesize]]
    train_label = [each[1] for each in data[:filesize]]

    test_set = [each[0] for each in data[filesize:]]
    test_label = [each[1] for each in data[filesize:]]
    return train_set, train_label, test_set, test_label

'''
    多项式分类器
'''
def multinamialNB(train_set, train_label, test_set, test_label):
    nbc = Pipeline([
        ('vect', TfidfVectorizer(

        )),
        ('clf', MultinomialNB(alpha=1.0))
    ])

    nbc.fit(train_set, train_label)    # 训练多项式分类器
    predict = nbc.predict(test_set)    # 测试分类器分类效果
    count = 0
    for left, right, tset in zip(predict, test_label, test_set):
        # print(left, "-->", right, "-->", tset)
        if left == right:
            count += 1
    print("多项式分类器准确率：", count/len(test_label))

'''
    伯努利分类器
'''
def bernousNB(train_set, train_label, test_set, test_label):
    nbc_1 = Pipeline([
        ('vect', TfidfVectorizer(

        )),
        ('clf', BernoulliNB(alpha=0.1))
    ])
    nbc_1.fit(train_set, train_label)
    predict = nbc_1.predict(test_set)  # 在测试集上预测结果
    count = 0  # 统计预测正确的结果个数
    for left, right in zip(predict, test_label):
        if left == right:
            count += 1
    print("伯努利分类器准确率：", count / len(test_label))




def main():
    for i in range(100):    # 多轮训练
        data = get_dataset()    # 加载最原始的输入数据
        # data = load_dataset()  # 加载手动提取的关键词数据
        train_set, train_label, test_set, test_label = split_train_and_test_set(data)
        print("第", i, "轮：")
        multinamialNB(train_set, train_label, test_set, test_label)
        bernousNB(train_set, train_label, test_set, test_label)

    ## 新想法：全部数据用来训练，新截取关键词用来测试

if __name__ == '__main__':
    main()