
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('delete-btn').addEventListener('click', function() {
        var xhr = new XMLHttpRequest();
        var csrftoken = '{{ csrf_token }}';

        xhr.open('POST', "{% url 'DeleteLivro' %}", true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.setRequestHeader('X-CSRFToken', csrftoken);

        xhr.onload = function() {
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                alert(response.message);
                // Faça algo com os dados retornados
            } else {
                alert('Ocorreu um erro.');
            }
        };

        xhr.send();
    });
});



