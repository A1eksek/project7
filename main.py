# class Documents(object):
#     def show(self):
#         raise NotImplementedError()
# class ODFDocument(Documents):
#     def show(self):
#         print('ODF format')
# class MSOfficeDocumnet(Documents):
#     def show(self):
#         print('MS Office format')
# class Application(object):
#     def create_document(self, type_):
#         raise NotImplementedError()
#
# class MyApplication(Application):
#     def create_document(self, type_):
#         if type_ == 'odf':
#             return ODFDocument()
#         elif type_ == 'doc':
#             return MSOfficeDocumnet()
#         else:
#             return Documents()
#
# app = MyApplication()
# app.create_document('odf').show()
# app.create_document('doc').show()
#
# try:
#     app.create_document('pdf').show()
# except:
#     print('NotImplementedError')

import copy

# class Prototype(object):
#     def __init__(self):
#         self._objects = {}
#     def register(self,name,obj):
#         self._objects[name] = obj
#     def unregister(self, name):
#         del self._objects[name]
#     def clone(self, name, attrs):
#         obj = copy.deepcopy(self._objects[name])
#         obj.__dict__.update(attrs)
#         return obj
# class Bird(object):
#     def __init__(self, name=None):
#         self.name = name
#
# prototype = Prototype()
# prototype.register('Птица', Bird())
#
# owl = prototype.clone('Птица', {'name': 'Owl'})
# print(type(owl), owl.name)
# duck = prototype.clone('Птица', {'name': 'Duck'})
# print(type(duck), duck.name)


# import copy
#
# class Prototype(object):
#     def __init__(self):
#         self._objects = {}
#
#     def register(self, name, obj):
#         self._objects[name] = obj
#
#     def unregister(self, name):
#         del self._objects[name]
#
#     def clone(self, name, attrs):
#         obj = copy.deepcopy(self._objects[name])
#         obj.__dict__.update(attrs)
#         return obj
#
# class Bird(object):
#     def __init__(self, name=None):
#         self.name = name
#
# prototype = Prototype()
# prototype.register('Птица', Bird())  # Регистрируем 'Птица'
#
# # Клонируем объекты с правильным именем
# owl = prototype.clone('Птица', {'name': 'Owl'})
# print(type(owl), owl.name)
#
# duck = prototype.clone('Птица', {'name': 'Duck'})
# print(type(duck), duck.name)

import copy
from typing import Dict, Any


class Prototype:
    def __init__(self) -> None:
        self._objects: Dict[str, Any] = {}

    def register(self, name: str, obj: Any) -> None:
        self._objects[name] = obj

    def unregister(self, name: str) -> None:
        del self._objects[name]

    def clone(self, name: str, attrs: Dict[str, Any]) -> Any:
        obj = copy.deepcopy(self._objects[name])
        obj.__dict__.update(attrs)
        return obj


class Bird:
    """Птица"""

    def __init__(self, name: str = "") -> None:
        self.name = name

    # Создаем экземпляр прототипа


prototype = Prototype()
prototype.register('bird', Bird())

# Клонируем и изменяем атрибуты для совы
owl = prototype.clone('bird', {'name': 'Owl'})
print(type(owl), owl.name)  # <class '_main_.Bird'> Owl

# Клонируем и изменяем атрибуты для утки
duck = prototype.clone('bird', {'name': 'Duck'})
print(type(duck), duck.name)  # <class '_main_.Bird'> Duck

