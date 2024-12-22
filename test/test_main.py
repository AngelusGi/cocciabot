import logging

import pytest
from telegram import Chat, Update, User
from telegram.ext import ContextTypes

from main import caps, help, init_logger, log_session, start


@pytest.fixture
def update():
    user = User(id=123, first_name="TestUser", is_bot=False)
    chat = Chat(id=456, type="private")
    message = type('obj', (object,), {'text': '/start', 'chat': chat, 'from_user': user})
    return Update(update_id=1, message=message)

@pytest.fixture
def context():
    return ContextTypes.DEFAULT_TYPE()

def test_init_logger():
    logger = init_logger()
    assert isinstance(logger, logging.Logger)

def test_log_session(update):
    logger = init_logger()
    response_message = "Test response"
    log_session(update, response_message)
    assert logger.name == "__main__"

@pytest.mark.asyncio
async def test_start(update, context):
    await start(update, context)
    assert update.message.text == "/start"

@pytest.mark.asyncio
async def test_help(update, context):
    await help(update, context)
    assert update.message.text == "/help"

@pytest.mark.asyncio
async def test_caps(update, context):
    context.args = ["test", "message"]
    await caps(update, context)
    assert update.message.text == "/caps test message"