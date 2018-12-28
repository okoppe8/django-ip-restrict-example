# django-ip-restrict-example

Djangoのミドルウェア・デコレータによるIPアドレス制限のサンプル

# 使い方

１．事前にpython(3.5以上)をインストールする。

２．gitでプロジェクトをダウンロードする

```
git clone https://github.com/okoppe8/django-ip-restrict-example.git
```

※ gitがない場合は左上の「Clone or Download」→ 「Download ZIP」でもOK

３．ターミナルよりセットアップコマンドを実行する

windows

```
cd django-ip-restrict-example
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

MacOS/Linux

```
cd django-ip-restrict-example
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

４．開発用サービスを立ち上げてブラウザからURLを開く

windows

```
manage.py runserver
```

MacOS/Linux

```
python manage.py runserver
```

URL

```
http://localhost:8000
```
