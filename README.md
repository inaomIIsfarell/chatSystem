``` 启动：python manage.py runserver```
```
mysite/
├── app1
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-38.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-38.pyc
│   │   ├── apps.cpython-38.pyc
│   │   ├── __init__.cpython-38.pyc
│   │   ├── models.cpython-38.pyc
│   │   └── views.cpython-38.pyc
│   ├── static                                       【静态文件】
│   │   ├── css                                      【css样式库】
│   │   ├── jslib                                    【js样式库】
│   │   ├── model                                    【模型】（貌似是不正规写法）
│   │   │   ├── args.py                              【模型参数】
│   │   │   ├── generation.py                        【模型预测】
│   │   │   ├── initialization.py                    【模型初始化】
│   │   │   └── __pycache__
│   │   │       ├── args.cpython-38.pyc
│   │   │       ├── generation.cpython-38.pyc
│   │   │       └── initialization.cpython-38.pyc
│   │   └── plugins                                  【工具插件】
│   │       ├── __pycache__
│   │       │   └── utils.cpython-38.pyc
│   │       └── utils.py                             【为翻译模型输出提供方法】
│   ├── templates                                    【模板库】
│   │   ├── dialogue.html
│   │   └── index.html
│   ├── tests.py
│   └── views.py                                     【视图函数】
├── db.sqlite3
├── manage.py
├── mysite
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   ├── settings.cpython-38.pyc
│   │   ├── urls.cpython-38.pyc
│   │   └── wsgi.cpython-38.pyc
│   ├── settings.py                                  【配置文件】
│   ├── urls.py                                      【URL和python函数的对应关系】
│   └── wsgi.py
└── __pycache__
    └── manage.cpython-38.pyc

```[输入链接说明](http://)