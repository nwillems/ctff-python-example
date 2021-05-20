
from typing import Callable
import functools



def lookup_flag(flag_name: str) -> bool:
  # do cool magic
  print(f"Looking up, the flag: {flag_name}")
  return True

def FeatureFlaggerMiddleware():
  pass

def FeatureFlagDecorator(flag_name):
  # register flag_name
  print(f"Registering flag: {flag_name}")

  def inner(fn: Callable) -> Callable:
      @functools.wraps(fn)
      def decorated(*args, **kwargs):
        kwargs[flag_name] = lookup_flag(flag_name)
        return fn(*args, **kwargs)
      return decorated
  
  return inner

featureflag = FeatureFlagDecorator
