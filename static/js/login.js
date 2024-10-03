/*
 * Project: System Temp
 * Description : JS to managment of Login Page
 */
(function($){
    var LogIn = {
        init: function(){
            this.viewFieldsEmpty();
        },
        viewFieldsEmpty: function(){
            $('#username, #password').unbind().on('keydown keyup change', function () {
                console.log('typing...')
                let username = $('#username').val()
                let password = $('#password').val()
                if (username.length > 0 && password.length > 0) {
                    $('.btn-login').removeClass('disabled')
                } else {
                    $('.btn-login').addClass('disabled')
                }
            })
        },
        login: function(){
            let username = $('#username').val()
            let password = $('#password').val()
            let payload = {
                'option': 'log_in',
                'username': username,
                'password': password
            }
            Pace.track(function () {
                $.ajax({
                    method: "POST",
                    data: JSON.stringify(payload),
                    contentType: "application/json",
                    dataType: 'json',
                }).done(function (data) {
                    if (data.error_fg) {
                        Swal.fire({
                            icon: 'error',
                            title: 'Oops...',
                            text: data.error_msg,
                        })
                    } else {
                        Swal.fire({
                            title: "Inicio de sesion satisfactorio",
                            icon: "success",
                            confirmButtonText: "Ok",
                            allowOutsideClick : false,
                            allowEscapeKey: false
                        }).then(() => {
                            window.location.href = data.data.redirect_url
                          });
                          
                    }
                }).fail(function (e) {
                    console.log(e);
                });
            });
        },
        create_admin: function(){
            let payload = {
                'option': 'register_admin'
            }

            Pace.track(function () {
                $.ajax({
                    method: "POST",
                    data: JSON.stringify(payload),
                    contentType: "application/json",
                    dataType: 'json',
                }).done(function (data) {
                    if (data.error_fg) {
                        Swal.fire({
                            icon: 'error',
                            title: 'Oops...',
                            text: data.message,
                        })
                    } else {
                        Swal.fire({
                            title: "Se Creo admin, usuario: '"+data.data.user_info.username+"', correo: '"+data.data.user_info.email+"', contraseña: '"+data.data.user_info.password+"'",
                            icon: "success",
                            confirmButtonText: "Ok",
                            allowOutsideClick : false,
                            allowEscapeKey: false
                        }).then(() => {
                            location.reload()
                        });  
                    }
                }).fail(function (e) {
                    console.log(e);
                });
            });
        }
    }
    
    $(document).ready(function(){
        LogIn.init();
    })
    
    window.LogIn = LogIn;
})(jQuery)
