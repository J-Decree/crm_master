from django.db import models
from django.conf import settings
import importlib
from general_admin.acquirer.modelAdmin import ModelAdmin


# 职责：获得所有注册的类，放在一个列表里
class Site(object):
    def __init__(self):
        self.app_to_admin = {}
        # {'account':[modelAdmin1,modelAdmin2,]}

    def register(self, cls_info, model_admin=ModelAdmin):
        if not issubclass(cls_info, models.Model):
            raise TypeError('not a subclass to models.Model')
        m = model_admin()
        setattr(m, 'ClsInfo', cls_info)
        app_name = cls_info._meta.app_label
        self.app_to_admin.setdefault(app_name, [])
        self.app_to_admin[app_name].append(m)

    def get_total_cls(self):
        ret = {}
        for app_name in self.app_to_admin:
            ret[app_name] = self.get_cls_list(app_name)
        return ret

    def get_cls_list(self, app_name):
        admin_list = self.app_to_admin[app_name]
        l = [admin.cls_detail for admin in admin_list]
        return l

    def get_model_list(self, app_name):
        admin_list = self.app_to_admin.get(app_name)
        ret = []
        for admin in admin_list:
            if not hasattr(admin, 'ClsInfo'): continue
            cls_info = getattr(admin, 'ClsInfo')
            ret.append(cls_info)
        return ret

    def get_model(self, app_name, cls_name):
        admin_list = self.app_to_admin.get(app_name, [])
        for admin in admin_list:
            if not hasattr(admin, 'ClsInfo'): continue
            cls_info = getattr(admin, 'ClsInfo')
            if cls_info.__name__ == cls_name:
                return cls_info

    def get_admin(self, app_name, cls_name):
        admin_list = self.app_to_admin.get(app_name, [])
        for admin in admin_list:
            if not hasattr(admin, 'ClsInfo'): continue
            cls_info = getattr(admin, 'ClsInfo')
            if cls_info.__name__ == cls_name:
                return admin

    @staticmethod
    def import_admin():
        for app in settings.INSTALLED_APPS:
            if not app.startswith('django.contrib.'):
                try:
                    importlib.import_module(app + '.myAdmin')
                except Exception as e:
                    print(e)

    def is_app_in_register(self, app):
        return True if app in self.app_to_admin else False

    def is_cls_in_register(self, app_name, cls_name):
        return True if self.get_model(app_name, cls_name) else False
