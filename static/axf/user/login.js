function a() {
    var i = document.getElementById('changeimg');
    i.src='/user/get_code/?'+Math.random();
}



function parse() {
    var password = document.getElementById('password').value;
    // alert(password);

    password = md5(password);
    // alert(password);

        document.getElementById('password').value = password;

    return true

}
