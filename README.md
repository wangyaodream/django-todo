# Todo list with django and react

## Task todo

- [x] 后端Django逻辑实现
- [x] 前端React模板实现
- [x] 增加前后端交互
- [ ] 完善交互功能
- [ ] 嵌入其他功能

## Usage

### 后端
终端进入到backend目录安装依赖
```shell
pip install -r requirements.txt
```

初始化数据库数据
```shell
python manage.py migrate
```

创建超级账户
```shell
python manage.py createsuperuser
```
*ps:超级账户的目的是为了进入到系统管理界面以UI界面的形式添加数据*

启动后端服务
```shell
python manage.py runserver
```

### 前端
终端进入到frontend目录安装依赖
```shell
npm i
```

启动前端服务
```shell
npm start
```

