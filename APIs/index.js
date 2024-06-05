async function getALLFoods() {
    try {
        const response = await fetch('http://localhost:3000/foods');
        const foods = await response.json();
        console.log('all foods;', foods);
    } catch (error) {
        console.error(error);
    }
}

async function getSpecificFoods(id) {
    try {
        const response = await fetch(`http://localhost:3000/foods/${id}`);
        const food = await response.json();
        console.log('specific food:', food);
    } catch (error) {
        console.error('specific food: {}');
    }
}

setTimeout(()=>{
    getALLFoods();
    getSpecificFoods();
}, 3000)

console.log("Asynchronous code takes time to complete")