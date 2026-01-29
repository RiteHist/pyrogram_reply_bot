import os
from dotenv import load_dotenv
from pyrogram import Client
from pyrogram.filters import user
import sentry_sdk

load_dotenv()

if os.getenv("SENTRY_DSN"):
    sentry_sdk.init(
        dsn=os.getenv("SENTRY_DSN"),
        release="v1.0",
        keep_alive=True,
        send_default_pii=True
    )

if not os.path.exists('me.session'):
    api_id = int(os.getenv("API_ID"))
    api_hash = os.getenv('API_HASH')
    phone = os.getenv('PHONE')

    app = Client('me', api_id=api_id, api_hash=api_hash, phone_number=phone)
else:
    app = Client('me')


@app.on_message(filters=user('MultiFactorBot'))
async def handle_bot(client, message):
    await message.click('Yes')

app.run()
