import socket
import re
import itertools

sock = socket.socket()
sock.connect(("asis-ctf.ir",12435))
sock.recv(1024)
sock.send(bytes("Sattelite\n", "utf8"))
r = re.compile(r"x\d+")
q = ["",""]
j = 6
while True:
    if len(q[1])>0:
        literal = q[1]
    else:
        literal = sock.recv(1024).decode("utf8")
    print(q)
    print(literal)
    literal = literal.replace("∨","or").replace("∧", "and").replace("¬","not ")
    s = ["x"+str(x) for x in range(1,j)]
    j+=1
    combs = list(itertools.product(["True","False"],repeat=len(s)))
    for c in combs:
        for i in range(len(c)):
            exec(s[i]+" = "+str(c[i]))
        if eval(literal) == True:
            sock.send(bytes("".join(c).replace("True","1").replace("False","0")+"\n","utf8"))
            q = sock.recv(1024).decode("utf8").split("\n");
            print(q[0])
            break
