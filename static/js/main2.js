

window.onload = function() {
    let solutions = document.querySelectorAll('.solution');

    solutions.forEach(function(solutionContainer, index) {
        console.log("we");

        let code = solutionContainer.innerHTML; // No necesitas buscar .solution dentro de .solution
        console.log(code)
        let editorContainer = solutionContainer.nextElementSibling;
        let editorId = "editor-lectura-" + index; // Crear un ID único para cada editor

        // Crear un nuevo div para el editor con el ID único
        let editorDiv = document.createElement("div");
        editorDiv.id = editorId;
        
        editorDiv.style.width = "500px"; 
        editorDiv.style.height = "300px";
        editorDiv.style.fontSize = "20px";

        console.log(editorId)
        console.log(editorContainer);
        editorContainer.appendChild(editorDiv);

        let readOnly = ace.edit(editorId, {
            theme: 'ace/theme/twilight',
            mode: "ace/mode/text",
            selectionStyle: "text"
        });
        readOnly.setReadOnly(true);

        var codeText = code;
        console.log(codeText)// Utiliza textContent para obtener el contenido del elemento
        readOnly.setValue(codeText, -1);
    });
};