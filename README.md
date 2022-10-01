The easiest and perhaps the most versatile logger for python, in hundred lines.

## Table of Contents
- [Installation](#Installation)
- [Usage](#Usage)
- [Config](#Config)
- [Appendix](#Appendix)
- [About the Author](#About-the-author)

### Installation
---
As simple as `pip install PyLoggor`!

### Usage
---
1) Once installed, you can access the logger class by importing it like so: `from PyLoggor import PyLoggor`
2) Instantize the class using: `myLogger = PyLoggor()`
3) Log something! `myLogger.log(level="ERROR", msg="JSON config is corrupt.")`

### Config
---
<details>
	<summary> Standard </summary>

1. Standard Format.
	This currently does not support customizing the base format, however you CAN pass in extra variables per log, which gets added at the end of the standard format string.
	- Standard Format: `[P] DATE_TIME LEVEL FILE TOPIC MSG EXTRAS`

2. Level.
	- The default level hierarchy is: `DEBUG` -> `INFO` -> `WARNING` -> `ERROR` -> `CRITICAL`.
		- This means that if the level is `WARNING`, it will log all WARNINGs, ERRORs, and CRITICALs but not DEBUG and INFO messages.
	- You can pass in a custom level as well, which will not effect the level hierarchy and always print as well as log to file.
</details>
<details>
	<summary> Initialization </summary>

1) `file_output_level`, `console_output_level`:
	Different levels for file and console output!
	- `PyLoggor(file_output_level="DEBUG", console_output_level="ERROR")`
	- This will write ALL logs to file but only print ERRORs and CRITICALs to the console.
	- Both default to `DEBUG`.

2) `fn`:
	The file it will output to, leave empty if it should not output to file.
	- Pass in the file name, or the literal file location- it will create the file if it doens't exist.
	- Defaults to None.

3) `console_output`:
	Set this to `False` if you do not want it to print logs to the console. Defaults to `True`.
	
4) `topic_beauty_space`, `file_beauty_space`, `level_beauty_space`:
	- The loggor automatically adds whitespace to the end of topics, file names and levels (passed during logging) to make the output appear more... beautiful, as seen below

5) `level_colours`:
	Defines the colour the log message is printed in.
	- Pass in a dict structure like so:
		```json
		{
			"DEBUG": "[bold blue]",
			"INFO": "[bold green]",
			"WARNING": "[bold yellow]",
			"ERROR": "[bold red]",
			"CRITICAL": "[bold red]"
		}
		```
	- Colour names should be [rich]("https://github.com/Textualize/rich") compliant.
	- If no colour is set, it defaults to above mentioned, and if custom level is used, defaults to ``[bold white]``

6) `level_symbols`:
	Each log level has a level system at the start of the log entry.
	- Pass in a dict structure like so:
		```json
		{
			"DEBUG": "D",
			"INFO": "I",
			"WARNING": "W",
			"ERROR": "E",
			"CRITICAL": "C"
		}
		```
	- Defaults to above mentioned and to `*` for all else
	- This will get printed as `[D]` at the start of all log entries.
	- Check below for a visual example.

7) `delim`:
	Each field is separated by this deliminator, defaults to `|` (it gets wrapped with a space on each side).
	
8) `datefmt`:
	The datetime format in which the output is logged, defaults to `"%d-%b-%y, %H:%M:%S:%f"`
	It appears something like this: `01-Oct-22, 10:35:21:300273`

</details>
<details>
	<summary> Usage </summary>

```python
from PyLoggor import PyLoggor

logger = PyLoggor(fn="log.txt")

logger.log(level="debug", msg="DEBUG", topic="Internal", file="utils/internal.py")
logger.log(level="info", msg="This is an info message", topic="Info", file="info.py")
logger.log(level="warning", msg="Something is not right here.", topic="Listener", file="modules/listener.py")
logger.log(level="error", msg="I caught an error.", topic="Error Handling", file="eh.py")
logger.log(level="critical", msg="Unhandled exception.", topic="MAIN", file="main.py")
logger.log(level="custom", msg="This is custom", topic="customized", file="test/custom.py")
```
</details>

![output](Assets/output.png)

### Appendix
---
**Find this incomplete?** Create an [issue](https://github.com/PrivatePandaCO/PyLoggor/issues)!


### About the author
---
Just check mi [main profile](https://github.com/ThePrivatePanda) and my site ye, leave a star if ye liked this!