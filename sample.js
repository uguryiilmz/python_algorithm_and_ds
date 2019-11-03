function Foo(){
    console.log(this.a);
  }
  var food = {a: "Magical this"};
  Foo.call(food); // food is this