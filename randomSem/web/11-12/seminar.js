var city1 = {};
city1.name = "ГородN";
city1.population = 10000000;

var city2 = {
    name: "ГородM",
    population: 1e6
};

city1.getName = city2.getName = function () { return this.name; };
console.log(city1.getName());
console.log(city2.getName());

city1.exportStr = city2.exportStr = function () {
    return `name=${this.name}\npopulation=${this.population}\n`;
};
console.log(city1.exportStr());
console.log(city2.exportStr());

function getObj() { return this; }
city1.getCity = city2.getCity = getObj;
console.log(city1.getCity().getName() + ' ' + city1.getCity().population);
console.log(city2.getCity().getName() + ' ' + city2.getCity().population);
