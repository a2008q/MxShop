"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from MxShop.settings import MEDIA_ROOT, STATIC_ROOT
from django.views.static import serve
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_swagger.views import get_swagger_view

from goods.views import GoodsListViewSet, CategoryViewSet, HotSearchsViewset, BannerViewSet, IndexCategoryViewset
from users.views import SmsCodeViewSet, UserViewSet
from user_operation.views import UserFavViewSet, LeavingMessageViewSet, AddressViewSet
from trade.views import ShoppingCartViewSet, OrderViewSet, AlipayView

router = DefaultRouter()
# 配置goods的url
router.register(r'goods', GoodsListViewSet, basename="goods")
# 配置categorys的url
router.register(r'categorys', CategoryViewSet, basename="categorys")
router.register(r'hotsearchs', HotSearchsViewset, basename="hotsearchs")
# 配置codes的url
router.register(r'codes', SmsCodeViewSet, basename="codes")
# 配置users的url
router.register(r'users', UserViewSet, basename="users")
router.register(r'messages', LeavingMessageViewSet, basename="messages")
router.register(r'address', AddressViewSet, basename="address")
router.register(r'shopcarts', ShoppingCartViewSet, basename="shopcarts")
router.register(r'orders', OrderViewSet, basename="orders")
router.register(r'banners', BannerViewSet, basename="banners")
router.register(r'indexgoods', IndexCategoryViewset, basename='indexgoods')

# 收藏
router.register(r'userfavs', UserFavViewSet, basename='userfavs')
schema_view = get_swagger_view(title="api文档")

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'docs/', include_docs_urls(title='暮学生鲜')),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(r'docs/', schema_view),
    url(r'^index/', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^', include(router.urls)),
    # 商品列表页
    # url(r'goods/$', GoodsListViewSet.as_view(), name='goods-list')
    url(r'^alipay/return/', AlipayView.as_view(), name="alipay")
]
