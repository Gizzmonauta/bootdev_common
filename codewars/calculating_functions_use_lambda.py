# def zero(func = None): return func(0) if func else 0
# def one(func = None): return func(1) if func else 1
# def two(func = None): return func(2) if func else 2
# def three(func = None): return func(3) if func else 3
# def four(func = None): return func(4) if func else 4
# def five(func = None): return func(5) if func else 5
# def six(func = None): return func(6) if func else 6
# def seven(func = None): return func(7) if func else 7
# def eight(func = None): return func(8) if func else 8
# def nine(func = None): return func(9) if func else 9

# def plus(y): return lambda x: x + y
# def minus(y): return lambda x: x - y
# def times(y): return lambda x: x * y
# def divided_by(y): return lambda x: x // y

def zero(arg=""):  return eval("0" + arg)
def one(arg=""):   return eval("1" + arg)
def two(arg=""):   return eval("2" + arg)
def three(arg=""): return eval("3" + arg)
def four(arg=""):  return eval("4" + arg)
def five(arg=""):  return eval("5" + arg)
def six(arg=""):   return eval("6" + arg)
def seven(arg=""): return eval("7" + arg)
def eight(arg=""): return eval("8" + arg)
def nine(arg=""):  return eval("9" + arg)

def plus(n):       return '+' + str(n)
def minus(n):      return '-' + str(n)
def times(n):      return '*' + str(n)
def divided_by(n): return '//' + str(n)

def main():
    # Example usages:
    print(f"Trying seven(times(five())): {seven(times(five()))}")        # 35
    print(f"Trying four(plus(nine())): {four(plus(nine()))}")          # 13
    print(f"Trying eight(minus(three())): {eight(minus(three()))}")       # 5
    print(f"Trying six(divided_by(two())): {six(divided_by(two()))}")      # 3
    print(f"Trying one(plus(one())): {one(plus(one()))}")            # 2
    print(f"Trying two(divided_by(six())): {two(divided_by(six()))}")      # 0

if __name__ == "__main__":
    main()
