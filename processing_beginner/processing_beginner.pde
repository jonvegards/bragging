//void setup(){
//  size(480, 120);
//}

//void draw() {
//  if (mousePressed) {
//    fill(0);
//  } else {
//    fill(255);
//  }
//  ellipse(mouseX, mouseY, 80, 80);
//} 

//void setup() {
//  size(600,600);
//  noStroke();
//  ellipseMode(RADIUS);
//  background(#FAC267, 50);
//  fill(#67C0FA, 200);
//  ellipse(200, 100, 100, 100);
//  //ellipse(400,200, 200, 200);
//  //fill(0,25, 51);
//  //ellipse(200,200, 20, 20);
//  //ellipse(400,200, 20, 20);
//  //fill(200, 50, 0);
//  //arc(300, 400, 400, 250, 0, PI);
//}

//Drawing lines with for loop
size(720,480);
strokeWeight(2);
background(0, 153, 204);

stroke(255);
float angle = 0.01
for (int i=0; i<N; i++){
  line(100, 100, 300*angle*i, 100*angle*i);  
}
