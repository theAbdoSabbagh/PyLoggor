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
	):
		self.file_output_level = file_output_level
		self.console_output_level = console_output_level
		self.topic_beauty_space = topic_beauty_space
		self.file_beauty_space = file_beauty_space
		self.extras = extras
		self.file = FileHandler(fn) if fn else False
		self.console_output = console_output
		self.allowed_levels = {
			"DEBUG": ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
			"INFO": ["INFO", "WARNING", "ERROR", "CRITICAL"],
			"WARNING": ["WARNING", "ERROR", "CRITICAL"],
			"ERROR": ["ERROR", "CRITICAL"],
			"CRITICAL": ["CRITICAL"]
		},
		self.level_colours = level_colours

	def extras_builder(self, extras):
		h = []
		for key, value in self.extras, extras:
				h.append(f"{key}={value}")
		return " | ".join(h)

	def beautify(self, _str):
		og_topic = _str.split(" | ")[3]
		topic = og_topic.ljust(self.topic_beauty_space)
		s = _str.replace(og_topic, f"{topic}")

		file = s.split(" | ")[2]
		file = file.ljust(self.file_beauty_space)
		s = s.replace(file, f"{file}")

		return s

	def log(self, *,
		level: str,
		extras: Optional[list] = None,
		date_fmt=r"%d-%b-%y, %H:%M:%S:%f",
		topic="None",
		file="NoFile",
		msg
	):
		time_str = datetime.now().strftime(date_fmt)

		if extras:
			extras_str = f"{self.extras_builder(extras)} | "
		else:
			extras_str = ""
		msg = self.beautify(f"{time_str} | {level}      | {file} | {topic} | {extras_str} {msg}")

		if level in self.level_colours.keys():
			level_colour = self.level_colours[level]
		else:
			level_colour = "[bold white]"

		if self.file:
			if level in self.allowed_levels[self.file_output_level]:
				self.file.write(f"{time_str} | {topic} | {msg}")
		if self.console_output:
			if level in self.allowed_levels[self.console_output_level]:
				print(f"{level_colour}[*]{msg}[/]")
