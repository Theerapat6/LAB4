class  pyramid():
    
    Base_l =""
    Base_w = "" 
    P_h = ""
    
    def volume(self):
        vol = (self.Base_l.length_cla * self.Base_w.width_cla * self.P_h.heigth_cla ) / 3
        print("{:.2f}".format(vol))

class length_c():
       length_cla = ""
           
class width_c():
       width_cla = ""
            
class heigth_c():
        heigth_cla = ""

Pyramid = pyramid()
pyramid_b = length_c()
pyramid_w = width_c()
pyramid_h = heigth_c()

pyramid_b.length_cla = 10
pyramid_h.width_cla = 7
pyramid_w.heigth_cla = 17 

Pyramid.Base_l = pyramid_b
Pyramid.P_h = pyramid_w
Pyramid.Base_w = pyramid_h

Pyramid.volume()