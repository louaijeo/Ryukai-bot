from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")

user_states = {}

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    msg = update.message.text.strip().lower()

    if user_id not in user_states:
        await update.message.reply_text("hello thats ryukai support bot type inforamtion for information")
        user_states[user_id] = 1
    elif user_states[user_id] == 1:
        await update.message.reply_text("""this all i formation about ryukai scalper :
Introducing the Ryukai Scalper EA – a trading robot designed to help you achieve consistent performance in the market, especially in the gold market!

🔰 What makes Ryukai Scalper EA unique?
✅ Easy to use – No prior experience needed!
✅ Automated 24/7 system – It works without any input from you.
✅ Support for beginners – Suitable for everyone!
✅ Automatic stop – It stops trading once it hits the set profit target.
✅ Works with low balances – Suitable for all account sizes!
You can find more information in the blog spot https://ryukaiinformation.blogspot.com/2025/05/ryukai-scalper.html?m=1
If you want to process payment or want the support just type "support""")
        user_states[user_id] = 2
    else:
        await update.message.reply_text("the support will respond to you as soon as possible thank you for ur patience")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
