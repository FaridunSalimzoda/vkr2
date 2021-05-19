var x = 0;

function addQuestion() {

    var str = '<label type="text" for="message"></label>  {{ form.title }} <label type="text" for="message" ></label> <input name="message" id="message" cols="30" rows="10" placeholder = "Добавить ответ"></input>  <div id="input' + (x + 1) + '"></div>';
    document.getElementById('input' + x).innerHTML = str;
    x++;

}

function addAnswer() {

    var str = '<label type="text" for="message" ></label> <input name="message" id="message" cols="30" rows="10" placeholder = "Добавить ответ"></input> <div id="input' + (x + 1) + '"></div>';
    document.getElementById('input' + x).innerHTML = str;
    x++;

}
