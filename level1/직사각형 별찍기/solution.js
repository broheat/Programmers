process.stdin.setEncoding("utf8");
process.stdin.on("data", (data) => {
  const n = data.split(" ");
  const a = Number(n[0]),
    b = Number(n[1]);
  const makeRectangleByStar = (row, column) => {
    var i = 0;
    var j = 0;
    var result = "";
    for (i = 0; i < column; i++) {
      for (j = 0; j < row; j++) {
        result += "*";
      }
      result += "\n";
    }
    console.log(result);
  };
  makeRectangleByStar(a, b);
});
