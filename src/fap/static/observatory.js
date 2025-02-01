const canvas = document.querySelector('canvas');
const context = canvas.getContext('2d');

function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}

window.onresize = resize;
resize();

function makeStars(k) {
    positions = [];

    h = Math.floor(canvas.innerHeight / Math.floor(Math.random() * 15 + 4))
    for (y = 0; y < canvas.innerHeight; y += h) {
        w = Math.floor(canvas.innerWidth / Math.floor(Math.random() * 15 + 4))
        for (x = 0; x < canvas.innerWidth; x += w) {    
            positions.push([x, y])
        }
    }

    return positions;
}

var star_names = fetch('/get-constellation', 
    {
        method: "POST", 
        body: JSON.stringify({
            constellation: 'pipelines'
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }
).then(response => response.json());

var stars = [];
var star_positions = makeStars(stars.length);

console.log(star_positions);

for (let i = 0; i < stars.length; i++)
{
    stars.push({
        name: star_names[i], 
        x: star_positions[i][0], 
        y: star_positions[i][1], 
        radius: 10, 
        fillStyle: '#22cccc',
        strokeStyle: '#009999'
    })
}

function drawNode(node) {
    context.beginPath();
    context.fillStyle = node.fillStyle;
    context.arc(node.x, node.y, node.radius, 0, Math.PI * 2, true);
    context.strokeStyle = node.strokeStyle;
    context.stroke();
    context.fill();
}

stars.forEach(node => {
    drawNode(node)
});

function within(x, y) {
    return stars.find(n => {
        return x > (n.x - n.radius) && 
            y > (n.y - n.radius) &&
            x < (n.x + n.radius) &&
            y < (n.y + n.radius);
    });
}

function click(e) {

    let star = within(e.x, e.y);

    fetch('/star-info', 
        {
            method: "POST", 
            body: json.stringify({name: star.name}),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        }
    )
}

window.onclick = click;

// function move(e) {
//     if (selection) {
//         selection.x = e.x;
//         selection.y = e.y;
//         drawNode(selection);
//     }
// }

// function down(e) {
//     let target = within(e.x, e.y);
//     if (target) {
//         selection = target;
//     }
// }

// function up(e) {
//     selection = undefined;
// }

// window.onmousemove = move;
// window.onmousedown = down;
// window.onmouseup = up;
