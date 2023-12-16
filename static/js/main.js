
let editor = ace.edit("editor", {
    theme: 'ace/theme/tomorrow_night',
    mode: "ace/mode/javascript",
    selectionStyle: "text"
});

let readOnly = ace.edit("editor-lectura", {
    theme: 'ace/theme/xcode',
    mode: "ace/mode/javascript",
    selectionStyle: "text"
});
readOnly.setReadOnly(true);


// window.onload = function() {
//     let boton = document.getElementById("grabar");

//     boton.addEventListener("click", function() {
//         var code = editor.getValue();
//         console.log(code);
//         let readOnlyCode = code;
//         readOnly.setValue(readOnlyCode, -1); 
//     });
// };






