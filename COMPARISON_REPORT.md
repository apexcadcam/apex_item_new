# تقرير مقارنة شاملة - تطبيقات Frappe

## مقارنة بين: frappe_whatsapp, erpnext_telegram_integration, apex_item

---

## 1. الملفات الأساسية في الجذر (Root Level)

### ✅ frappe_whatsapp:
- `setup.py` ✓
- `pyproject.toml` ✓
- `MANIFEST.in` ✓
- `requirements.txt` ✓
- `license.txt` ✓
- `README.md` ✓
- `patches.txt` ✓ (في frappe_whatsapp/)

### ✅ erpnext_telegram_integration:
- `setup.py` ✓
- `MANIFEST.in` ✓
- `requirements.txt` ✓
- `license.txt` ✓
- `README.md` ✓
- `patches.txt` ✓ (في erpnext_telegram_integration/)
- ❌ لا يوجد `pyproject.toml`

### ❌ apex_item (الحالي):
- ❌ لا يوجد `setup.py`
- ✓ `pyproject.toml`
- ❌ لا يوجد `MANIFEST.in`
- ❌ لا يوجد `requirements.txt`
- ❌ لا يوجد `patches.txt`
- ❌ `setup_hook.py` (غير قياسي)
- ❌ `PRD.md` (ملف إضافي)
- ❌ `TEST_PLAN.md` (ملف إضافي)
- ❌ `testsprite_tests/` (مجلد إضافي)

---

## 2. ملفات __init__.py

### ✅ frappe_whatsapp/__init__.py:
```python
__version__ = '1.0.7'
```
**بسيط وقياسي - فقط الإصدار**

### ✅ erpnext_telegram_integration/__init__.py:
```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__version__ = "1.3.0"
```
**بسيط وقياسي - فقط الإصدار**

### ❌ apex_item/__init__.py:
```python
# معقد - يحتوي على:
# 1. setup_hook imports
# 2. pre-loading modules
# 3. sys.path manipulation
```
**غير قياسي - يجب تبسيطه ليكون فقط `__version__`**

---

## 3. ملف hooks.py

### ✅ frappe_whatsapp/hooks.py:
- `after_install` و `before_uninstall` معلقة فقط (commented out)
- لا يوجد install hooks فعلية

### ✅ erpnext_telegram_integration/hooks.py:
- `after_install` و `before_uninstall` معلقة فقط (commented out)
- لا يوجد install hooks فعلية

### ❌ apex_item/hooks.py:
```python
after_install = "apex_item.install.after_install"
after_migrate = ["apex_item.install.after_migrate"]
before_uninstall = "apex_item.install.before_uninstall"
```
**هذا قياسي - ولكن يجب التأكد من أن install.py موجود ويعمل بشكل صحيح**

---

## 4. ملف install.py

### ✅ frappe_whatsapp:
- ❌ لا يوجد `install.py` منفصل
- الـ hooks معلقة فقط في hooks.py

### ✅ erpnext_telegram_integration:
- ❌ لا يوجد `install.py` منفصل
- الـ hooks معلقة فقط في hooks.py

### ✅ apex_item:
- ✓ يوجد `install.py` في `apex_item/install.py`
- ✓ يحتوي على `after_install()`, `after_migrate()`, `before_uninstall()`
- **هذا جيد - ولكن يجب التأكد من أنه لا يحتوي على server management**

---

## 5. ملف MANIFEST.in

### ✅ frappe_whatsapp/MANIFEST.in:
```
include MANIFEST.in
include requirements.txt
include *.json
include *.md
include *.py
include *.txt
recursive-include frappe_whatsapp *.css
recursive-include frappe_whatsapp *.csv
recursive-include frappe_whatsapp *.html
recursive-include frappe_whatsapp *.ico
recursive-include frappe_whatsapp *.js
recursive-include frappe_whatsapp *.json
recursive-include frappe_whatsapp *.md
recursive-include frappe_whatsapp *.png
recursive-include frappe_whatsapp *.py
recursive-include frappe_whatsapp *.svg
recursive-include frappe_whatsapp *.txt
recursive-exclude frappe_whatsapp *.pyc
```

### ✅ erpnext_telegram_integration/MANIFEST.in:
```
include MANIFEST.in
include requirements.txt
include *.json
include *.md
include *.py
include *.txt
recursive-include erpnext_telegram_integration *.css
recursive-include erpnext_telegram_integration *.csv
recursive-include erpnext_telegram_integration *.html
recursive-include erpnext_telegram_integration *.ico
recursive-include erpnext_telegram_integration *.js
recursive-include erpnext_telegram_integration *.json
recursive-include erpnext_telegram_integration *.md
recursive-include erpnext_telegram_integration *.png
recursive-include erpnext_telegram_integration *.py
recursive-include erpnext_telegram_integration *.svg
recursive-include erpnext_telegram_integration *.txt
recursive-exclude erpnext_telegram_integration *.pyc
```

### ❌ apex_item:
- ❌ لا يوجد MANIFEST.in

---

## 6. ملف setup.py

### ✅ frappe_whatsapp/setup.py:
```python
from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

from frappe_whatsapp import __version__ as version

setup(
    name="frappe_whatsapp",
    version=version,
    description="WhatsApp integration for frappe",
    author="Techstation",
    author_email="info@techstation.eg",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
```

### ✅ erpnext_telegram_integration/setup.py:
```python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

from erpnext_telegram_integration import __version__ as version

setup(
	name='erpnext_telegram_integration',
	version=version,
	description='Telegram Integration For Frappe - Erpnext',
	author='Youssef Restom',
	author_email='Youssef@totrox.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
```

### ❌ apex_item:
- ❌ لا يوجد setup.py

---

## 7. ملف patches.txt

### ✅ frappe_whatsapp/patches.txt:
- ملف فارغ ✓

### ✅ erpnext_telegram_integration/patches.txt:
- ملف فارغ ✓

### ❌ apex_item:
- ❌ لا يوجد patches.txt

---

## 8. ملف requirements.txt

### ✅ frappe_whatsapp/requirements.txt:
```
# frappe -- https://github.com/frappe/frappe is installed via 'bench init'
python-magic
```

### ✅ erpnext_telegram_integration/requirements.txt:
```
python-telegram-bot
```

### ❌ apex_item:
- ❌ لا يوجد requirements.txt

---

## 9. البنية الداخلية للمجلدات

### ✅ frappe_whatsapp/frappe_whatsapp/:
- `__init__.py` ✓
- `hooks.py` ✓
- `modules.txt` ✓
- `patches.txt` ✓
- `config/` ✓
- `frappe_whatsapp/` (namespace package) ✓
- `public/` ✓
- `templates/` ✓
- `utils/` ✓

### ✅ erpnext_telegram_integration/erpnext_telegram_integration/:
- `__init__.py` ✓
- `hooks.py` ✓
- `modules.txt` ✓
- `patches.txt` ✓
- `config/` ✓
- `erpnext_telegram_integration/` (namespace package) ✓
- `public/` ✓
- `templates/` ✓

### ❌ apex_item/apex_item/:
- `__init__.py` ✓ (لكن معقد)
- `hooks.py` ✓
- `modules.txt` ✓
- ❌ `patches.txt` غير موجود
- ❌ لا يوجد `config/` (اختياري)
- ❌ `apex_item/apex_item/` (namespace package) موجود لكن غير مستخدم بشكل واضح
- `public/` ✓
- ❌ `install.py` موجود (لكن هذا جيد)

---

## 10. الملفات غير القياسية في apex_item

### ❌ يجب حذفها:
1. `setup_hook.py` - غير موجود في التطبيقات القياسية
2. `PRD.md` - ملف إضافي غير قياسي
3. `TEST_PLAN.md` - ملف إضافي غير قياسي
4. `testsprite_tests/` - مجلد إضافي غير قياسي

### ✅ يجب تبسيطها:
1. `__init__.py` - يجب أن يكون بسيطاً مثل التطبيقات القياسية
2. `hooks.py` - جيد ولكن يجب التأكد من عدم وجود server management code

### ✅ يجب إضافتها:
1. `setup.py` - مطلوب
2. `MANIFEST.in` - مطلوب
3. `patches.txt` - مطلوب
4. `requirements.txt` - مطلوب (حتى لو كان فارغاً)

---

## الخلاصة والتوصيات

### الملفات المطلوبة لـ apex_item (معيار Frappe):
1. ✓ `pyproject.toml` - موجود
2. ❌ `setup.py` - يجب إضافته
3. ❌ `MANIFEST.in` - يجب إضافته
4. ❌ `patches.txt` - يجب إضافته (فارغ)
5. ❌ `requirements.txt` - يجب إضافته
6. ✓ `license.txt` - موجود (افتراضي)
7. ✓ `README.md` - موجود
8. ✓ `hooks.py` - موجود (يحتاج مراجعة)
9. ✓ `install.py` - موجود (يحتاج مراجعة)
10. ❌ `__init__.py` - يحتاج تبسيط

### الملفات التي يجب حذفها:
1. ❌ `setup_hook.py` - غير قياسي
2. ❌ `PRD.md` - ملف إضافي
3. ❌ `TEST_PLAN.md` - ملف إضافي
4. ❌ `testsprite_tests/` - مجلد إضافي

### الكود الذي يجب إزالته من __init__.py:
- كل الكود المتعلق بـ `setup_hook`
- كل الكود المتعلق بـ `pre-loading modules`
- يجب أن يبقى فقط `__version__`

### الكود الذي يجب التأكد من إزالته من install.py:
- أي كود متعلق بـ server management
- أي كود متعلق بـ build process
- أي كود متعلق بـ apps.txt manipulation (يجب أن يتركه bench)


