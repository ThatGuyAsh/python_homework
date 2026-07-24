# Task 1
import logging

# One-time logger setup
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        # Log function name
        logger.info(f"function: {func.__name__}")

        # Log positional parameters
        if args:
            logger.info(f"positional parameters: {args}")
        else:
            logger.info("positional parameters: none")

        # Log keyword parameters
        if kwargs:
            logger.info(f"keyword parameters: {kwargs}")
        else:
            logger.info("keyword parameters: none")

        # Call the original function
        result = func(*args, **kwargs)

        # Log return value
        logger.info(f"return: {result}")

        return result

    return wrapper


@logger_decorator
def hello_world():
    print("Hello, World!")


@logger_decorator
def positional_function(*args):
    return True


@logger_decorator
def keyword_function(**kwargs):
    return logger_decorator


# Main program
hello_world()
positional_function(1, 2, 3, "Python")
keyword_function(name="Ashton", age=40)