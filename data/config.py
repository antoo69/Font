from email.policy import default

from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
ADMINS = env.list("ADMINS", "1506963557, 7342395108")  # adminlar ro'yxati
# IP = env.str("ip")  # Hosting ip manzili
BACKEND_URL = env.str("BACKEND_URL")  # BACKEND_URL manzili
ADMIN_TOKEN = env.str("ADMIN_TOKEN")  # Admin tokeni

CHANNELS = env.list("CHANNELS", "-1002128807252")  # channels
