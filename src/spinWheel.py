import random
import bisect
def spinWheel(ids, weights):

  # Compute the cumulative sum of weights
  cumulative_weights = []
  total = 0
  for weight in weights:
    total += weight
    cumulative_weights.append(total)

# Generate a random number between 0 and weight
rand_num = random.uniform(0, total)

# Use binary search to find the index where the random number fits

index = bisect.bisect_left(cumulative_weights, rand_num)

return ids[index]
