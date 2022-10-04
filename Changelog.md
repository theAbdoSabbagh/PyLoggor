I'm not sure how this works

### 1.1.3
BREAKING CHANGES
- Fix typehint for extras
- Rename `*_beauty_space` to `*_adjustment_space`
- Add option to left align, center, or right align level/topic/file, defaults to left
- Add params `console_output` and `file_output` to `log()` func in the instance you wish to log specifically deviant from base config
- Add `set_level` function, takes in `console_output_level` and/or `file_output_level`
- Internally made print above filewrite, should print 0.005 nanoseconds faster now


### 1.1.2
- Change default values of `topic_beauty_space` and `file_beauty_space` to 15
- Change default colour of `ERROR` level to `[red]` instead of `[bold red]`
- Internally better handle levels
- Default level to `DEBUG` in `log()` if not passed
- Default message to `NoMessage` in `log()` if not passed