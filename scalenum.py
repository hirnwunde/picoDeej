# https://stackoverflow.com/a/42095130/5690568
def scale_number(unscaled, to_min, to_max, from_min, from_max):
  return (to_max-to_min)*(unscaled-from_min)/(from_max-from_min)+to_min
