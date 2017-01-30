//bottom plank (red)
color([1, 0, 0]) translate([12, 0, 0]) cube([194, 150, 12]);

//back plank (blue)
color([0, 0, 1]) translate([206, -12, 0]) cube([12, 174, 550]);

difference() {
	//front plank (green)
	color([0, 1, 0]) cube([12, 150, 234]);
	//hole
	translate([-10, 75, 196.5]) rotate(90, [0, 1, 0])
	    cylinder(44, 12.5, 12.5, false);
};

//top plank (red)
color([1, 0, 0]) translate([0, 0, 234]) cube([206, 150, 12]);

//top plank (yellow)
color([1,1,0]) translate([-25, -12, 225]) rotate(45, [0,1,0]) cube([12, 174, 325]);

//bird section
translate([0,0,0]) {
    
    //bottom plank (yellow)
    translate([34, 0, 22]) cube([150, 150, 12]);
    
    //back plank (green) 
    color("purple") translate([184, 0, 22]) cube([12, 150, 212]);
    
    difference() {
	//front plank (blue)
	color([0, 0, 1]) translate([22, 0, 22]) cube([12, 150, 212]);
	//hole
	translate([-10, 75, 196.5]) rotate(90, [0, 1, 0])
	    cylinder(49, 12.5, 12.5, false);
    };
};

//side planks (turquoise)
color([0, 1, 1]) translate([0, 0, 0]) {
    
    
    
    //left side (from front)
    translate([0, 150, 0]) {
        //square section
        cube([206, 12, 234]);
        
        //triangle section
        translate([0, 12, 234])
        rotate(90, [1, 0, 0])
        linear_extrude(height = 12)
        polygon([[0, 0], [206, 0], [206, 206]]);
        
    }
    
    //right side (from front)
    translate([0, -12, 0]) {
        //square section
        cube([206, 12, 234]);
        
        //triangle section
        translate([0, 12, 234])
        rotate(90, [1, 0, 0])
        linear_extrude(height = 12)
        polygon([[0, 0], [206, 0], [206, 206]]);
    }
    
    
};

