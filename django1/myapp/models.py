from django.db import models

# Create your models here.
class SinhVien(models.Model):
    ma_sv = models.CharField(unique=True, max_length = 200, verbose_name = ' Mã Sinh Viên')
    ho_ten = models.CharField(max_length = 200, default='')
    gioi_tinh = models.BooleanField(default = False)
    ngay_sinh = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.ho_ten

    #sửa sang tiếng việt cho admin
    class Meta:
        verbose_name = 'Sinh viên'
        verbose_name_plural = 'Sinh viên'


class LopHoc(models.Model):
    ma_lop = models.CharField(unique = True, max_length = 200)
    ten_lop = models.CharField(max_length = 200, blank = True, null =True)


class SinhVienLopHoc(models.Model):
    #CASCADE xoa khi xao lop
    sinh_vien = models.ForeignKey(SinhVien, on_delete= models.CASCADE)
    lop_hoc = models.ForeignKey(LopHoc, on_delete = models.CASCADE)


