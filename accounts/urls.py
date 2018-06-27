from django.conf.urls import url, include
from . import views

app_name = "accounts"

urlpatterns = [
    url(r'^signup/$',views.signup_view, name="signup"),
    # url(r'^(?P<slug>[\w-]+)/', views.article_detail, name="detail"),
]
