document.querySelector("input[name='barcode']").addEventListener("keypress", function(e) {
  if (e.key === "Enter") this.form.submit();
});
