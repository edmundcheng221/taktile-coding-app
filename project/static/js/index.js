// let counter = 0;
// const add = () => {
//     let parent = document.getElementById("array-item");
//     // <input name="text">
//     let node = document.createElement("input"); 
//     node.setAttribute("class", "elements");
//     parent.appendChild(node);
//     counter++;
// }
const show = () => {
    let parent = document.getElementById("array-item");
    let node = document.createElement("a"); 
    let textContent = "Submit Another Form!";
    node.appendChild(textContent);
    node.setAttribute('href',"~/");
    parent.appendChild(node);
}