resultado.png sigma.png solar.png : punto3.py ci.dat dif.dat Punto1.py valores.txt Punto2.py monthrg.dat
	python punto3.py
	python Punto1.py
	python Punto2.py

ci.dat dif.dat : dif.x
	./dif.x
	
dif.x : dif.cpp
	c++ dif.cpp -o dif.x
	
