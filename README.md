# 📦 Odoo 18 開發環境專案

本專案為一個基於 **Odoo 18** 的開發環境，支援模組擴充與 Docker 容器化部署，適合用於學習與開發企業應用系統。

---

## 📁 專案結構

| 路徑 / 檔案          | 說明                          |
| -------------------- | ----------------------------- |
| `.gitignore`         | 指定 Git 應忽略的檔案與資料夾 |
| `odoo.conf`          | Odoo 設定檔，含 DB 與服務參數 |
| `docker-compose.yml` | Docker 容器設定與服務定義     |
| `addons/`            | 自訂開發的模組存放資料夾      |
| `odoo/`              | Odoo 官方原始碼（請自行下載） |

---

## 🚀 安裝步驟

1. **克隆專案**
   ```bash
   git clone https://your.repo.url/odoo18-dev.git
   cd odoo18-dev
   ```

2. **下載 Odoo 原始碼**
   > 從 [Odoo GitHub](https://github.com/odoo/odoo) 下載對應版本並放入 `odoo/` 資料夾中。

3. **啟動容器**
   ```bash
   docker-compose up -d
   ```

4. **開啟 Odoo**
   - 在瀏覽器輸入網址 [http://localhost:8069](http://localhost:8069)

---

## 🛠️ 常用指令

```bash
# 啟動專案
docker-compose up -d

# 停止專案
docker-compose down

# 查看 log
docker-compose logs -f odoo

# 查看運行中的容器
docker ps

# 重啟服務
docker-compose restart odoo
```

---

## 🧩 新增自訂模組教學

### 1️⃣ 建立模組資料夾

在 `addons/` 底下建立你的模組資料夾，例如 `my_custom_module/`，資料夾結構如下：

```
my_custom_module/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── my_model.py
├── views/
│   └── my_model_views.xml
```

### 2️⃣ 撰寫模組內容

#### `__manifest__.py`
```python
{
    'name': 'My Custom Module',
    'version': '1.0',
    'summary': '一個簡單的自訂模組',
    'author': 'Your Name',
    'depends': ['base'],
    'data': ['views/my_model_views.xml'],
    'installable': True,
    'application': True,
}
```

#### `models/my_model.py`
```python
from odoo import models, fields

class MyModel(models.Model):
    _name = 'my.model'
    _description = 'My Custom Model'

    name = fields.Char(string='名稱')
    active = fields.Boolean(string='啟用', default=True)
```

#### `views/my_model_views.xml`
```xml
<odoo>
    <record id="view_my_model_form" model="ir.ui.view">
        <field name="name">my.model.form</field>
        <field name="model">my.model</field>
        <field name="arch" type="xml">
            <form string="My Model">
                <sheet>
                    <group>
                        <field name="name"/>
                        <field name="active"/>
                    </group>
                </sheet>
            </form>
        </field>
    </record>

    <record id="view_my_model_tree" model="ir.ui.view">
        <field name="name">my.model.tree</field>
        <field name="model">my.model</field>
        <field name="arch" type="xml">
            <tree string="My Model">
                <field name="name"/>
                <field name="active"/>
            </tree>
        </field>
    </record>

    <menuitem id="my_model_root_menu" name="My Module"/>
    <menuitem id="my_model_menu" name="My Models" parent="my_model_root_menu"/>
    <act_window id="action_my_model"
                name="My Models"
                res_model="my.model"
                view_mode="tree,form"
                menu_id="my_model_menu"/>
</odoo>
```

---

### 3️⃣ 設定 `addons_path`（若尚未設定）

編輯 `odoo.conf` 增加以下設定，確保自訂模組可以被載入：

```ini
addons_path = /odoo/addons,/addons
```

---

### 4️⃣ 安裝模組

1. 重新啟動服務：`docker-compose restart`
2. 登入 Odoo，進入「應用程式」頁面，啟用開發模式
3. 搜尋你建立的模組並點擊「安裝」

---

### 5️⃣ 修改後升級模組

若修改 models 或欄位結構，請透過下列指令升級模組：

```bash
docker-compose exec odoo odoo -u my_custom_module -d odoo_db
```

---

### 🧪 資料表確認（PostgreSQL）

可進入資料庫檢查資料表是否成功建立：

```bash
docker-compose exec db psql -U odoo -d odoo_db
\dt
```

---

## 📚 延伸閱讀

- [Odoo 官方開發者文件](https://www.odoo.com/documentation/18.0/developer.html)
- [Odoo GitHub 原始碼](https://github.com/odoo/odoo)

---