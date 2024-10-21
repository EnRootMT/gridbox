
import argparse

def draw_stack(origin_x, origin_y, radius, grid_size, nb, side, thickness, demi_kerf):
    
    x = origin_x 
    y = origin_y

    if side == "x":
        line_inner = (grid_size / 2 - radius)
        line_ext = line_inner

    else:
        line_inner = (grid_size / 2 - radius)
        line_ext = (grid_size / 2 - radius) - thickness

    for _ in range(nb):
        
        #left
        x = x - demi_kerf
        path_stack_line_left = "M " + str(x) + " " + str(y) +" "
        x = x + demi_kerf
        
        if _ == 0:
            x = x + line_ext

        else:
            x = x + line_inner
       
        path_stack_line_left = path_stack_line_left + "L " + str(x) + " " + str(y) + " "
        path_stack_arc_left =  "M "+str(x)+","+str(y) + " a " + str(radius)+ "," + str(radius) +  " 0 0,1 " + str(radius) +",-" + str(radius) + " "

        #right
        x = x + radius
        y = y - radius
        path_stack_arc_right = "M "+str(x)+","+str(y) + " a " + str(radius)+ "," + str(radius) +  " 0 0,1 " + str(radius) +"," + str(radius) + " "
        
        #line right
        y = y + radius
        x = x + radius
        path_stack_line_right = "M " + str(x) + " " + str(y) +" " + " "

        if _ == nb - 1:
            x = x + line_ext + demi_kerf
            

        else: 
            x = x + line_inner

        path_stack_line_right = path_stack_line_right + "L " + str(x) + " " + str(y) + " " + " "
        path_stack_for = path_stack_line_left + path_stack_arc_left + path_stack_arc_right + path_stack_line_right

        if _ > 0:
            path_stack = path_stack + path_stack_for
        else:
            path_stack = path_stack_for

    return path_stack

def calcul(lenght_y, slot_lenght):    
    nb_slots = lenght_y / slot_lenght 
    nb_slots_int = int(nb_slots)
    if (nb_slots_int % 2) == 0 : #pair
        line = (lenght_y - (nb_slots_int - 1)* slot_lenght) /2
        while (line < slot_lenght):

            nb_slots_int_new = nb_slots_int - 3
            line = (lenght_y - (nb_slots_int_new)* slot_lenght) /2
    
    else:
        line = (lenght_y - (nb_slots_int)* slot_lenght) /2
        nb_slots_int_new = nb_slots_int
        while (line < slot_lenght):
            
            nb_slots_int_new = nb_slots_int -2
            
            line = (lenght_y - (nb_slots_int_new)* slot_lenght) /2

    return line, nb_slots_int_new

def draw_vert_plus(origin_x, origin_y, thickness, slot_lenght, lenght_y, demi_kerf, part = None):

    if part == "bottom":
        line, nb_slots_int_new = calcul(lenght_y - 2 * thickness, slot_lenght)
    else:
        line, nb_slots_int_new = calcul(lenght_y, slot_lenght)

    x = origin_x
    y = origin_y

    #chaine Back left

    #A
    x_kerf = x + demi_kerf
    path_vert_right = "M " + str(x_kerf) + " " + str(y) +" "

    #B
    x = 0
    y = line
    y_kerf = y - demi_kerf
    path_vert_right = path_vert_right + "l " + str(x) + " " + str(y_kerf) + " "

    for _ in range(int(nb_slots_int_new/2)):
        
        #C
        x = thickness
        y = 0
        path_vert_right = path_vert_right + "l " + str(x) + " " + str(y) + " "

        #D
        x = 0
        y = slot_lenght
        y_kerf = y + 2 * demi_kerf
        path_vert_right = path_vert_right + "l " + str(x) + " " + str(y_kerf) + " "

        #E
        x = 0 - thickness
        y = 0
        path_vert_right = path_vert_right + "l " + str(x) + " " + str(y) + " "
        
        #F
        x = 0
        y = slot_lenght
        y_kerf = y - 2 * demi_kerf
        
        path_vert_right = path_vert_right + "l " + str(x) + " " + str(y_kerf) + " "

    x = thickness
    y = 0
    path_vert_right = path_vert_right + "l " + str(x) + " " + str(y) + " "
    y = slot_lenght
    y_kerf = y + 2 * demi_kerf
    x = 0
    path_vert_right = path_vert_right + "l " + str(x) + " " + str(y_kerf) + " "
    
    x = 0 - thickness
    y = 0
    y_kerf = y - demi_kerf
    path_vert_right = path_vert_right + "l " + str(x) + " " + str(y) + " "
    
    
    x = 0
    y = line
    y_kerf = y - demi_kerf
    
    path_vert_right = path_vert_right + "l " + str(x) + " " + str(y_kerf) + " "

    return path_vert_right

def draw_vert_minus(origin_x, origin_y, thickness, slot_lenght, lenght_y, demi_kerf, part = None):

    if part == "bottom":
        line, nb_slots_int_new = calcul(lenght_y - 2 * thickness, slot_lenght)
    else:
        line, nb_slots_int_new = calcul(lenght_y, slot_lenght)

    x = origin_x
    y = origin_y

    #chaine Back left

    #A
    x_kerf = x + demi_kerf
    y_kerf = y
    #print(f"A x : {x_kerf}, y: {y_kerf} ")
    path_vert_left = "M " + str(x_kerf) + " " + str(y_kerf) +" "
    
    #B
    x = 0
    x_kerf = x # + demi_kerf
    y = line
    y_kerf = y + demi_kerf
    #print(f"B x : {x}, y: {y} ")
    #print(f"B x : {x_kerf}, y: {y_kerf} (kerf) ")
    path_vert_left = path_vert_left + "l " + str(x_kerf) + " " + str(y_kerf) + " "

    for _ in range(int(nb_slots_int_new/2)):
        
        #C
        x = - thickness
        x_kerf = x# + demi_kerf
        y = 0
        y_kerf = y#  + demi_kerf
        #print(f"C x : {x_kerf}, y: {y_kerf} ")
        path_vert_left = path_vert_left + "l " + str(x_kerf) + " " + str(y_kerf) + " "
        
        #D
        x = 0
        x_kerf = x# + demi_kerf
        y = slot_lenght
        y_kerf = y - 2 * demi_kerf
        #print(f"D x : {x_kerf}, y: {y_kerf} ")
        path_vert_left = path_vert_left + "l " + str(x_kerf) + " " + str(y_kerf) + " "
        
        #E
        x = thickness 
        x_kerf = x #+ demi_kerf
        y = 0
        y_kerf = y #- demi_kerf
        #print(f"E x : {x_kerf}, y: {y_kerf} ")
        path_vert_left = path_vert_left + "l " + str(x_kerf) + " " + str(y_kerf) + " "

        #F
        x = 0 
        x_kerf = x #+ demi_kerf
        y = slot_lenght
        y_kerf= y + 2 * demi_kerf
        #print(f"F x : {x_kerf}, y: {y_kerf} ")
        path_vert_left = path_vert_left + "l " + str(x_kerf) + " " + str(y_kerf) + " "

    #B
    x = 0 - thickness #+ demi_kerf
    y = 0# + demi_kerf
    path_vert_left = path_vert_left + "l " + str(x) + " " + str(y) + " "
    
    #C
    y = slot_lenght# + demi_kerf
    x = 0 #+ demi_kerf
    y_kerf = y - 2 * demi_kerf
    path_vert_left = path_vert_left + "l " + str(x) + " " + str(y_kerf) + " "
    
    #D
    x =  thickness  #+ demi_kerf
    y = 0 #- demi_kerf
    path_vert_left = path_vert_left + "l " + str(x) + " " + str(y) + " "
    
    #E
    x = 0 #- demi_kerf
    y = line #+ demi_kerf
    y_kerf = y + demi_kerf
    path_vert_left = path_vert_left + "l " + str(x) + " " + str(y_kerf) + " "

    return path_vert_left

def draw_part(path_stack_top, path_vert_right, path_vert_left, path_stack_bottom, color, x_unit, y_unit,height_z, kerf, thickness, output):
    
    file = open(f"{output}.html", "a")
    
    file.write('            <path d="')
    file.write(path_stack_top)
    file.write(f'" style="fill:none;stroke:{color};stroke-width:0.20" />\n')

    file.write('            <path d="')
    file.write(path_vert_right)
    file.write(f'" style="fill:none;stroke:{color};stroke-width:0.20" />\n')

    file.write('            <path d="')
    file.write(path_vert_left)
    file.write(f'" style="fill:none;stroke:{color};stroke-width:0.20" />\n')

    file.write('            <path d="')
    file.write(path_stack_bottom)
    file.write(f'" style="fill:none;stroke:{color};stroke-width:0.20" />\n')

    file.close()

    #svg
    filesvg  = open(f"{output}-x{x_unit}-y{y_unit}-h{height_z}-t{thickness}-k{kerf}.svg", "a")
    
    filesvg.write('            <path d="')
    filesvg.write(path_stack_top)
    filesvg.write(f'" style="fill:none;stroke:{color};stroke-width:0.20" />\n')

    filesvg.write('            <path d="')
    filesvg.write(path_vert_right)
    filesvg.write(f'" style="fill:none;stroke:{color};stroke-width:0.20" />\n')

    filesvg.write('            <path d="')
    filesvg.write(path_vert_left)
    filesvg.write(f'" style="fill:none;stroke:{color};stroke-width:0.20" />\n')

    filesvg.write('            <path d="')
    filesvg.write(path_stack_bottom)
    filesvg.write(f'" style="fill:none;stroke:{color};stroke-width:0.20" />\n')

    filesvg.close()

def draw_holes(path_holes, color, x_unit, y_unit,height_z, kerf, thickness, output):
    
    file = open(f"{output}.html", "a")
    file.write('            <path d="')
    file.write(path_holes)
    file.write(f'" style="fill:none;stroke:{color};stroke-width:0.20" />\n')
    file.close()

    #svg
    filesvg  = open(f"{output}-x{x_unit}-y{y_unit}-h{height_z}-t{thickness}-k{kerf}.svg", "a")
    filesvg.write('            <path d="')
    filesvg.write(path_holes)
    filesvg.write(f'" style="fill:none;stroke:{color};stroke-width:0.20" />\n')
    filesvg.close()

def draw_horizontal_top(origin_x, origin_y, thickness, slot_lenght, width_x, demi_kerf):

    x = origin_x
    y = origin_y

    line, nb_slots_int_new = calcul(width_x, slot_lenght)

    #horizontal
    x_kerf = origin_x - demi_kerf
    y_kerf = origin_y - demi_kerf
    path_horizontal_top =  "M " + str(x_kerf) + " " + str(y) +" "

    x = 0
    y = 0
    y_kerf = y - demi_kerf
    path_horizontal_top = path_horizontal_top + "l " + str(x) + " " + str(y_kerf) + " "



    x = line
    y = 0
    kerf_x = x #- demi_kerf
    
    path_horizontal_top = path_horizontal_top + "l " + str(x) + " " + str(y) + " "

    for _ in range(int(nb_slots_int_new/2)):
        
        y = - thickness
        x = 0
        
        path_horizontal_top = path_horizontal_top + "l " + str(x) + " " + str(y) + " "
        
        x = slot_lenght
        kerf_x = x + 2 * demi_kerf
        y = 0
        path_horizontal_top = path_horizontal_top + "l " + str(kerf_x) + " " + str(y) + " "
        x = 0
        y =  thickness
        path_horizontal_top = path_horizontal_top + "l " + str(x) + " " + str(y) + " "
        y = 0
        x = slot_lenght
        kerf_x = x - 2 * demi_kerf
        path_horizontal_top = path_horizontal_top + "l " + str(kerf_x) + " " + str(y) + " "

    x = 0 
    y = 0- thickness
    path_horizontal_top = path_horizontal_top + "l " + str(x) + " " + str(y) + " "
    y = 0
    x = slot_lenght
    x_kerf = x + 2 * demi_kerf
    path_horizontal_top = path_horizontal_top + "l " + str(x_kerf) + " " + str(y) + " "
    x =  0
    y = thickness
    path_horizontal_top = path_horizontal_top + "l " + str(x) + " " + str(y) + " "
    y = 0
    x = line
    
    path_horizontal_top = path_horizontal_top + "l " + str(x) + " " + str(y) + " "

    #vertical

    x=0
    y = demi_kerf
    path_horizontal_top = path_horizontal_top + "l " + str(x) + " " + str(y) + " "


    return path_horizontal_top

def draw_horizontal_bottom(origin_x, origin_y, thickness, slot_lenght, width_x, demi_kerf):
    
    x = origin_x
    y = origin_y

    line, nb_slots_int_new = calcul(width_x, slot_lenght)

    x_kerf = x - demi_kerf
    y_kerf = y + demi_kerf

    path_horizontal_bottom = "M " + str(x_kerf) + " " + str(y) +" "

    x = 0
    y = demi_kerf
    path_horizontal_bottom = path_horizontal_bottom + "l " + str(x) + " " + str(y) + " "

    x = line
    y = 0
    path_horizontal_bottom = path_horizontal_bottom + "l " + str(x) + " " + str(y) + " "

    for _ in range(int(nb_slots_int_new/2)):
        
        y = thickness
        x = 0
        path_horizontal_bottom = path_horizontal_bottom + "l " + str(x) + " " + str(y) + " "
        y = 0
        x = slot_lenght
        x_kerf = x + 2 * demi_kerf
        path_horizontal_bottom = path_horizontal_bottom + "l " + str(x_kerf) + " " + str(y) + " "

        x = 0
        y =  0 - thickness
        path_horizontal_bottom = path_horizontal_bottom + "l " + str(x) + " " + str(y) + " "

        y = 0
        x = slot_lenght
        x_kerf = x - 2 * demi_kerf
        path_horizontal_bottom = path_horizontal_bottom + "l " + str(x_kerf) + " " + str(y) + " "

    x = 0 
    y = thickness
    path_horizontal_bottom = path_horizontal_bottom + "l " + str(x) + " " + str(y) + " "

    y = 0
    x = slot_lenght
    x_kerf = x + 2 * demi_kerf
    path_horizontal_bottom = path_horizontal_bottom + "l " + str(x_kerf) + " " + str(y) + " "
    x =  0
    y = 0 - thickness
    path_horizontal_bottom = path_horizontal_bottom + "l " + str(x) + " " + str(y) + " "
    y = 0
    x = line
    path_horizontal_bottom = path_horizontal_bottom + "l " + str(x) + " " + str(y) + " "

    x=0
    y = - demi_kerf
    path_horizontal_bottom = path_horizontal_bottom + "l " + str(x) + " " + str(y) + " "

    return path_horizontal_bottom

def draw_x_holes(origin_x, origin_y, thickness, slot_lenght, width_x, demi_kerf):

    line, nb_slots_int_new = calcul(width_x, slot_lenght)

    x = origin_x + line
    y = origin_y


    path_x_holes = ""

    for _ in range(int(nb_slots_int_new/2 + 1)):
        
        x_kerf= x + demi_kerf
        y_kerf= y - demi_kerf
        path_x_holes = path_x_holes + "M " + str(x_kerf) + " " + str(y_kerf) +" "

        y = y - thickness
        x_kerf = x + demi_kerf
        y_kerf = y + demi_kerf

        path_x_holes = path_x_holes + "L " + str(x_kerf) + " " + str(y_kerf) + " "
        
        x = x + slot_lenght
        x_kerf = x - demi_kerf
        y_kerf = y + demi_kerf
        path_x_holes = path_x_holes + "L " + str(x_kerf) + " " + str(y_kerf) + " "
        
        y = y + thickness

        x_kerf = x - demi_kerf
        y_kerf = y - demi_kerf
        path_x_holes = path_x_holes + "L " + str(x_kerf) + " " + str(y_kerf) + " "
        
        x = x - slot_lenght
        x_kerf = x + demi_kerf
        y_kerf = y - demi_kerf
        path_x_holes = path_x_holes + "L " + str(x_kerf) + " " + str(y_kerf) + " "
        x = x + 2 * slot_lenght
        

    return path_x_holes

 
def main():
    print ("on fait des boites")
    print ("let's make boxes")

    parser = argparse.ArgumentParser(description="Generate svg for making boxes with laser cutter machines using gridfinty multiples")
    
    parser.add_argument('-x', '--width', type=int, default=2, help="width, in multiple of gridfinity size (42mm). Ex: if 2 then the outer width wil be 84, default = 2")
    parser.add_argument('-y', '--depth', type=int, default=3, help="depth, in multiple of gridfinity size (42mm). Ex: if 3 then the outer depth wil be 126, default = 3")
    parser.add_argument('-ht', '--height', type=int, default=100, help="height in millimeters, default = 100")
    parser.add_argument('-k', '--kerf', type=float, default=0.2, help="the width of the laser cut, default = 0.2")
    parser.add_argument('-t', '--thickness', type=float, default=3, help="thickness of material, default = 3")
    parser.add_argument('-o', '--output', default="gridbox", help="output file name (no extension needed), default = gridbox-x-y-height-kerf html and svg")
    args = parser.parse_args()

    origin_x = 20
    origin_y = 20
    thickness = args.thickness
    slot_lenght = 7
    x_unit = args.width
    y_unit = args.depth
    grid_size = 42
    width_x = x_unit * grid_size
    depth_y = y_unit * grid_size
    height_z = args.height # grifinity multiple de 7 
    radius = 6
    holes_height = 10
    # decallage entre les morceaux de boites
    offset_x = 10 
    offset_y = 10
    kerf = args.kerf #sculpfun kerf 0.2 ok
    demi_kerf = kerf / 2
    output = args.output

    print(thickness)


    svg_height = origin_y + height_z * 2 + depth_y + offset_y *2 + 10
    svg_width = origin_x + width_x + depth_y + offset_x + 10


    #viewbox permet de creer l'echelle en passant de px à mm
    #svg height et width doit etre en mm et identique à celui de la viewbox (viexbox sans unite)
    file = open(f"{output}.html", "w")
    file.write(f'<html>\n    <body>\n        <svg height="{svg_height}mm" viewBox="0.0 0.0 {svg_width} {svg_height}" width="{svg_width}mm">\n')
    file.close()

    filesvg = open(f"{output}-x{x_unit}-y{y_unit}-h{height_z}-t{thickness}-k{kerf}.svg", "w")
    filesvg .write(f'<svg height="{svg_height}mm" viewBox="0.0 0.0 {svg_width} {svg_height}" width="{svg_width}mm">\n')
    filesvg .close()

    #box bottom
    part = "bottom"
    origin_x_bottom = origin_x + thickness
    path_top = draw_horizontal_top(origin_x_bottom, origin_y, thickness, slot_lenght, width_x - thickness * 2, demi_kerf )
    path_left = draw_vert_minus(origin_x_bottom, origin_y, thickness, slot_lenght, depth_y, -demi_kerf, part)
    path_right = draw_vert_plus(origin_x_bottom + width_x  - thickness * 2, origin_y, thickness, slot_lenght, depth_y, demi_kerf, part)
    path_bottom = draw_horizontal_bottom(origin_x_bottom, origin_y + depth_y - 2 * thickness, thickness, slot_lenght, width_x  - thickness * 2, demi_kerf)
    draw_part(path_top, path_right, path_left, path_bottom, "blue", x_unit, y_unit,height_z, kerf, thickness, output)

    #box back
    origin_y_back = origin_y + depth_y + offset_y
    side = "x"
    
    path_stack_top = draw_stack(origin_x,origin_y_back,radius,grid_size,x_unit, side, thickness, demi_kerf)
    path_vert_left = draw_vert_plus(origin_x,origin_y_back, thickness,slot_lenght, height_z, - demi_kerf)
    path_vert_right = draw_vert_minus(origin_x + width_x , origin_y_back, thickness,slot_lenght, height_z, demi_kerf)
    path_stack_bottom = draw_stack(origin_x,origin_y_back + height_z, radius, grid_size,x_unit, side, thickness, demi_kerf)
    draw_part(path_stack_top, path_vert_right, path_vert_left, path_stack_bottom, "blue", x_unit, y_unit,height_z, kerf, thickness, output)

    #holes_back
    origin_y_holes_back = origin_y + depth_y + height_z - holes_height + offset_y
    #draw_x_holes(origin_x, origin_y, thickness, slot_lenght, width_x):
    path_x_holes = draw_x_holes(origin_x_bottom, origin_y_holes_back , thickness, slot_lenght, width_x - thickness * 2, demi_kerf)
    draw_holes(path_x_holes, "red", x_unit, y_unit,height_z, kerf, thickness, output)

    #box right
    side = "y"
    origin_x_right = origin_x + width_x + offset_x
    origin_y_right = origin_y + depth_y + offset_y
    path_stack_top = draw_stack(origin_x_right, origin_y_right,radius,grid_size,y_unit, side, thickness, demi_kerf)
    path_vert_left = draw_vert_minus(origin_x_right, origin_y_right, thickness,slot_lenght, height_z, - demi_kerf)
    path_vert_right = draw_vert_plus(origin_x_right - 2 * thickness + depth_y , origin_y_right, thickness,slot_lenght, height_z, demi_kerf)
    path_stack_bottom = draw_stack(origin_x_right, origin_y_right + height_z, radius, grid_size,y_unit, side, thickness, demi_kerf)
    draw_part(path_stack_top, path_vert_right, path_vert_left, path_stack_bottom, "blue", x_unit, y_unit,height_z, kerf, thickness, output)

    #holes_right
    origin_x_holes_back = origin_x + width_x + offset_x
    origin_y_holes_back = origin_y + depth_y + height_z - holes_height + offset_y
    path_x_holes = draw_x_holes(origin_x_holes_back, origin_y_holes_back , thickness, slot_lenght, depth_y - thickness * 2, demi_kerf)
    draw_holes(path_x_holes, "red", x_unit, y_unit,height_z, kerf, thickness, output)

    #box front
    side = "x"
    origin_y_front = depth_y + origin_y + height_z + offset_y *2
    path_stack_top = draw_stack(origin_x,origin_y_front,radius,grid_size,x_unit, side, thickness, demi_kerf)
    path_vert_left = draw_vert_plus(origin_x,origin_y_front, thickness,slot_lenght, height_z, - demi_kerf)
    path_vert_right = draw_vert_minus(origin_x + width_x , origin_y_front, thickness,slot_lenght, height_z, demi_kerf)
    path_stack_bottom = draw_stack(origin_x,origin_y_front + height_z, radius, grid_size,x_unit, side, thickness, demi_kerf)
    draw_part(path_stack_top, path_vert_right, path_vert_left, path_stack_bottom, "blue", x_unit, y_unit,height_z, kerf, thickness, output)

    #holes_front
    origin_y_holes_front = origin_y + depth_y + height_z *2 - holes_height + offset_y *2 
    path_x_holes = draw_x_holes(origin_x_bottom, origin_y_holes_front , thickness, slot_lenght, width_x - thickness * 2, demi_kerf)
    draw_holes(path_x_holes, "red", x_unit, y_unit,height_z, kerf, thickness, output)

    #box left
    side = "y"
    origin_x_left =  origin_x + width_x + offset_x
    origin_y_left = depth_y + origin_y + height_z + offset_y * 2 
    path_stack_top = draw_stack(origin_x_left,origin_y_left,radius, grid_size,y_unit, side, thickness, demi_kerf)
    path_vert_left = draw_vert_minus(origin_x_left, origin_y_left , thickness, slot_lenght, height_z, - demi_kerf)
    path_vert_right = draw_vert_plus(origin_x_left + depth_y - 2 * thickness, origin_y_left, thickness, slot_lenght, height_z, demi_kerf)
    path_stack_bottom = draw_stack(origin_x_left,origin_y_left + height_z, radius, grid_size, y_unit, side, thickness, demi_kerf)
    draw_part(path_stack_top, path_vert_right, path_vert_left, path_stack_bottom, "blue", x_unit, y_unit,height_z, kerf, thickness, output)

    #holes_left
    origin_x_holes_left = origin_x + width_x + offset_x
    origin_y_holes_left = origin_y + depth_y + height_z *2 - holes_height + offset_y *2 
    path_x_holes = draw_x_holes(origin_x_holes_left, origin_y_holes_left , thickness, slot_lenght, depth_y - thickness * 2, demi_kerf)
    draw_holes(path_x_holes, "red", x_unit, y_unit,height_z, kerf, thickness, output)

    file = open(f"{output}.html", "a")
    file.write("        </svg>\n    </body>\n</html>\n")
    file.close()

    filesvg  = open(f"{output}-x{x_unit}-y{y_unit}-h{height_z}-t{thickness}-k{kerf}.svg", "a")
    filesvg .write("</svg>\n")
    filesvg .close()
    

if __name__ == '__main__':
    main()
