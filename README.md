
#  Kutubxona Boshqaruv Tizimi

Bu loyiha — kutubxona ishlarini boshqarishga mo‘ljallangan konsol interfeysli (CLI) dastur bo‘lib, foydalanuvchilarni ro'yxatdan o'tkazish, kitoblar va mualliflarni qo'shish, mavjud kitoblar bilan ishlash imkonini beradi.

---

##  Texnologiyalar

- Python 3.10+
- PostgreSQL
- `psycopg2` (PostgreSQL uchun Python adapteri)
- `.env` fayl orqali konfiguratsiya
- Fayl strukturalangan, modulli loyiha

---

##  Loyihaning struktura tavsifi

```bash
pscopg_kutubxona_project/
│
├── core/                  # Konfiguratsiya va asosiy baza fayllari
│   ├── config.py          # .env faylni yuklash
│   ├── database_settings.py  # DB ulanishi va query bajarish
│   ├── table_queries.py   # Jadval yaratish query-lari
│   └── .env               # Maxfiy ma'lumotlar (.gitignore ichida bo'lishi kerak)
│
├── users/                 # Foydalanuvchi bilan bog'liq funksiyalar
│   └── views.py
│
├── utils/                 # CRUD operatsiyalar
│   └── crud.py
│
├── main.py                # Dastur ishga tushadigan asosiy fayl
├── requirements.txt       # Kutubxonalar ro‘yxati
└── README.md              # Loyiha haqida ma’lumot
# Ornatish
git clone https://github.com/username/pscopg_kutubxona_project.git
cd pscopg_kutubxona_project
Virtual environment yarating va faollashtiring:
python -m venv venv
venv\Scripts\activate  # Windows
# Kerakli kutubxonalarni o‘rnating:
Kerakli kutubxonalarni o‘rnating:
pip install -r requirements.txt

