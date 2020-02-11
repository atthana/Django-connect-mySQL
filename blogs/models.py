from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/3.0/ref/models/fields/  ดูชนิดข้อมูลต่างๆได้ที่นี่
class Post(models.Model):  # สร้าง table ขึ้นมาชื่อว่า Post มี 2 คอลัมน์ คือ name -> datatype = ตัวอักษร+ข้อความความยาว200 , desc เป้น textField
	name = models.CharField(max_length=200)  # กำหนดความยาวไว้ 200 ตัวอักษร  จิงๆ 2 อันนี้คือ Field หรือ Column นะ
	desc = models.TextField()  # อันนี้ไม่กำหนดความยาวนะ
