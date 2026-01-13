from loguru import logger
import sys

logger.remove()
logger.add(
    sys.stdout,
    level="DEBUG",
    format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <7}</level> |id={extra[request_id]}| <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    backtrace=True,
    diagnose=True,
    enqueue=True,
    serialize=True,
)
