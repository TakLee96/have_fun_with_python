def solve(string):
  print(string)
  def s_to_l(string):
    char_array = []
    for char in string:
      char_array.append(ord(char) - ord('A'))
    return char_array
  array = s_to_l(string)
  print('converted as: ', array)
  result = [(array[0] + 5) % 25]
  for i in range(1, len(array)):
    result.append((array[i] - array[i - 1]) % 26)
  def l_to_s(list):
    char_array = []
    for num in list:
      char_array.append(chr(num + ord('A')))
    return char_array
  print('deciphered as: ', result)
  return l_to_s(result)

def interpolate_2D(x_lst, y_lst):
    x1, x2, x3, y4 = x_lst
    y1, y2, y3, y4 = y_lst
    D1 = lambda x: (x-x2)*(x-x3)/(x1-x2)/(x1-x3)
    D2 = lambda x: (x-x1)*(x-x3)/(x2-x1)/(x2-x3)
    D3 = lambda x: (x-x1)*(x-x2)/(x3-x1)/(x3-x2)
    P = lambda x: y1*D1(x) + y2*D2(x) + y3*D3(x)
    return P(x4) == y4

def find(y):
  total = 0
  for num1 in y:
    print(num1)
    quotient = 1
    for num2 in y:
      if (num1 != num2):
        quotient *= (num1 - num2)
    print(quotient)
    total += num1 / quotient
  return total
