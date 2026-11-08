function piglatin() {
    var text = document.getElementById("Q2").value.trim();
    var a = text.split(/\s+/);
    var out = [];
    var i;
    var txt;
    for (i = 0; i < a.length; i++) {
      txt = a[i];
      if (txt === "") continue;
      out.push(txt.substring(1, txt.length) + txt.charAt(0) + "ay");
    }
    document.getElementById("display").textContent = out.join(" ");
  }