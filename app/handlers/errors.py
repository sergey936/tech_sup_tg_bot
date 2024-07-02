from typing import Coroutine

from telegram import Update
from telegram.ext import CallbackContext

from exceptions.base import ApplicationException
from exceptions.chats import BaseWebException


async def error_handler(update: Update, context: CallbackContext) -> Coroutine:
    try:
        raise context.error

    except BaseWebException as error:
        if update and update.effective_message:
            await update.effective_message.reply_text('\n'.join((error.message, error.error_text)))

    except ApplicationException as error:
        if update and update.effective_message:
            await update.effective_message.reply_text(error.message)


