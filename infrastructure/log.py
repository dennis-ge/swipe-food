from infrastructure.config import CrawlerConfig, ApiConfig
import logging.config

import structlog


class Logger:

    @classmethod
    def create(cls, name: str, **kwargs):
        return structlog.getLogger(name=name, **kwargs)

    @classmethod
    def load_config(cls, config: CrawlerConfig or ApiConfig):
        logging.config.dictConfig({
            "version": 1,
            "disable_existing_loggers": True,
            "formatters": {
                "simpleFormatter": {
                    "()": structlog.stdlib.ProcessorFormatter,
                    "processor": structlog.dev.ConsoleRenderer(colors=False),
                },
                "jsonFormatter": {
                    "()": structlog.stdlib.ProcessorFormatter,
                    "processor": structlog.processors.JSONRenderer(),
                },
            },
            "handlers": {
                "consoleHandler": {
                    "level": config.log_level_console,
                    "class": "logging.StreamHandler",
                    "formatter": "simpleFormatter",
                },
                "fileHandler": {
                    "level": config.log_level_file,
                    "class": "logging.handlers.TimedRotatingFileHandler",
                    "formatter": "jsonFormatter",
                    "filename": config.log_file_name,
                    "when": "midnight",
                    "interval": 10,
                    "backupCount": 7
                },
            },
            "loggers": {
                "": {
                    "handlers": ["consoleHandler", "fileHandler"],
                    "level": "DEBUG",
                },
            }
        })

        structlog.configure(
            processors=[
                structlog.stdlib.add_log_level,
                structlog.stdlib.PositionalArgumentsFormatter(),
                structlog.processors.TimeStamper(fmt="iso"),
                structlog.processors.StackInfoRenderer(),
                structlog.processors.format_exc_info,
                structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
            ],
            context_class=dict,
            logger_factory=structlog.stdlib.LoggerFactory(),
            cache_logger_on_first_use=True, 
        )
