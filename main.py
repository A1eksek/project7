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

# import copy
# from typing import Dict, Any
#
#
# class Prototype:
#     def __init__(self) -> None:
#         self._objects: Dict[str, Any] = {}
#
#     def register(self, name: str, obj: Any) -> None:
#         self._objects[name] = obj
#
#     def unregister(self, name: str) -> None:
#         del self._objects[name]
#
#     def clone(self, name: str, attrs: Dict[str, Any]) -> Any:
#         obj = copy.deepcopy(self._objects[name])
#         obj.__dict__.update(attrs)
#         return obj
#
#
# class Bird:
#     """Птица"""
#
#     def __init__(self, name: str = "") -> None:
#         self.name = name
#
#     # Создаем экземпляр прототипа
#
#
# prototype = Prototype()
# prototype.register('bird', Bird())
#
# # Клонируем и изменяем атрибуты для совы
# owl = prototype.clone('bird', {'name': 'Owl'})
# print(type(owl), owl.name)  # <class '_main_.Bird'> Owl
#
# # Клонируем и изменяем атрибуты для утки
# duck = prototype.clone('bird', {'name': 'Duck'})
# print(type(duck), duck.name)  # <class '_main_.Bird'> Duck

# class WindowBase(object):
#     def show(self):
#         raise NotImplementedError()
#     def hide(self):
#         raise NotImplementedError
# class MainWindows(WindowBase):
#     def show(self):
#         print('Показать MainWindow')
#     def hide(self):
#         print('Спрятать MainWindow')
# class SettingWindows(WindowBase):
#     def show(self):
#         print('Show SettingWindow')
#     def hide(self):
#         print('Спрятать SettingWindow')
# class HelpWindows(WindowBase):
#     def show(self):
#         print('Show HelpWindow')
#     def hide(self):
#         print('Спрятать HelpWindow')
#
# class WindowMediator(object):
#     def __init__(self):
#         self.windows = dict.fromkeys(['main', 'setting', 'help'])
#     def show(self, win):
#         for window in self.windows.values():
#             if not window is win:
#                 window.hide()
# from typing import Dict, Optional
#
# class WindowBase:
#     def show(self) -> None:
#         raise NotImplementedError()
#
#     def hide(self) -> None:
#         raise NotImplementedError()
#
#
# class MainWindow(WindowBase):
#     def show(self) -> None:
#         print('Show MainWindow')
#
#     def hide(self) -> None:
#         print('Hide MainWindow')
#
#
# class SettingWindow(WindowBase):
#     def show(self) -> None:
#         print('Show SettingWindow')
#
#     def hide(self) -> None:
#         print('Hide SettingWindow')
#
#
# class HelpWindow(WindowBase):
#     def show(self) -> None:
#         print('Show HelpWindow')
#
#     def hide(self) -> None:
#         print('Hide HelpWindow')
#
#
# class WindowMediator:
#     def __init__(self) -> None:
#         self.windows: Dict[str, Optional[WindowBase]] = {
#             'main': None,
#             'setting': None,
#             'help': None
#         }
#
#     def show(self, win: WindowBase) -> None:
#         for window in self.windows.values():
#             if window is not None and window is not win:
#                 window.hide()
#         win.show()
#
#     def set_main(self, win: MainWindow) -> None:
#         self.windows['main'] = win
#
#     def set_setting(self, win: SettingWindow) -> None:
#         self.windows['setting'] = win
#
#     def set_help(self, win: HelpWindow) -> None:
#         self.windows['help'] = win
#
#
# # Создаем окна
# main_win = MainWindow()
# setting_win = SettingWindow()
# help_win = HelpWindow()
#
# # Создаем медиатор и устанавливаем окна
# med = WindowMediator()
# med.set_main(main_win)
# med.set_setting(setting_win)
# med.set_help(help_win)
#
# # Показать главное окно
# main_win.show()  # Show MainWindow
#
# # Показать окно настроек
# med.show(setting_win)
# # Hide MainWindow
# # Show SettingWindow
#
# # Показать окно помощи
# med.show(help_win)
# # Hide MainWindow
# # Hide SettingWindow
# # Show HelpWindow

