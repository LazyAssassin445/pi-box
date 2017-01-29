//bottom plank (red)
color([1, 0, 0]) translate([12, 0, 0]) cube([194, 194, 12]);

//back plank (blue)
color([0, 0, 1]) translate([206, -12, 0]) cube([12, 218, 550]);

//front plank (green)
color([0, 1, 0]) cube([12, 194, 234]);

//top plank (red)
color([1, 0, 0]) translate([0, 0, 234]) cube([206, 194, 12]);

//top plank (yellow)
color([1,1,0]) translate([-25, -12, 221]) rotate(45, [0,1,0]) cube([12, 218, 325]);

//bird section
translate([0,0,0]) {
    
    //bottom plank (yellow)
    translate([34, 34, 22]) cube([150, 150, 12]);
    
    //back plank (green) 
    color([0, 1, 0]) translate([184, 34, 22]) cube([12, 150, 215]);
    
    //front plank (blue)
    color([0, 0, 1]) translate([22, 34, 22]) cube([12, 150, 215]);
};

//side planks (turquoise)
color([0, 1, 1]) translate([0, 0, 0]) {
    
    //left side (from front)
    translate([0, -12, 0]) {
        //square section
        cube([206, 12, 234]);
        
        //triangle section
        translate([0, 12, 234])
        rotate(90, [1, 0, 0])
        linear_extrude(height = 12)
        polygon([[0, 0], [206, 0], [206, 218]]);
    }
    
    //right side (from front)
    translate([0, 194, 0]) {
        //square section
        cube([206, 12, 234]);
        
        //triangle section
        translate([0, 12, 234])
        rotate(90, [1, 0, 0])
        linear_extrude(height = 12)
        polygon([[0, 0], [206, 0], [206, 218]]);
        
    }
    
    
};


//hole
color([0, 0, 0]) translate([0, 97, 196.5]) 
    rotate(90, [0, 1, 0])
    cylinder(34, 12.5, 12.5, false);
