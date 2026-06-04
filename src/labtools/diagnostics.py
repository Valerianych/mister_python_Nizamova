import logging
import warnings

logger = logging.getLogger("labtools")


def old_sum(a, b):
    warnings.warn("old_sum is deprecated", DeprecationWarning)
    return a + b


def process_item(item_id):
    logger.info("item processed: %s", item_id)
    return True
