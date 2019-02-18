from hashlib import *
print("""

        ,:oho/-.                             
   mMMMMMMMMMMMNmmdhy                    
   dMMMMMMMMMMMMMMMMMMs.                  
   +MMsohNMMMMMMMMMMMMMm/                  
   .My   .+dMMMMMMMMMMMMMh.               
    +       :NMMMMMMMMMMMMNo             
             ryMMMMMMMMMMMMMm:              
              /NMMMMMMMMMMMMMy.          
                .hMMMMMMMMMMMMMN+      
                    ``-NMMMMMMMMMd-        
                      /MMMMMMMMMMMs.     
                       mMMMMMMMsyNMN/     
                       +MMMMMMMo  :sNh.   
                       +NMMMMMMm     yn/
                        oMMMMMMM.        
                        -NMMMMMM+        
                         +MMd/NMh        
                          mMm -mN*       
                          /MM  *h:       
                           dM*   .       
                           :M-       
                            d:           
                           -+   



""")
print("_______________")
print("coded by sofi")
print("_______________")
print('1: sha-1')
print('2: sha-224')
print('3: md5')
print('4: sha-256')
print('5: sha-384')
print('6: sha-512')

j=input('====> ')
if j==1:
	n=raw_input('enter the word to hash : ')
	x=sha1(n.encode()).hexdigest()
	print(x)
elif j==2:
   	f=raw_input("enter the word to hash : ")
   	killer=sha224(f.encode()).hexdigest()
   	print(killer)
elif j==3:
	y=raw_input("enter the word to hash : ")
	hitman=md5(y.encode()).hexdigest()
	print(hitman)
elif j==4:
	g=raw_input("enter the word to hash : ")
	sofi=sha256(g.encode()).hexdigest()
	print(sofi)
elif j==5:
	k=raw_input("enter the word to hash : ")
	nhu=sha384(k.encode()).hexdigest()
	print(nhu)
elif j==6:
	m=raw_input("enter the word to hash : ")
	nh=sha512(m.encode()).hexdigest()
	print(nh)
