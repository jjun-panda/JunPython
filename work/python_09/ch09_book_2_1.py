from calc.calculater import Calc

c =  Calc(0)

c.add(100)
c.sub(50)
c.mult(2)
c.div(5)

res = c.getResult()

print("result = ", res)