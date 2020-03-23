$(function () {
    $('#exampleInputName').blur(function () {

        var name = $(this).val();
        //监听文本内容

        // alert(name);

        var reg = /^[a-z]{3,6}$/;

        b = reg.test(name);

        if (b){
            $.getJSON(
                '/user/checkname/',
                {'name':name},
                function (data) {
            //  $('#nameinfo').html('✔用户名字可以使用').css({'color':'green','font-size':10});
                    if (data['status'] === 200){
                       $('#nameinfo').html(data['msg']).css({'color':'green','font-size':15});
                    } else{
                       $('#nameinfo').html(data['msg']).css({'color': 'red', 'font-size': 15});
                    }
                })
        }
        else{
            $('#nameinfo').html('用户名字格式不正确').css({'color':'red','font-size':15});
        }
    })
});
//
$(function () {
        //
        $('#exampleInputPassword2').blur(function () {
        var pw1 =$('#exampleInputPassword1').val();
        var pw2 =$('#exampleInputPassword2').val();
        if (pw1===pw2){
            $('#pwdinfo').html('密码一致').css({'color':'green','font-size':15});
        }else {
            $('#pwdinfo').html('密码不一致').css({'color':'red','font-size':15});}
        })
        });


function parse1() {
    var password = document.getElementById('exampleInputPassword1').value;

    password = md5(password);

    document.getElementById('exampleInputPassword1').value = password;

    return true
}

