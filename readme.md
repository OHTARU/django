## Django & Django REST Framework API Server Tutorial

이 프로젝트는 Django와 Django REST Framework를 사용하여 간단한 API 서버를 만드는 과정을 다룹니다. Django는 Python 기반의 강력한 웹 프레임워크이며, Django REST Framework는 Django를 위한 강력한 API 구축 도구입니다.
이 튜토리얼은 초심자를 대상으로 하며, 단계별로 API 서버를 구축하는 방법을 설명합니다.

## Installation

1. 가상환경 생성 및 활성화:

    ```bash
    python -m venv myenv
    source myenv/bin/activate  # MacOS/Linux
    myenv\Scripts\activate  # Windows
    ```

2. 필수 패키지 설치:

    ```bash
    pip install django djangorestframework
    ```

3. Django 프로젝트 생성:

    ```bash
    django-admin startproject myproject
    cd myproject
    ```

4. Django 앱 생성:

    ```bash
    python manage.py startapp myapp
    ```

5. `settings.py` 파일 수정:

    ```python
    INSTALLED_APPS = [
        ...,
        'rest_framework',
        'myapp',
    ]
    ```

6. 초기 마이그레이션 및 서버 실행:

    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

서버가 성공적으로 실행되면, `http://127.0.0.1:8000/`에서 Django 기본 페이지를 볼 수 있습니다.


## Setting up Models and Serializers

1. 모델 정의:

    `myapp/models.py` 파일을 열고 다음과 같이 모델을 정의합니다.

    ```python
    from django.db import models

    class Item(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
    ```

2. 시리얼라이저 설정:

    `myapp/serializers.py` 파일을 생성하고 다음과 같이 작성합니다.

    ```python
    from rest_framework import serializers
    from .models import Item

    class ItemSerializer(serializers.ModelSerializer):
        class Meta:
            model = Item
            fields = '__all__'
    ```

3. 마이그레이션 적용:

    ```bash
    python manage.py makemigrations myapp
    python manage.py migrate
    ```


## Setting up Views and URLs

1. 뷰 정의:

    `myapp/views.py` 파일에서 다음과 같이 API 뷰를 정의합니다.

    ```python
    from rest_framework import viewsets
    from .models import Item
    from .serializers import ItemSerializer

    class ItemViewSet(viewsets.ModelViewSet):
        queryset = Item.objects.all()
        serializer_class = ItemSerializer
    ```

2. URL 설정:

    `myapp/urls.py` 파일을 생성하고 다음과 같이 설정합니다.

    ```python
    from django.urls import path, include
    from rest_framework.routers import DefaultRouter
    from .views import ItemViewSet

    router = DefaultRouter()
    router.register(r'items', ItemViewSet)

    urlpatterns = [
        path('', include(router.urls)),
    ]
    ```

    또한, `myproject/urls.py` 파일에 `myapp.urls`를 포함시킵니다.

    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/', include('myapp.urls')),
    ]
    ```

## Running and Testing

1. 서버 실행:

    ```bash
    python manage.py runserver
    ```

2. API 테스트:

    브라우저 또는 Postman과 같은 도구를 사용하여 다음 URL을 통해 API를 테스트할 수 있습니다.

    - `GET /api/items/` : 아이템 목록 가져오기
    - `POST /api/items/` : 새로운 아이템 생성
    - `GET /api/items/<id>/` : 특정 아이템 가져오기
    - `PUT /api/items/<id>/` : 특정 아이템 업데이트
    - `DELETE /api/items/<id>/` : 특정 아이템 삭제


#### 참고 자료https://codemonkyu.tistory.com/entry/Djnago-Django-rest-framework-%ED%99%9C%EC%9A%A9%ED%95%98%EC%97%AC-API-%EC%84%9C%EB%B2%84-%EB%A7%8C%EB%93%A4%EA%B8%B0





form 사용할때 쓰는 부트스트랩 주소 : https://getbootstrap.com/docs/5.1/getting-started/download/