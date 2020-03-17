# Contributing

## 选择项目版本

项目使用 3.7.4 版本, 可以使用 [pyenv](https://github.com/pyenv/pyenv) 指定当前 Python 版本.

```shell
$ pyenv local 3.7.4
```

## 创建虚拟环境

使用 Python 原生提供的 [venv](https://docs.python.org/3/library/venv.html) 创建虚拟环境.

```shell
$ python -m venv venv  # 创建虚拟环境
$ source ./venv/bin/activate  # 使用虚拟环境
```

## 生成 `SECRET_KEY`

```shell
(venv)$ python project/management/commands/generate_key.py
```

将生成的 `SECRET_KEY` 复制, 填入 `config/.env` 文件中.

## 数据库创建

使用 `create_schema` 命令创建数据库 schema

```shell
(venv)$ python manage.py create_schema
```

## 依赖管理

### 安装依赖

```shell
(venv)$ pip install requests  # 安装时需要确认已处于虚拟环境中
```

### 导出依赖配置

```shell
$ pip freeze > requirements.txt
```
