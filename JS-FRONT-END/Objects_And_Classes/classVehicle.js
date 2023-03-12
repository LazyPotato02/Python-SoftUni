class Vehicle {
    constructor(type, model, parts, fuel) {
        this.type = type;
        this.model = model;
        this.parts = parts;
        this.fuel = fuel;
        this.quality = this.parts.engine * this.parts.power;
        this.parts.quality = this.quality
    }

    drive(fuelLoss) {
        this.fuel -= fuelLoss;
    }
}