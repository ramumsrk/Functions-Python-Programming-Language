Three ways of using asterisk * in a function definition
01. Tuple of arguments
02. Dictionary of arguments
03. Function that only accepts keyword arguments
Following is applicable to both 01 and 02 above
    def \_\_new\_\_(klass, *args, **kwargs):
      return super().\_\_new\_\_(klass)
    def third_function(*args, **kwargs):
      pass
Keyword only arguments function definition
    def \_\_init\_\_(self, *, first_name: str, last_name: st) -> None
      self.first_name = first_name
      self.last_name = last_name
      return None
            