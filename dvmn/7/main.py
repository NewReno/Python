import os
from dotenv import load_dotenv
from pytimeparse import parse
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext


def load_config():
    load_dotenv()
    return {
        "tg_token": os.getenv("TG_TOKEN"),
    }


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}".format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def notify(chat_id, message_id, context):
    context.bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="Время вышло!")


def update_countdown(context: CallbackContext):
    job = context.job
    chat_id = job.context["chat_id"]
    message_id = job.context["message_id"]
    remaining_time = job.context["remaining_time"]
    total_seconds = job.context["total_seconds"]
    if remaining_time > 0:
        elapsed_time = total_seconds - remaining_time
        progress_bar = render_progressbar(
            total=total_seconds,
            iteration=elapsed_time,
            prefix="Прогресс:",
            suffix="",
            length=30,
            fill='█',
            zfill='░'
        )
        context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=f"Осталось {remaining_time} секунд...\n{progress_bar}"
        )
        job.context["remaining_time"] -= 1
    else:
        notify(chat_id, message_id, context)
        job.schedule_removal()


def reply(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    message = update.message.text
    total_seconds = parse(message)
    if total_seconds:
        progress_bar = render_progressbar(
            total=total_seconds,
            iteration=0,
            prefix="Прогресс:",
            suffix="",
            length=30,
            fill='█',
            zfill='░'
        )
        message = context.bot.send_message(chat_id, f"Запущен таймер на {total_seconds} секунд...\n{progress_bar}")
        message_id = message.message_id
        context.job_queue.run_repeating(
            update_countdown,
            interval=1,
            first=1,
            context={
                "chat_id": chat_id,
                "message_id": message_id,
                "remaining_time": total_seconds,
                "total_seconds": total_seconds
            }
        )


def main():
    config = load_config()
    tg_token = config["tg_token"]
    updater = Updater(tg_token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
