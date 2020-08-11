import time 

def caso1(n):

    if n < 2:
        return n
    else:
        return caso1(n-1) + caso1(n-2)
    
def caso2(n):
  if n < 2:
        return n
  else:
    a=0
    b=1
    for i in range(2,n+1):
      c=a+b
      a=b
      b=c
    return(c)

# Por alguna razon en VS code no funciona pero en repl.it si
def test(number, cases):
    elapsed_times = []

    for case in cases:

        start = time.time()
        case(number)
        end = time.time()

        elapsed_times.append(end - start)
        
    print(elapsed_times)

    for i in range(len(elapsed_times)):
        if elapsed_times[i] == min(elapsed_times):
            print("El caso {} es el más eficiente".format(i+1))

test(12, [caso1, caso2])