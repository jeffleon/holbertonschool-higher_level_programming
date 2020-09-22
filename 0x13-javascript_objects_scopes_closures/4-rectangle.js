#!/usr/bin/node

class Rectangle {
    constructor(w, h){
        if((w && h) && (w > 0 && h > 0))
        {
            this.width = w;
            this.height = h;
        }
    }
    print(){
        for (let i = 0; i < this.height; i++)
            console.log('X'.repeat(this.width))
    }
    double()
    {
	this.width = this.width * 2;
	this.height = this.height * 2;
    }
    rotate()
    {
	let aux = this.width;
	this.width = this.height;
	this.height = aux;
    }
}

module.exports = Rectangle
