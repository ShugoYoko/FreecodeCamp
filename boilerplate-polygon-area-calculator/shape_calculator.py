class Rectangle:
    width=0
    height=0
    
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def set_width(self,width):
        self.width=width
    def set_height(self,height):
        self.height=height
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return 2*self.width+2*self.height
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    def get_picture(self):
        if self.width>50 or self.height>50:
            return "Too big for picture."
        picture=""
        for row in range(0,self.height,1):
            for column in range(0,self.width,1):
                picture+="*"
            picture+="\n"
        return picture
    def get_amount_inside(self,another_pic):
        width_count=self.width//another_pic.width
        height_count=self.height//another_pic.height
        return width_count*height_count
    def __str__(self):
        return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"

class Square(Rectangle):
    def __init__(self,side):
        self.height=side
        self.width=side
    def set_side(self,side):
        self.height=side
        self.width=side
    def __str__(self):
        return "Square(side="+str(self.width)+")"