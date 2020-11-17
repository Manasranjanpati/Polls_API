from django.urls import path
from .views import polls_list, polls_detail

# DRF
from .apiview import PollList, PollDetail, ChoiceList, CreateVote, PollViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')


urlpatterns = [
    path("polls/", polls_list, name="polls_list"),
    path("polls/<int:pk>/", polls_detail, name="polls_detail"),

    # DRF
    path("api/polls/", PollList.as_view(), name="polls_list"),
    path("api/polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    # path("choices/", ChoiceList.as_view(), name="choice_list"),
    # path("vote/", CreateVote.as_view(), name="create_vote"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),


]

urlpatterns += router.urls
