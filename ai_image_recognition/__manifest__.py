# -*- coding: utf-8 -*-
# Copyright 2018 Jarvis (www.odoomod.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


{
    'name': 'Image Recognition',
    'summary': 'Image Recognition',
    'version': '1.1',
    'category': 'Extra Tools',
    'description': """
Tensorflow Image Recognition

Installation:
First installation takes a long time, because file will be download automatically. 
If download failure, you need download 'http://download.tensorflow.org/models/image/imagenet/inception-2015-12-05.tgz', and create a folder 'imagenet' at this module dir, then decompress file in the this folder

安装：
模块首次安装需要一定时间，因为有文件会自动下载。
如果下载失败，则你需要手动下载‘http://download.tensorflow.org/models/image/imagenet/inception-2015-12-05.tgz’，并在模块文件夹建立‘imagenet’子文件夹，把文件解压到那里
https://storage.googleapis.com/download.tensorflow.org/models/inception_v3_2016_08_28_frozen.pb.tar.gz
""",
    'author': "OnGood, Jarvis (www.odomod.com)",
    'website': 'https://www.ongood.cn',
    'license': 'AGPL-3',
    'depends': ['base'
    ],
    'external_dependencies': {
        'python': ['numpy', 'tensorflow'],
        'bin': [],
    },
    'data': [
        'views/views.xml',
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
}
