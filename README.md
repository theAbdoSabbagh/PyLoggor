Hey! I made this 100 line piece of code to simplify logging while keeping it versatile enough to suit my needs project-to-project.
You can install this as a package: `pip install *.whl` and use it anywhere in your by `from PyLoggor import PyLoggor`!

### Config
PyLoggor aims to be very incredibly configurable, hence I've made the following possible config you can pass into the PyLoggor class.

file_output_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "DEBUG",
console_output_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "DEBUG",
topic_beauty_space: int = 30,
file_beauty_space: int = 30,
extras: list = [],
fn=False,
console_output=True,
level_colours: dict = {
    "DEBUG": "[bold blue]",
    "INFO": "[bold green]",
    "WARNING": "[bold yellow]",
    "ERROR": "[bold red]",
    "CRITICAL": "[bold red]"
}
