from Focus_Roots import *

def change():
    write_text("Rocket",250,20,10,color=color_white )
    set_background(color_mid_night_blue)
    draw_polygon([[100,250],[400,250],[250,130]],0,color=color_white)
    draw_rect(200,150,100,200,0,color=color_white)
    draw_polygon([[200,150],[299,150],[250,50]],0,color=color_white)
    draw_rect(200,300,100,90,0,color=color_yellow)
    draw_rect(200,300,100,40,0,color=color_firebrick)
    draw_circle(250,250,20,0,color=color_blue)
    draw_circle(250,190,20,0,color=color_blue)
    draw_circle(250,130,30,0,color=color_yellow)
    write_text("Rocket",250,20,30,color=color_white )


draw(change)