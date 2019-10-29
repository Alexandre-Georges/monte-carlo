import numpy as np
import sys
import time
import math

def generate_samples(sample_size, variable):
  params = variable['params']
  if variable['distribution'] == 'uniform':
    return np.random.uniform(low = params['min'], high = params['max'], size = sample_size)
  elif variable['distribution'] == 'normal':
    return np.random.normal(loc = params['mean'], scale = params['std'], size = sample_size)
  elif variable['distribution'] == 'weibull':
    return np.random.weibull(params['shape'], size = sample_size)
  else:
    raise Exception('Unknown distribution')

def organise_samples(sample_size, variables):
  samples = []
  for variable in variables:
    samples.append(generate_samples(sample_size, variable))
  return np.array(samples)

def post_generation(interval_size, xile_size, mini, maxi, results):
  interval_max_index = interval_size - 1
  intervals = [0] * interval_size
  interval_width = (float(maxi) - mini) / interval_size
  for result in results:
    intervals[min(int((result - mini) / interval_width), interval_max_index)] += 1

  histogram = []
  for index in range(interval_size):
    histogram.append({ 'start': mini + index * interval_width, 'count': intervals[index] })

  xiles = []
  length = len(results)
  for index in range(xile_size):
    xiles.append({
      'low': results[index * int(length / xile_size)],
      'high': results[min((index + 1) * int(length / xile_size), length - 1)],
    })

  return {
    'histogram': histogram,
    'xiles': xiles,
  }

def evaluate(interval_size, xile_size, expression, sample_size, variables):
  report={
    'min': None,
    'max': None,
    'mean': None,
    'variance': None,
    'std': None,
    'runtime': time.time(),
  }
  results = []
  sum = 0
  variance = 0
  mini = sys.maxint
  maxi = -sys.maxint

  samples=organise_samples(sample_size, variables)
  compiled_expression=compile(expression, '<string>', 'exec')

  current_index = 0
  while current_index < sample_size:
    sample={}

    for i in range(0, len(variables)):
      sample[variables[i]['name']] = samples[i][current_index]

    exec(compiled_expression, sample)
    output = sample['output']
    sum += output
    variance += output ** 2
    mini = min(mini, output)
    maxi = max(maxi, output)

    if math.isnan(output):
      raise Exception('the expression could not be solved')

    results.append(output)
    current_index += 1

  results.sort()
  post_generation_props = post_generation(interval_size, xile_size, mini, maxi, results)
  report['histogram'] = post_generation_props['histogram']
  report['xiles'] = post_generation_props['xiles']
  report['min'] = mini
  report['max'] = maxi
  report['mean'] = sum / sample_size
  report['variance'] = variance / sample_size - report['mean'] ** 2
  report['std'] = report['variance'] ** 0.5
  report['runtime'] = time.time() - report['runtime']

  return report


#print(to_xiles(10, 1.0, 11.0, [9.9999, 10.0, 10.99, 11.0]))
#print(evaluate(100, 10, 'output=x', 1000000, [
#   { 'name': 'x', 'distribution': 'uniform', 'params': { 'min': 0.0, 'max': 10.0 }},
# ])['runtime'])
