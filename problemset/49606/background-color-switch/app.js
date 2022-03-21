// Github: https://github.com/mohsenebrahimyir/quera
// https://quera.ir/problemset/49606/

var changeColor = function () {
  document.body.style.backgroundColor = this.id;
};

var colors = document.getElementsByTagName("span");

for (let i = 0; i < colors.length; i++) {
  document.getElementById(colors[i].id).onclick = changeColor;
}
