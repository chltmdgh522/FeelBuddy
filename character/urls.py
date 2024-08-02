from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'character'
urlpatterns = [

    # 캐릭터 생성 관련 페이지

    path('character/list', character_list, name='character_list'), # 생성한 캐릭터 리스트 페이지

    path('character/create', character_create, name='character_create'), # 캐릭터 5개 있는 페이지 선택

    # 캐릭터 하나를 선택하고 들어온 그 text 페이지 여기서는 선택이유 쓰면 됨  결국 이 텍스트는 introudce에 저장 추가로 캐릭터 이름도 적어야됨
    path('character/create/<int:pk>', character_create_detail, name='character_create_detail'),

    path('character/update/<int:pk>', character_update, name='character_update'), # 캐릭터 이름만 수정                   {{ 차이 }} --> 캐릭터의 이름은 감정 그 자체로 해서 변화시킬 수 없는것으로 구상한것이었음 

    path('trash/delete/<int:pk>', trash_delete, name='trash_delete'), # 이거는 캐릭터 삭제버튼 url 즉 휴지통으로  이동 post 만 접속가능하게 해야됨

    path('trash', trash, name='trash'),  # 여기는 삭제된 캐릭터의 휴지통 페이지

    path('trash/restore/<int:pk>', trash_restore, name='trash_restore'),  # 여기는 휴지통에서 캐릭터 선택하면 복구하는 페이지 만약 복구했는데 캐릭터 5개이면 복구못하게

    path('trash/perfect/delete/<int:pk>', trash_perfect_delete, name='trash_perfect_delete'),  # 이거는 캐릭터 영구 삭제 url 즉 휴지통에서만 작동할수 있는 url임

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)