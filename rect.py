class DrawRectangle:
    def show(self):
        t.tracer(False)
        t.pensize(2)
        t.penup()
        t.goto(self.x,self.y)
        t.pendown()
        for _ in range(0,2):
            t.fd(self.width)
            t.rt(90)
            t.fd(self.height)
            t.rt(90)
