ispeed=float(input("Enter initial speed u:"))
accel=float(input("Enter acceleration   a:"))
time=float(input("Enter time travelling t:"))
print ("Object travelled %.2f"%(ispeed*time+0.5*accel*time*time),"m")
