def computepay(h,r):
    if h > 40.0:
     x = r * 40.0 +(1.5*r*(h-40.0))
    elif h <= 40 :
   	 x= h*r
    return x

hrs = float(input("Enter Hours:"))
rate = float(raw_input("Enter the rate:"))
p = computepay(hrs,rate)
print("Pay",p)
