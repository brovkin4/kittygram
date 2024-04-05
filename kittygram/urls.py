from django.urls import include, path
from rest_framework.routers import SimpleRouter

# from cats.views import cat_list
# from cats.views import APICat
# from cats.views import CatList, CatDetail
from cats.views import CatViewSet

# Функции
'''urlpatterns = [
   path('cats/', cat_list),
]'''

# Низкоуровневые view-классы
'''urlpatterns = [
   path('cats/', APICat.as_view()),
]'''

# Высокоуровневые классы
'''urlpatterns = [
   path('cats/', CatList.as_view()),
   path('cats/<int:pk>/', CatDetail.as_view()),
]'''

# ViewSets
router = SimpleRouter()
router.register('cats', CatViewSet)
urlpatterns = [
   path('', include(router.urls)),
]
