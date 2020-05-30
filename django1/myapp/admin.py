from django.contrib import admin

# Register your models here.
from .models import SinhVien, LopHoc, SinhVienLopHoc


class SinhVienAdmin(admin.ModelAdmin):
    list_display = ('ma_sv','ho_ten','gioi_tinh')
admin.site.register(SinhVien, SinhVienAdmin)
admin.site.register(LopHoc)
admin.site.register(SinhVienLopHoc)

admin.site.site_header = ('Quản lí sinh viên')