#coding=utf-8
from flask import render_template, request, \
    current_app
from . import scpic
import sys
import platform

reload(sys)
sys.setdefaultencoding('utf-8')


#current_app.config['UPLOADED_PHOTOS_DEST']
import os
def getDate(fileurl):
    loadfile = [fileurl]
    imagedata = []
    while(loadfile):
        try:
            path = loadfile.pop()
            #print path
            for x in os.listdir(path):
                if os.path.isfile(os.path.join(path,x)):
                    imagedata.append(x)
                else:
                    loadfile.append(os.path.join(path,x))


        except Exception,e:
            print str(e) + path

    return imagedata

def getfile(fileurl):
    loadfile = [fileurl]
    imagefile = []
    while(loadfile):
        try:
            path = loadfile.pop()
            for x in os.listdir(path):
                if os.path.isfile(os.path.join(path,x)):
                    pass
                else:
                    loadfile.append(os.path.join(path,x))
                    if(platform.system()=='Windows'):
                        imagefile.append(x.decode('gbk'))
                    else:
                        imagefile.append(x)
        except Exception,e:
            print str(e) + path

    return imagefile

@scpic.route('/piclist', methods=['GET', 'POST'])
def piclist():
    file_url =  getfile(current_app.config['UPLOADED_PHOTOS_DEST'])
    print file_url
    # getDate(getfile(current_app.config['UPLOADED_PHOTOS_DEST'])[0])
    return render_template('scpic/filelist.html',file_url=file_url)

import re
@scpic.route('/pics/<pic>', methods=['GET', 'POST'])
def pic(pic):
    image_list = getDate(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'],pic))
    image_list = sorted(image_list,key = lambda i:int(re.match(r'(\d+)',i).group()))
    print image_list
    return render_template('scpic/test.html',pic=pic,image_list=image_list)


ALLOWED_EXTENSIONS = ['jpg', 'png']

def allowe_file(filename):
    '''
    限制上传的文件格式
    :param filename:
    :return:
    '''
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS


@scpic.route('/upload', methods=['GET', 'POST'])
def updata():
    return render_template('scpic/upload.html')

@scpic.route('/index', methods=['GET', 'POST'])
def index():
    return "ok"
import os
from werkzeug.utils import secure_filename
import uuid
@scpic.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    # file = request.files.get('文件名') # 获取文件
    filelist = request.files.getlist("fileFolder")
    for file in filelist:
        filename = secure_filename(file.filename)  # 获取文件名
        mkdir(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'],file.filename.split('/')[0]))
        print os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'],file.filename.split('/')[0])
        file.save(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'], file.filename)) # 保存文件
    excel_dict = {}
    return "ok"


def mkdir(path):

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    print path
    isExists=os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        #print path+' 创建成功'
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        #print path+' 目录已存在'
        return False