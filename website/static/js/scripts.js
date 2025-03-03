function clearLabels() {
	var labels = document.getElementsByTagName("label");
	for (var index = 0; index < labels.length; index++) {
		labels[index].innerHTML = "";
	}
}
document.addEventListener("DOMContentLoaded", function() {
	clearLabels();
});

