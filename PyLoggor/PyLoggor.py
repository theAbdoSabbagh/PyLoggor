from typing import Literal, Optional
from datetime import datetime
from rich import print
import os

class FileHandler:
	def __init__(self, fn):
		self.fn = fn
		open(fn, "w") if not os.path.exists(fn) else ...

	def write(self, msg):
		with open(self.fn, "a") as f:
				f.write(f"{msg}\n")


class PyLoggor:
	def __init__(
		self,
		*,
		file_output_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "DEBUG",
		console_output_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "DEBUG",
		topic_beauty_space: int = 15,
		file_beauty_space: int = 15,
		level_beauty_space: int = 10,
		fn=False,
		console_output=True,
		level_colours: dict = {
			"DEBUG": "[bold blue]",
			"INFO": "[bold green]",
			"WARNING": "[bold yellow]",
			"ERROR": "[red]",
			"CRITICAL": "[bold red]"
		},
		delim="|",
		datefmt=r"%d-%b-%y, %H:%M:%S:%f",
		level_symbols = {
			"DEBUG": "D",
			"INFO": "I",
			"WARNING": "W",
			"ERROR": "E",
			"CRITICAL": "C"
		}
	):
		self.file_output_level = file_output_level
		self.console_output_level = console_output_level
		self.topic_beauty_space = topic_beauty_space
		self.file_beauty_space = file_beauty_space
		self.level_beauty_space = level_beauty_space
		self.file = FileHandler(fn) if fn else False
		self.console_output = console_output
		self.level_symbols = level_symbols

		self.level_colours = level_colours
		self.delim = delim
		self.datefmt = datefmt

		self.default_levels = {
			"DEBUG": 0,
			"INFO": 1,
			"WARNING": 2,
			"ERROR": 3,
			"CRITICAL": 4,
		}

	def extras_builder(self, extras):
		h = []
		for key, value in extras.items():
			h.append(f"{key}={value}")
		return f" {self.delim} ".join(h)

	def beautify(self, _str, space):
		return _str.ljust(space)

	def log(self, *,
		level: str = "DEBUG",
		extras: Optional[list] = None,
		topic="None",
		file="NoFile",
		msg="NoMessage", # I don't know why people do this
	):
		level = level.upper()
		time_str = datetime.now().strftime(self.datefmt)

		if extras:
			extras_str = f"{self.delim} {self.extras_builder(extras)}"
		else:
			extras_str = ""

		beautifed_level = self.beautify(level, self.level_beauty_space)
		beautifed_topic = self.beautify(topic, self.topic_beauty_space)
		beautifed_file = self.beautify(file, self.file_beauty_space)

		if level in self.level_symbols.keys():
			level_symbol = self.level_symbols[level]
		else:
			level_symbol = "*"

		msg = f"[{level_symbol}] {time_str} {self.delim} {beautifed_level} {self.delim} {beautifed_file} {self.delim} {beautifed_topic} {self.delim} {msg}{extras_str}"

		if level in self.level_colours.keys():
			level_colour = self.level_colours[level]
		else:
			level_colour = "[bold white]"

		if self.file:
			if level not in self.default_levels.keys() or self.default_levels[level] >= self.default_levels[self.file_output_level]:
				self.file.write(msg)
		if self.console_output:
			if level not in self.default_levels.keys() or self.default_levels[level] >= self.default_levels[self.console_output_level]:
				print(f"{level_colour}{msg}[/]")
