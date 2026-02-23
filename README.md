# ToDoGemini 🚀

ToDoGemini, kullanıcıların günlük görevlerini yönetebildiği ve Google Gemini yapay zeka modelini kullanarak kısa görev girdileri için otomatik olarak detaylı ve kapsamlı açıklamalar oluşturabildiği, FastAPI tabanlı modern bir web uygulamasıdır.

🔗 **Canlı Demo:** [ToDoGemini'yi Dene](https://todogemini-7cva.onrender.com/auth/login-page)

## 🌟 Özellikler

* **Yapay Zeka Destekli Açıklamalar:** LangChain ve Google Gemini entegrasyonu sayesinde, eklenen kısa bir "to-do" maddesi için yapay zeka tarafından uzun ve eyleme geçirilebilir açıklamalar üretilir.
* **Kullanıcı Kimlik Doğrulama:** JWT (JSON Web Token) ve Bcrypt kullanılarak güvenli kullanıcı kaydı ve giriş sistemi (Login/Register).
* **Tam CRUD İşlemleri:** Görevleri oluşturma, okuma, güncelleme ve silme işlemleri.
* **Modern ve Duyarlı Arayüz:** Jinja2 template motoru ve Bootstrap kullanılarak tasarlanmış, mobil uyumlu temiz kullanıcı arayüzü.
* **Veritabanı Yönetimi:** SQLAlchemy ORM ve yapısal veritabanı güncellemeleri için Alembic migration desteği.

## 🛠️ Kullanılan Teknolojiler

* **Backend:** Python, FastAPI
* **Veritabanı & ORM:** SQLite, SQLAlchemy
* **Migration:** Alembic
* **Yapay Zeka Entegrasyonu:** LangChain, Google Gemini API (`gemini-2.5-flash`)
* **Güvenlik:** passlib (Bcrypt), python-jose (JWT)
* **Frontend:** HTML, CSS, Jinja2 Templates, Bootstrap
* **Deployment:** Render

## 📋 API Uç Noktaları (Endpoints)

Uygulama temel olarak iki ana router üzerinden çalışmaktadır:

**Authentication (`/auth`)**
* `GET /auth/login-page` - Giriş sayfasını render eder.
* `GET /auth/register-page` - Kayıt sayfasını render eder.
* `POST /auth/` - Yeni kullanıcı oluşturur.
* `POST /auth/token` - Access token almak için giriş işlemi.

**Todo (`/todo`)**
* `GET /todo/todo-page` - Ana görevler sayfasını render eder.
* `GET /todo/add-todo-page` - Yeni görev ekleme sayfasını render eder.
* `GET /todo/edit-todo-page/{todo_id}` - Görev düzenleme sayfasını render eder.
* `GET /todo/` - Kullanıcının tüm görevlerini getirir.
* `POST /todo/todo` - Yeni görev oluşturur (Gemini AI entegrasyonu burada çalışır).
* `GET /todo/todo/{todo_id}` - Belirli bir görevi getirir.
* `PUT /todo/todo/{todo_id}` - Görevi günceller.
* `DELETE /todo/todo/{todo_id}` - Görevi siler.
