import matplotlib
import requests
import inspect

print(matplotlib.__name__)
print(callable(matplotlib))
print(inspect.ismodule(matplotlib))
print(inspect.getmodule(matplotlib.get))
print(matplotlib.executable)
print(matplotlib.version)
print(matplotlib.platform)
print(matplotlib.argv)
