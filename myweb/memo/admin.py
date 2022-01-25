from django.contrib import admin
from memo.models import Memo

class MemoAdmin(admin.ModelAdmin):
    #관리자 사이트에서 처리할 필드
    list_display = ('writer', 'memo')
    
admin.site.register(Memo, MemoAdmin)
